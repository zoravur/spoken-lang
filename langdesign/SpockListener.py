# Generated from Spock.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SpockParser import SpockParser
else:
    from SpockParser import SpockParser

# This class defines a complete listener for a parse tree produced by SpockParser.
class SpockListener(ParseTreeListener):

    # Enter a parse tree produced by SpockParser#program.
    def enterProgram(self, ctx:SpockParser.ProgramContext):
        pass

    # Exit a parse tree produced by SpockParser#program.
    def exitProgram(self, ctx:SpockParser.ProgramContext):
        pass


    # Enter a parse tree produced by SpockParser#statement.
    def enterStatement(self, ctx:SpockParser.StatementContext):
        pass

    # Exit a parse tree produced by SpockParser#statement.
    def exitStatement(self, ctx:SpockParser.StatementContext):
        pass


    # Enter a parse tree produced by SpockParser#printStatement.
    def enterPrintStatement(self, ctx:SpockParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by SpockParser#printStatement.
    def exitPrintStatement(self, ctx:SpockParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by SpockParser#block.
    def enterBlock(self, ctx:SpockParser.BlockContext):
        pass

    # Exit a parse tree produced by SpockParser#block.
    def exitBlock(self, ctx:SpockParser.BlockContext):
        pass


    # Enter a parse tree produced by SpockParser#declaration.
    def enterDeclaration(self, ctx:SpockParser.DeclarationContext):
        pass

    # Exit a parse tree produced by SpockParser#declaration.
    def exitDeclaration(self, ctx:SpockParser.DeclarationContext):
        pass


    # Enter a parse tree produced by SpockParser#type.
    def enterType(self, ctx:SpockParser.TypeContext):
        pass

    # Exit a parse tree produced by SpockParser#type.
    def exitType(self, ctx:SpockParser.TypeContext):
        pass


    # Enter a parse tree produced by SpockParser#assignment.
    def enterAssignment(self, ctx:SpockParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SpockParser#assignment.
    def exitAssignment(self, ctx:SpockParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SpockParser#whileLoop.
    def enterWhileLoop(self, ctx:SpockParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by SpockParser#whileLoop.
    def exitWhileLoop(self, ctx:SpockParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by SpockParser#expression.
    def enterExpression(self, ctx:SpockParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SpockParser#expression.
    def exitExpression(self, ctx:SpockParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SpockParser#lambda.
    def enterLambda(self, ctx:SpockParser.LambdaContext):
        pass

    # Exit a parse tree produced by SpockParser#lambda.
    def exitLambda(self, ctx:SpockParser.LambdaContext):
        pass


    # Enter a parse tree produced by SpockParser#call.
    def enterCall(self, ctx:SpockParser.CallContext):
        pass

    # Exit a parse tree produced by SpockParser#call.
    def exitCall(self, ctx:SpockParser.CallContext):
        pass


    # Enter a parse tree produced by SpockParser#arglist.
    def enterArglist(self, ctx:SpockParser.ArglistContext):
        pass

    # Exit a parse tree produced by SpockParser#arglist.
    def exitArglist(self, ctx:SpockParser.ArglistContext):
        pass


    # Enter a parse tree produced by SpockParser#list.
    def enterList(self, ctx:SpockParser.ListContext):
        pass

    # Exit a parse tree produced by SpockParser#list.
    def exitList(self, ctx:SpockParser.ListContext):
        pass



del SpockParser