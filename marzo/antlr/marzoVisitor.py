# Generated from c:\Users\andyv\Desktop\Escuela\Sem feb-jun 22\Diseño Compi\abdul_itesm-tc3048-202211-b79baf5d7348\abdul_itesm-tc3048-202211-b79baf5d7348\ejemplosANTLR\marzo\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#suma.
    def visitSuma(self, ctx:marzoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#variable.
    def visitVariable(self, ctx:marzoParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#primaria.
    def visitPrimaria(self, ctx:marzoParser.PrimariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#comp.
    def visitComp(self, ctx:marzoParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#boleano.
    def visitBoleano(self, ctx:marzoParser.BoleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declaracion.
    def visitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#asig.
    def visitAsig(self, ctx:marzoParser.AsigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifnoelse.
    def visitIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifelse.
    def visitIfelse(self, ctx:marzoParser.IfelseContext):
        return self.visitChildren(ctx)



del marzoParser