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

VERSION
    0.0.1

FILE
    d:\programmation\python\projet\pycreator\pycreator-core\pycreator_core\__init__.py


""")
