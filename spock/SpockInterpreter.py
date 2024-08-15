from antlr4 import *
from gen.SpockLexer import SpockLexer
from gen.SpockParser import SpockParser
from gen.SpockVisitor import SpockVisitor
from Environment import Environment

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value


class SpockInterpreter(SpockVisitor):
    def __init__(self):
        self.environment = Environment()
        self.word_to_number = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
            'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20
        }

        self._inject_builtins()

    def visitId(self, ctx: SpockParser.IdContext):
        id = ' '.join(part.getText() for part in ctx.ID_PART())
        # print(id)
        return id

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitDeclaration(self, ctx):
        # print(ctx.id_().toStringTree())
        # print(ctx.expression().toStringTree())
        # var_name = ctx.ID().getText()
        var_name = self.visit(ctx.id_())
        # var_type = ctx.type_().getText() if ctx.type_() else None
        self.environment.declare(var_name)
        return None
    
    def visitDefinition(self, ctx: SpockParser.DefinitionContext):
        # print(self.visitId(ctx.id_()).toStringTree())
        # print(ctx.expression().toStringTree())
        # var_type = ctx.type_().getText() if ctx.type_() else None
        value = self.visitExpression(ctx.expression())
        # print(value)
        # var_name = ctx.ID().getText()
        var_name = self.visit(ctx.id_())
        # print(f"Defining {var_name} as {value}")
        self.environment.declare(var_name)
        self.environment.set(var_name, value)
        return None

    def visitAssignment(self, ctx):
        # var_name = ctx.ID().getText()
        var_name = self.visit(ctx.id_())
        value = self.visit(ctx.expression())
        self.environment.set(var_name, value)
        # print(self.environment)
        # print(self.environment.get(var_name))
        return None

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expression())
        print(value)
        return None

    def visitExpression(self, ctx: SpockParser.ExpressionContext):
        # print(list(ctx)[0].toStringTree())
        if ctx.id_():
            # var_name = ctx.ID().getText()
            var_name = self.visitId(ctx.id_())
            # print(self.environment, var_name)
            return self.environment.get(var_name) # throws exception if not defined
        elif ctx.STRING():
            return ctx.STRING().getText()[6:-8]  # Remove quotes
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.WORD_NUMBER():
            return self.word_to_number[ctx.WORD_NUMBER().getText().lower()]
        else:
            return self.visitChildren(ctx)

    def visitCall(self, ctx):
        # print('call')
        args = self.visit(ctx.list_())
        # print(args)

        fn = self.visitExpression(ctx.expression())

        if callable(fn):
            return fn(*args)

    def _inject_builtins(self):
        self.environment.declare('sum')
        self.environment.set('sum', lambda x, y: x + y)
        self.environment.declare('product')
        self.environment.set('product', lambda x, y: x * y)
        self.environment.declare('difference')
        self.environment.set('difference', lambda x, y: x - y)
        self.environment.declare('quotient')
        self.environment.set('quotient', lambda x, y: x // y)
        self.environment.declare('remainder')
        self.environment.set('remainder', lambda x, y: x % y)
        self.environment.declare('greater')
        self.environment.set('greater', lambda x, y: x > y)
        self.environment.declare('less')
        self.environment.set('less', lambda x, y: x < y)
        self.environment.declare('equal')
        self.environment.set('equal', lambda x, y: x == y)
        self.environment.declare('not equal')
        self.environment.set('not equal', lambda x, y: x != y)
        self.environment.declare('not')
        self.environment.set('not', lambda x: not x)
        self.environment.declare('conj')
        self.environment.set('conj', lambda x, y: x and y)
        self.environment.declare('or')
        self.environment.set('or', lambda x, y: x or y)

    def visitList(self, ctx):
        result = [self.visit(expr) for expr in ctx.expression()]
        return result
    
    def visitArglist(self, ctx: SpockParser.ArglistContext):
        return [self.visitId(arg) for arg in ctx.id_()]

    def visitIfStatement(self, ctx):
        # if self.visit(ctx.expression()):
        #     self.visit(ctx.statement(0))
        # elif ctx.ELSE():
        #     self.visit(ctx.statement(1))
        if self.visit(ctx.expression()):
            self.visit(ctx.statement())

    def visitWhileLoop(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.statement())

    def visitBlock(self, ctx, new_env=None):
        if new_env is None:
            new_env = Environment(self.environment)
        self.environment = new_env
        result = self.visitChildren(ctx)
        self.environment = self.environment._enclosing
        return result

    def visitLambda(self, ctx):
        self.args = self.visit(ctx.arglist())

        closure = self.environment
        lambda_env = Environment(closure)

        def lambda_func(*args):
            try:
                for i, arg in enumerate(self.args):
                    lambda_env.declare(arg)
                    lambda_env.set(arg, args[i])
            
                self.visitBlock(ctx.block(), lambda_env)
            except ReturnException as e:
                return e.value
        return lambda_func

    def visitReturnStatement(self, ctx: SpockParser.ReturnStatementContext):
        return_value = self.visit(ctx.expression())
        raise ReturnException(return_value)
        
def process_input(interpreter, input_text):
    # print(input_text)
    input_stream = InputStream(input_text)
    lexer = SpockLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SpockParser(stream)
    tree = parser.program()

    # print(tree.toStringTree(recog=parser))

    # print('Interpreting...')
    interpreter.visit(tree)
