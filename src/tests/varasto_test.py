import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollautuu(self):
        testi_varasto = Varasto(-1)
        self.assertAlmostEqual(testi_varasto.tilavuus, 0)

    def test_negatiivinen_saldo_nollautuu(self):
        testi_varasto = Varasto(10, -1)
        self.assertAlmostEqual(testi_varasto.saldo, 0)

    def test_saldo_ei_suurempi_kuin_tilavuus(self):
        testi_varasto = Varasto(10, 11)
        self.assertAlmostEqual(testi_varasto.saldo, testi_varasto.tilavuus)

    def test_negatiivista_numeroa_ei_voi_lisata(self):
        temp_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, temp_saldo)

    def test_varaston_tilavuutta_ei_voi_ylittaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivista_numeroa_ei_voi_poistaa(self):
        temp_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, temp_saldo)

    def test_varastosta_ei_voi_poistaa_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.ota_varastosta(6), 5)

    def test_str_palautus_toimii(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
