import unittest
import pycreator_core


class InformationsTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual(pycreator_core.__version__, "0.0.1")


class DocumentationTests(unittest.TestCase):
    def test_getdoc(self):
        self.assertEqual(pycreator_core.get_doc("compile"), "https://docs.python.org/3/search.html?q=compile")

    def test_gethemlp(self):
        self.assertEqual(pycreator_core.get_help("WTF"), "No Python documentation found for 'WTF'.\n"
                                                         "Use help() to get the interactive help utility.\n"
                                                         "Use help(str) for help on the str class.\n\n")
        self.assertEqual(pycreator_core.get_help("pycreator_core"), """Help on package pycreator_core:

NAME
    pycreator_core

PACKAGE CONTENTS
    documentation
    execute
    utils

VERSION
    0.0.1

FILE
    d:\programmation\python\projet\pycreator\pycreator-core\pycreator_core\__init__.py


""")
class ConfigTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = pycreator_core.Config()

    def test_get_set(self):
        self.assertEqual(self.config.get("EXISTE PAS", "oui"), "oui")
        self.assertEqual(self.config.get("last_file", "oui"), "")
        self.config.set("last_file", "test.py")
        self.assertEqual(self.config.get("last_file", "oui"), "test.py")


class HistoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.history = pycreator_core.History()
        self.history.add("oui")
        self.history.add("non")

    def test_history(self):
        self.assertEqual(self.history.get_back(), "non")
        self.assertEqual(self.history.get_back(), "oui")
        self.assertEqual(self.history.get_back(), "oui")
        self.assertEqual(self.history.get_forward(), "non")
        self.assertEqual(self.history.get_forward(), "")