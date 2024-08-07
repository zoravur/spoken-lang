# Generated from Spock.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SpockParser import SpockParser
else:
    from SpockParser import SpockParser

# This class defines a complete generic visitor for a parse tree produced by SpockParser.

class SpockVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpockParser#program.
    def visitProgram(self, ctx:SpockParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#statement.
    def visitStatement(self, ctx:SpockParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#printStatement.
    def visitPrintStatement(self, ctx:SpockParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#returnStatement.
    def visitReturnStatement(self, ctx:SpockParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#block.
    def visitBlock(self, ctx:SpockParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#declaration.
    def visitDeclaration(self, ctx:SpockParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#type.
    def visitType(self, ctx:SpockParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#assignment.
    def visitAssignment(self, ctx:SpockParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#definition.
    def visitDefinition(self, ctx:SpockParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#whileLoop.
    def visitWhileLoop(self, ctx:SpockParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#expression.
    def visitExpression(self, ctx:SpockParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#lambda.
    def visitLambda(self, ctx:SpockParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#call.
    def visitCall(self, ctx:SpockParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#arglist.
    def visitArglist(self, ctx:SpockParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpockParser#list.
    def visitList(self, ctx:SpockParser.ListContext):
        return self.visitChildren(ctx)



del SpockParser