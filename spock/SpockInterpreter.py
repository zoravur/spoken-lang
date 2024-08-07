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

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        # var_type = ctx.type_().getText() if ctx.type_() else None
        self.environment.declare(var_name)
        return None
    
    def visitDefinition(self, ctx):
        # var_type = ctx.type_().getText() if ctx.type_() else None
        value = self.visit(ctx.expression())
        var_name = ctx.ID().getText()
        self.environment.declare(var_name)
        self.environment.set(var_name, value)
        return None

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.environment.set(var_name, value)
        # print(self.environment)
        # print(self.environment.get(var_name))
        return None

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expression())
        print(value)
        return None

    def visitExpression(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
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
        args = self.visit(ctx.list_())

        if (ctx.ID().getText().lower() == 'sum'):
            return args[0] + args[1]
        elif (ctx.ID().getText().lower() == 'product'):
            return args[0] * args[1]
        elif (ctx.ID().getText().lower() == 'difference'):
            return args[0] - args[1]
        elif (ctx.ID().getText().lower() == 'quotient'):
            return args[0] // args[1]
        # else:
            # raise Exception(f"Function '{ctx.ID().getText()}' not defined")

        func_name = ctx.ID().getText().lower()
        # if func_name not in self.environment:
        #     raise Exception(f"Function '{func_name}' not defined")
        try:
            return self.environment.get(func_name)(*args)
        except Exception as e:
            print(e)
        # return self.environment.get(func_name)(*args)

    def visitList(self, ctx):
        result = [self.visit(expr) for expr in ctx.expression()]
        return result
    
    def visitArglist(self, ctx: SpockParser.ArglistContext):
        return [arg.getText() for arg in ctx.ID()]

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
        
