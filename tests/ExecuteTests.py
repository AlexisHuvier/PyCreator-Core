import unittest
import pycreator_core


class FakeStdout:
    def __init__(self):
        self.contenu = ""

    def write(self, data):
        self.contenu += data


class BasicRunTests(unittest.TestCase):
    def setUp(self) -> None:
        self.std = FakeStdout()

    def test_interactive_withouterror(self):
        pycreator_core.execute_interactive("print('oui')", self.std.write)
        self.assertEqual(self.std.contenu, "oui\n")
        self.std.contenu = ""
        pycreator_core.execute_interactive("x = 3", self.std.write)
        self.assertEqual(self.std.contenu, '')

    def test_file_withouterror(self):
        pycreator_core.execute_file("code.py", self.std.write, "print('oui')")
        self.assertEqual(self.std.contenu, "oui\n")
        self.std.contenu = ""
        pycreator_core.execute_file("code.py", self.std.write, "x = 3")
        self.assertEqual(self.std.contenu, '')

    def test_interactive_withsyntaxerror(self):
        pycreator_core.execute_interactive("print)", self.std.write)
        self.assertEqual(self.std.contenu, "  File \"<input>\", line 1\n    print)\n         ^\nSyntaxError: invalid "
                                           "syntax\n")
        self.std.contenu = ""
        pycreator_core.execute_interactive("x === 3", self.std.write)
        self.assertEqual(self.std.contenu, "  File \"<input>\", line 1\n    x === 3\n        ^\nSyntaxError: invalid "
                                           "syntax\n")

    def test_file_withsyntaxerror(self):
        pycreator_core.execute_file("code.py", self.std.write, "print)")
        self.assertEqual(self.std.contenu,
                         "  File \"code.py\", line 1\n    print)\n         ^\nSyntaxError: invalid syntax\n")
        self.std.contenu = ""
        pycreator_core.execute_file("code.py", self.std.write, "x === 3")
        self.assertEqual(self.std.contenu,
                         "  File \"code.py\", line 1\n    x === 3\n        ^\nSyntaxError: invalid syntax\n")

    def test_interactive_witherrorinexecution(self):
        pycreator_core.execute_interactive("print(y)", self.std.write)
        self.assertEqual(self.std.contenu, "Traceback (most recent call last):\n  File \"<input>\", line 1, in "
                                           "<module>\nNameError: name 'y' is not defined\n")
        self.std.contenu = ""
        pycreator_core.execute_interactive("x = 3/0", self.std.write)
        self.assertEqual(self.std.contenu, "Traceback (most recent call last):\n  File \"<input>\", line 1, in "
                                           "<module>\nZeroDivisionError: division by zero\n")

    def test_file_witherrorinexecution(self):
        pycreator_core.execute_file("code.py", self.std.write, "print(y)")
        self.assertEqual(self.std.contenu,
                         "Traceback (most recent call last):\n  File \"code.py\", line 1, in <module>\n    \"\"\""
                         "Utilities needed to emulate Python's interactive interpreter.\nNameError: name 'y' is not "
                         "defined\n")
        self.std.contenu = ""
        pycreator_core.execute_file("code.py", self.std.write, "x = 3/0")
        self.assertEqual(self.std.contenu,
                         "Traceback (most recent call last):\n  File \"code.py\", line 1, in <module>\n    \"\"\""
                         "Utilities needed to emulate Python's interactive interpreter.\nZeroDivisionError: division by"
                         " zero\n")
