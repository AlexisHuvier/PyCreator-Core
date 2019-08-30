import unittest
import pycreator_core


class SnippetsTests(unittest.TestCase):
    def test_whileT(self):
        self.assertEqual(pycreator_core.get_snippet("whileT"), "while True:")
        self.assertEqual(pycreator_core.get_snippet("blabla whileT"), "blabla while True:")

    def test_invalid(self):
        self.assertEqual(pycreator_core.get_snippet("WTF"), "WTF")