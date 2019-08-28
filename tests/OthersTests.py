import unittest
import pycreator_core


class InformationsTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual(pycreator_core.__version__, "0.0.1")
