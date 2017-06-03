class _TaxaEmprestimo():

   def __init__(self, valor_emprestimo, percentual):
       self.valor_emprestimo = valor_emprestimo
       self.percentual = percentual

def calcular_taxa(self):
       raise NotImplementedError('Exception raised, ImageFinder is supposed to be an interface / abstract class!')


class _TaxaBmg(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0 :
           taxa = self.valor_emprestimo/100 * self.percentual

        return taxa

class _TaxaCaixa(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaPan(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaItau(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaBradesco(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaBomSucesso(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaMercantil(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaDaycoval(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa
class _TaxaMatone(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa
class _TaxaBgnCartao(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaPanCartao(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaSafra(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa
class _TaxaSafraCartao(_TaxaEmprestimo):

    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

class _TaxaBB(_TaxaEmprestimo):
    def calcular_taxa(self):
        taxa = 0
        if self.valor_emprestimo > 0 and self.percentual > 0:
            taxa = self.valor_emprestimo / 100 * self.percentual

        return taxa

OPCOES_TAXAS = [_TaxaBB, _TaxaBgnCartao, _TaxaBmg, _TaxaBomSucesso, _TaxaBradesco, _TaxaCaixa, _TaxaDaycoval,
                _TaxaItau, _TaxaMatone, _TaxaMercantil, _TaxaPan, _TaxaPanCartao, _TaxaSafra, _TaxaSafraCartao

                ]
class CalcMelhorTaxa:
     def __init__(self, taxa):
        self.taxa = taxa


     def calcular(self):
         opcao_taxa = OPCOES_TAXAS[self.taxa]
         opcao = opcao_taxa()
         return opcao.calcular_taxa()
