# Generated from c:\Users\andyv\Desktop\Escuela\Sem feb-jun 22\Diseño Compi\abdul_itesm-tc3048-202211-b79baf5d7348\abdul_itesm-tc3048-202211-b79baf5d7348\ejemplosANTLR\marzo\antlr\marzo.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("D\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\2\6\2\25\n\2\r\2\16\2\26\5\2")
        buf.write("\31\n\2\3\3\3\3\3\3\5\3\36\n\3\3\3\3\3\3\3\7\3#\n\3\f")
        buf.write("\3\16\3&\13\3\3\4\3\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7B\n\7\3\7\2\3\4\b\2\4\6\b\n\f\2\2\2D\2\30")
        buf.write("\3\2\2\2\4\35\3\2\2\2\6,\3\2\2\2\b.\3\2\2\2\n\61\3\2\2")
        buf.write("\2\fA\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3\2\2")
        buf.write("\2\21\17\3\2\2\2\21\22\3\2\2\2\22\31\3\2\2\2\23\25\5\b")
        buf.write("\5\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3")
        buf.write("\2\2\2\27\31\3\2\2\2\30\17\3\2\2\2\30\24\3\2\2\2\31\3")
        buf.write("\3\2\2\2\32\33\b\3\1\2\33\36\7\n\2\2\34\36\7\f\2\2\35")
        buf.write("\32\3\2\2\2\35\34\3\2\2\2\36$\3\2\2\2\37 \f\5\2\2 !\7")
        buf.write("\3\2\2!#\5\4\3\6\"\37\3\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3")
        buf.write("\2\2\2%\5\3\2\2\2&$\3\2\2\2\'(\5\4\3\2()\7\4\2\2)*\5\4")
        buf.write("\3\2*-\3\2\2\2+-\7\13\2\2,\'\3\2\2\2,+\3\2\2\2-\7\3\2")
        buf.write("\2\2./\7\5\2\2/\60\7\f\2\2\60\t\3\2\2\2\61\62\7\f\2\2")
        buf.write("\62\63\7\6\2\2\63\64\5\4\3\2\64\13\3\2\2\2\65\66\7\7\2")
        buf.write("\2\66\67\5\4\3\2\678\7\b\2\289\5\f\7\29B\3\2\2\2:;\7\7")
        buf.write("\2\2;<\5\4\3\2<=\7\b\2\2=>\5\f\7\2>?\7\t\2\2?@\5\f\7\2")
        buf.write("@B\3\2\2\2A\65\3\2\2\2A:\3\2\2\2B\r\3\2\2\2\t\21\26\30")
        buf.write("\35$,A")
        return buf.getvalue()


class marzoParser ( Parser ):

    grammarFileName = "marzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'<'", "'var'", "'='", "'si'", 
                     "'entonces'", "'si no'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Numero", "Boolean", "Variable", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_comparar = 2
    RULE_declarar = 3
    RULE_asignar = 4
    RULE_sentencias = 5

    ruleNames =  [ "program", "expression", "comparar", "declarar", "asignar", 
                   "sentencias" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Numero=8
    Boolean=9
    Variable=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def declarar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.DeclararContext)
            else:
                return self.getTypedRuleContext(marzoParser.DeclararContext,i)


        def getRuleIndex(self):
            return marzoParser.RULE_program

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

        localctx = marzoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.Numero, marzoParser.Variable]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 12
                    self.expression(0)
                    self.state = 15 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==marzoParser.Numero or _la==marzoParser.Variable):
                        break

                pass
            elif token in [marzoParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 17
                    self.declarar()
                    self.state = 20 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==marzoParser.T__2):
                        break

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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(marzoParser.Variable, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class PrimariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaria" ):
                return visitor.visitPrimaria(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = marzoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.Numero]:
                localctx = marzoParser.PrimariaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.match(marzoParser.Numero)
                pass
            elif token in [marzoParser.Variable]:
                localctx = marzoParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(marzoParser.Variable)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = marzoParser.SumaContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 29
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 30
                    self.match(marzoParser.T__0)
                    self.state = 31
                    self.expression(4) 
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompararContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_comparar

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompContext(CompararContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.CompararContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)


    class BoleanoContext(CompararContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.CompararContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Boolean(self):
            return self.getToken(marzoParser.Boolean, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoleano" ):
                listener.enterBoleano(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoleano" ):
                listener.exitBoleano(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoleano" ):
                return visitor.visitBoleano(self)
            else:
                return visitor.visitChildren(self)



    def comparar(self):

        localctx = marzoParser.CompararContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comparar)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.Numero, marzoParser.Variable]:
                localctx = marzoParser.CompContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.expression(0)
                self.state = 38
                self.match(marzoParser.T__1)
                self.state = 39
                self.expression(0)
                pass
            elif token in [marzoParser.Boolean]:
                localctx = marzoParser.BoleanoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(marzoParser.Boolean)
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


    class DeclararContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_declarar

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionContext(DeclararContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.DeclararContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(marzoParser.Variable, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)



    def declarar(self):

        localctx = marzoParser.DeclararContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declarar)
        try:
            localctx = marzoParser.DeclaracionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(marzoParser.T__2)
            self.state = 45
            self.match(marzoParser.Variable)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_asignar

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsigContext(AsignarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.AsignarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(marzoParser.Variable, 0)
        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsig" ):
                listener.enterAsig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsig" ):
                listener.exitAsig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsig" ):
                return visitor.visitAsig(self)
            else:
                return visitor.visitChildren(self)



    def asignar(self):

        localctx = marzoParser.AsignarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignar)
        try:
            localctx = marzoParser.AsigContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(marzoParser.Variable)
            self.state = 48
            self.match(marzoParser.T__3)
            self.state = 49
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_sentencias

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfnoelseContext(SentenciasContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.SentenciasContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def sentencias(self):
            return self.getTypedRuleContext(marzoParser.SentenciasContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfnoelse" ):
                listener.enterIfnoelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfnoelse" ):
                listener.exitIfnoelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfnoelse" ):
                return visitor.visitIfnoelse(self)
            else:
                return visitor.visitChildren(self)


    class IfelseContext(SentenciasContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.SentenciasContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(marzoParser.SentenciasContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfelse" ):
                listener.enterIfelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfelse" ):
                listener.exitIfelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)



    def sentencias(self):

        localctx = marzoParser.SentenciasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sentencias)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = marzoParser.IfnoelseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(marzoParser.T__4)
                self.state = 52
                self.expression(0)
                self.state = 53
                self.match(marzoParser.T__5)
                self.state = 54
                self.sentencias()
                pass

            elif la_ == 2:
                localctx = marzoParser.IfelseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(marzoParser.T__4)
                self.state = 57
                self.expression(0)
                self.state = 58
                self.match(marzoParser.T__5)
                self.state = 59
                self.sentencias()
                self.state = 60
                self.match(marzoParser.T__6)
                self.state = 61
                self.sentencias()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




