# Generated from Spock.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,
        3,1,3,4,3,44,8,3,11,3,12,3,45,1,3,1,3,1,4,1,4,1,4,3,4,53,8,4,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,73,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        11,1,11,4,11,88,8,11,11,11,12,11,89,1,11,1,11,1,12,1,12,4,12,96,
        8,12,11,12,12,12,97,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,
        18,20,22,24,0,1,1,0,5,7,102,0,27,1,0,0,0,2,36,1,0,0,0,4,38,1,0,0,
        0,6,41,1,0,0,0,8,49,1,0,0,0,10,54,1,0,0,0,12,56,1,0,0,0,14,60,1,
        0,0,0,16,72,1,0,0,0,18,74,1,0,0,0,20,81,1,0,0,0,22,85,1,0,0,0,24,
        93,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,
        0,29,30,1,0,0,0,30,1,1,0,0,0,31,37,3,8,4,0,32,37,3,12,6,0,33,37,
        3,4,2,0,34,37,3,14,7,0,35,37,3,6,3,0,36,31,1,0,0,0,36,32,1,0,0,0,
        36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,39,5,1,
        0,0,39,40,3,16,8,0,40,5,1,0,0,0,41,43,5,2,0,0,42,44,3,2,1,0,43,42,
        1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,
        47,48,5,3,0,0,48,7,1,0,0,0,49,50,5,4,0,0,50,52,5,18,0,0,51,53,3,
        10,5,0,52,51,1,0,0,0,52,53,1,0,0,0,53,9,1,0,0,0,54,55,7,0,0,0,55,
        11,1,0,0,0,56,57,5,18,0,0,57,58,5,8,0,0,58,59,3,16,8,0,59,13,1,0,
        0,0,60,61,5,9,0,0,61,62,5,10,0,0,62,63,3,16,8,0,63,64,5,11,0,0,64,
        65,3,2,1,0,65,15,1,0,0,0,66,73,5,18,0,0,67,73,5,19,0,0,68,73,5,20,
        0,0,69,73,5,17,0,0,70,73,3,18,9,0,71,73,3,20,10,0,72,66,1,0,0,0,
        72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,
        0,0,0,73,17,1,0,0,0,74,75,5,12,0,0,75,76,5,13,0,0,76,77,3,22,11,
        0,77,78,5,14,0,0,78,79,5,15,0,0,79,80,3,6,3,0,80,19,1,0,0,0,81,82,
        5,16,0,0,82,83,5,18,0,0,83,84,3,24,12,0,84,21,1,0,0,0,85,87,5,2,
        0,0,86,88,5,18,0,0,87,86,1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,
        90,1,0,0,0,90,91,1,0,0,0,91,92,5,3,0,0,92,23,1,0,0,0,93,95,5,10,
        0,0,94,96,3,16,8,0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,
        98,1,0,0,0,98,99,1,0,0,0,99,100,5,11,0,0,100,25,1,0,0,0,7,29,36,
        45,52,72,89,97
    ]

class SpockParser ( Parser ):

    grammarFileName = "Spock.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'begin'", "'end'", "'declare'", 
                     "'function'", "'integer'", "'string'", "'equals'", 
                     "'while'", "'left'", "'right'", "'lambda'", "'takes'", 
                     "'and'", "'does'", "'call'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'flush'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WORD_NUMBER", "ID", "STRING", "NUMBER", 
                      "COMMENT", "MULTILINE_COMMENT", "WS", "FLUSH" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_printStatement = 2
    RULE_block = 3
    RULE_declaration = 4
    RULE_type = 5
    RULE_assignment = 6
    RULE_whileLoop = 7
    RULE_expression = 8
    RULE_lambda = 9
    RULE_call = 10
    RULE_arglist = 11
    RULE_list = 12

    ruleNames =  [ "program", "statement", "printStatement", "block", "declaration", 
                   "type", "assignment", "whileLoop", "expression", "lambda", 
                   "call", "arglist", "list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    WORD_NUMBER=17
    ID=18
    STRING=19
    NUMBER=20
    COMMENT=21
    MULTILINE_COMMENT=22
    WS=23
    FLUSH=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpockParser.StatementContext)
            else:
                return self.getTypedRuleContext(SpockParser.StatementContext,i)


        def getRuleIndex(self):
            return SpockParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SpockParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 262678) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(SpockParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(SpockParser.AssignmentContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(SpockParser.PrintStatementContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(SpockParser.WhileLoopContext,0)


        def block(self):
            return self.getTypedRuleContext(SpockParser.BlockContext,0)


        def getRuleIndex(self):
            return SpockParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SpockParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.declaration()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.printStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.whileLoop()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SpockParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SpockParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = SpockParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(SpockParser.T__0)
            self.state = 39
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpockParser.StatementContext)
            else:
                return self.getTypedRuleContext(SpockParser.StatementContext,i)


        def getRuleIndex(self):
            return SpockParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SpockParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(SpockParser.T__1)
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.statement()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 262678) != 0)):
                    break

            self.state = 47
            self.match(SpockParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SpockParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(SpockParser.TypeContext,0)


        def getRuleIndex(self):
            return SpockParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = SpockParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(SpockParser.T__3)
            self.state = 50
            self.match(SpockParser.ID)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0):
                self.state = 51
                self.type_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpockParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = SpockParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SpockParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(SpockParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SpockParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SpockParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(SpockParser.ID)
            self.state = 57
            self.match(SpockParser.T__7)
            self.state = 58
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SpockParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(SpockParser.StatementContext,0)


        def getRuleIndex(self):
            return SpockParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = SpockParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(SpockParser.T__8)
            self.state = 61
            self.match(SpockParser.T__9)
            self.state = 62
            self.expression()
            self.state = 63
            self.match(SpockParser.T__10)
            self.state = 64
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SpockParser.ID, 0)

        def STRING(self):
            return self.getToken(SpockParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(SpockParser.NUMBER, 0)

        def WORD_NUMBER(self):
            return self.getToken(SpockParser.WORD_NUMBER, 0)

        def lambda_(self):
            return self.getTypedRuleContext(SpockParser.LambdaContext,0)


        def call(self):
            return self.getTypedRuleContext(SpockParser.CallContext,0)


        def getRuleIndex(self):
            return SpockParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SpockParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(SpockParser.ID)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(SpockParser.STRING)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(SpockParser.NUMBER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.match(SpockParser.WORD_NUMBER)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.lambda_()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.call()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arglist(self):
            return self.getTypedRuleContext(SpockParser.ArglistContext,0)


        def block(self):
            return self.getTypedRuleContext(SpockParser.BlockContext,0)


        def getRuleIndex(self):
            return SpockParser.RULE_lambda

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda" ):
                listener.enterLambda(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda" ):
                listener.exitLambda(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambda" ):
                return visitor.visitLambda(self)
            else:
                return visitor.visitChildren(self)




    def lambda_(self):

        localctx = SpockParser.LambdaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lambda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(SpockParser.T__11)
            self.state = 75
            self.match(SpockParser.T__12)
            self.state = 76
            self.arglist()
            self.state = 77
            self.match(SpockParser.T__13)
            self.state = 78
            self.match(SpockParser.T__14)
            self.state = 79
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SpockParser.ID, 0)

        def list_(self):
            return self.getTypedRuleContext(SpockParser.ListContext,0)


        def getRuleIndex(self):
            return SpockParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = SpockParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SpockParser.T__15)
            self.state = 82
            self.match(SpockParser.ID)
            self.state = 83
            self.list_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SpockParser.ID)
            else:
                return self.getToken(SpockParser.ID, i)

        def getRuleIndex(self):
            return SpockParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = SpockParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(SpockParser.T__1)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.match(SpockParser.ID)
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==18):
                    break

            self.state = 91
            self.match(SpockParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpockParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SpockParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SpockParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = SpockParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(SpockParser.T__9)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.expression()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2035712) != 0)):
                    break

            self.state = 99
            self.match(SpockParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





