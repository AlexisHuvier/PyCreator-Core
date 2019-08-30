import unittest
import pycreator_core


class AnalyseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = pycreator_core.Config()
        self.analyser = pycreator_core.Analyser(self.config)

    def test_doublechar(self):
        self.assertEqual(self.analyser.update_code("Bonjour"), "Bonjour")
        self.assertEqual(self.analyser.update_code("Bonjour'"), "Bonjour''")
        self.config.set("doublechar", False)
        self.assertEqual(self.analyser.update_code("Bonjour'"), "Bonjour'")
