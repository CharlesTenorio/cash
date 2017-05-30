import types

class TaxatEmprestimo:
   def calcular_taxa(self, valor_emprestimo, percentual):
       raise NotImplementedError('Exception raised, ImageFinder is supposed to be an interface / abstract class!')


class TaxaBmg(TaxatEmprestimo):

    def calcular_taxa(self, valor_emprestimo, percentual):
        taxa = 0
        if valor_emprestimo > 0 and percentual > 0 :
           taxa = valor_emprestimo/100 * percentual

        return taxa

class TaxaCaixa(TaxatEmprestimo):

    def calcular_taxa(self, valor_emprestimo, percentual):

        taxa = valor_emprestimo/100 * percentual
        return  taxa

class TaxaPan(TaxatEmprestimo):

    def calcular_taxa(self, valor_emprestimo, percentual):
        taxa = valor_emprestimo/100 * percentual
        return taxa

class TaxaItau(TaxatEmprestimo):

    def calcular_taxa(self, valor_emprestimo, percentual):
        taxa = valor_emprestimo/100 * percentual
        return taxa




