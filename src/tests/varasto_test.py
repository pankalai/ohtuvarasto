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

    def test_tulostaa_oikein(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_ota_varasto_negatiivinen_maara(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-5), 0.0)

    def test_ota_varastota_yli_saldon(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.ota_varastosta(12), 10.0)

    def test_lisaa_varastoon_negatiivinen_maara(self):
        self.assertAlmostEqual(self.varasto.lisaa_varastoon(-5), None)

    def test_ylisuuri_lisays_tayttaa_tilavuuteen_asti(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10.0)

    def test_virheellinen_tilavuus_nollataan(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)

    def test_virheellinen_alkusaldo_nollataan(self):
        self.varasto = Varasto(10,-2)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_ylisuuresta_alkusaldosta_menee_hukkaan(self):
        self.varasto = Varasto(10,12)
        self.assertAlmostEqual(self.varasto.saldo, 10.0)
