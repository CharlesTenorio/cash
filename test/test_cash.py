import unittest
from controlls.taxas import _TaxaBmg, _TaxaCaixa,_TaxaBB, _TaxaBgnCartao,  _TaxaBomSucesso, _TaxaBradesco, _TaxaDaycoval, _TaxaItau, _TaxaMatone, _TaxaMercantil, _TaxaPan, _TaxaPanCartao, _TaxaSafra, _TaxaSafraCartao

class TestClass03(unittest.TestCase):
    def test_taxa_bmg(self):
        Bmg = _TaxaBmg(100,10)
        self.assertEqual(10, Bmg.calcular_taxa())

    def test_taxa_cx(self):
        Cx = _TaxaCaixa(1000,3)
        self.assertEqual(30, Cx.calcular_taxa())

    def test_taxa_bb(self):
        Bb = _TaxaBB(1000, 3)
        self.assertEqual(30, Bb.calcular_taxa())

    def test_taxa_bgn_cartao(self):
        BmgCartao = _TaxaBgnCartao(1000, 3)
        self.assertEqual(30, BmgCartao.calcular_taxa())

    def test_taxa_bom_sucesso(self):
        Bs = _TaxaBomSucesso(1000,3)
        self.assertEqual(30, Bs.calcular_taxa())

    def test_taxa_bradesco(self):
        Brad = _TaxaBradesco(1000, 3)
        self.assertEqual(30, Brad.calcular_taxa())

    def test_taxa_daycoval(self):
        Day = _TaxaDaycoval(1000,3)
        self.assertEqual(30, Day.calcular_taxa())

    def test_taxa_itau(self):
        It = _TaxaItau(1000, 3)
        self.assertEqual(30, It.calcular_taxa())

    def test_taxa_matone(self):
        Mt = _TaxaMatone(1000,3)
        self.assertEqual(30, Mt.calcular_taxa())

    def test_taxa_Mercantil(self):
         Mc= _TaxaMercantil(1000,3)
         self.assertEqual(30, Mc.calcular_taxa())

    def test_taxa_pan(self):
        Pan = _TaxaPan(1000, 3)
        self.assertEqual(30, Pan.calcular_taxa())

    def test_taxa_pan_cartao(self):
        Panc = _TaxaPanCartao(1000,3)
        self.assertEqual(30, Panc.calcular_taxa())

    def test_taxa_safra(self):
        sf = _TaxaSafra(1000,3)
        self.assertEqual(30, sf.calcular_taxa())

    def test_taxa_safra_crt(self):
        sfcrt = _TaxaSafraCartao(1000, 3)
        self.assertEqual(30, sfcrt.calcular_taxa())




