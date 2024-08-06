from antlr4 import *
from SpockLexer import SpockLexer
from SpockParser import SpockParser
from SpockVisitor import SpockVisitor

class SpockInterpreter(SpockVisitor):
    def __init__(self):
        self.variables = {}

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
            return ctx.STRING().getText()[6:-8]  # Remove 'quote' and 'unquote'
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        else:
            return self.visitChildren(ctx)

    def visitCall(self, ctx):
        if (ctx.ID().getText().lower() == 'sum'):
            args = self.visit(ctx.list_())
            return args[0] + args[1]

    def visitList(self, ctx):
        result = [self.visit(expr) for expr in ctx.expression()]
        return result

def main(filename):
    input_stream = FileStream(filename)
    lexer = SpockLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SpockParser(stream)
    tree = parser.program()

    interpreter = SpockInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a filename as an argument.")
