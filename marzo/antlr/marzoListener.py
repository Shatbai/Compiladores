# Generated from c:\Users\andyv\Desktop\Escuela\Sem feb-jun 22\Diseño Compi\abdul_itesm-tc3048-202211-b79baf5d7348\abdul_itesm-tc3048-202211-b79baf5d7348\ejemplosANTLR\marzo\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#suma.
    def enterSuma(self, ctx:marzoParser.SumaContext):
        pass

    # Exit a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        pass


    # Enter a parse tree produced by marzoParser#variable.
    def enterVariable(self, ctx:marzoParser.VariableContext):
        pass

    # Exit a parse tree produced by marzoParser#variable.
    def exitVariable(self, ctx:marzoParser.VariableContext):
        pass


    # Enter a parse tree produced by marzoParser#primaria.
    def enterPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass

    # Exit a parse tree produced by marzoParser#primaria.
    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass


    # Enter a parse tree produced by marzoParser#comp.
    def enterComp(self, ctx:marzoParser.CompContext):
        pass

    # Exit a parse tree produced by marzoParser#comp.
    def exitComp(self, ctx:marzoParser.CompContext):
        pass


    # Enter a parse tree produced by marzoParser#boleano.
    def enterBoleano(self, ctx:marzoParser.BoleanoContext):
        pass

    # Exit a parse tree produced by marzoParser#boleano.
    def exitBoleano(self, ctx:marzoParser.BoleanoContext):
        pass


    # Enter a parse tree produced by marzoParser#declaracion.
    def enterDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by marzoParser#declaracion.
    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by marzoParser#asig.
    def enterAsig(self, ctx:marzoParser.AsigContext):
        pass

    # Exit a parse tree produced by marzoParser#asig.
    def exitAsig(self, ctx:marzoParser.AsigContext):
        pass


    # Enter a parse tree produced by marzoParser#ifnoelse.
    def enterIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifnoelse.
    def exitIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        pass


    # Enter a parse tree produced by marzoParser#ifelse.
    def enterIfelse(self, ctx:marzoParser.IfelseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifelse.
    def exitIfelse(self, ctx:marzoParser.IfelseContext):
        pass



del marzoParser