from gen.SpockLexer import SpockLexer
from gen.SpockParser import SpockParser
from gen.SpockVisitor import SpockVisitor

class SpockInterpreter(SpockVisitor):
    def __init__(self):
        self.variables = {}
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
        var_type = ctx.type_().getText() if ctx.type_() else None
        self.variables[var_name] = None
        return None

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        if var_name in self.variables:
            self.variables[var_name] = value
        else:
            raise Exception(f"Variable '{var_name}' not declared")
        return None

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expression())
        print(value)
        return None

    def visitExpression(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise Exception(f"Variable '{var_name}' not defined")
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove quotes
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.WORD_NUMBER():
            return self.word_to_number[ctx.WORD_NUMBER().getText().lower()]
        else:
            return self.visitChildren(ctx)

    def visitCall(self, ctx):
        if (ctx.ID().getText().lower() == 'sum'):
            args = self.visit(ctx.list_())
            return args[0] + args[1]

    def visitList(self, ctx):
        result = [self.visit(expr) for expr in ctx.expression()]
        return result

    def visitWhileLoop(self, ctx):
	    pass
        
