import unittest
import pycreator_core


class FakeStdout:
    def __init__(self):
        self.contenu = ""

    def write(self, data):
        self.contenu += data


class DocumentationTests(unittest.TestCase):
    def test_getdoc(self):
        self.assertEqual(pycreator_core.get_doc("compile"), "https://docs.python.org/3/search.html?q=compile")

    def test_gethemlp(self):
        std = FakeStdout()
        pycreator_core.get_help("WTF", std.write)
        self.assertEqual(std.contenu, "No Python documentation found for 'WTF'.\nUse help() to get the interactive "
                                      "help utility.\nUse help(str) for help on the str class.\n\n")
        std.contenu = ""
        pycreator_core.get_help("pycreator_core", std.write)
        self.assertEqual(std.contenu, """Help on package pycreator_core:

NAME
    pycreator_core

PACKAGE CONTENTS
    analyse
    autocompletion
    config
    documentation
    execute
    filesystem
    history
    snippets
    utils

VERSION
    1.0.0

FILE
    d:\programmation\python\projet\pycreator\pycreator-core\pycreator_core\__init__.py


""")
