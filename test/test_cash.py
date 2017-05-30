import unittest
from controlls.controll import TaxaBmg, TaxaCaixa

class TestClass03(unittest.TestCase):
    def test_taxa_bmg(self):
        Bmg = TaxaBmg()
        self.assertEqual(10, Bmg.calcular_taxa(100, 10))

    def test_taxa_cx(self):
        Cx = TaxaCaixa()
        self.assertEqual(30, Cx.calcular_taxa(1000,3))



