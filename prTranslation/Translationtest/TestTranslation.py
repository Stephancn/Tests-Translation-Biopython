import unittest

from prTranslation.Translationtest.Translation import translatecommondna
from prTranslation.Translationtest.Translation import translateMitocondrialdna
from prTranslation.Translationtest.Translation import translaterna
from prTranslation.Translationtest.Translation import translateStop
from prTranslation.Translationtest.Translation import translateBacterial

class TestTranslation(unittest.TestCase):
    #Test para traducir dna normal:
    def test_translatecommondna(self):
        self.assertEqual(str(translatecommondna('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')), "MAIVMGR*KGAR*")
    #Test para traducir adn mitocondrial:
    def test_translatemitocondrialdna(self):
        self.assertEqual(str(translateMitocondrialdna('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')), "MAIVMGRWKGAR*")

    #Test para traducir rna:
    def test_translaterna(self):
        self.assertEqual(str(translaterna('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG')), "MAIVMGR*KGAR*")

    #Test para traducir una secuencia con stop definitivo:
    def test_translateStop(self):
        self.assertEqual(str(translateStop('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')), "MAIVMGR")

    # Test para traducir dna bacteriano con un codón de comienzo no estándar:
    def test_translateBacterial(self):
        self.assertEqual(str(translateBacterial('GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCATAA')), "MKKMQSIVLALSLVLVAPMA")

if __name__ == "__main__":
    unittest.main()