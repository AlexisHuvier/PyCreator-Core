import unittest
import pycreator_core


class BasicRunTests(unittest.TestCase):
    def test_interactive_withouterror(self):
        self.assertEqual(pycreator_core.execute_interactive("print('oui')"), "oui\n")
        self.assertEqual(pycreator_core.execute_interactive("x = 3"), '')
        self.assertEqual(pycreator_core.execute_interactive("abs(-4)"), '4\n')
        self.assertEqual(pycreator_core.execute_interactive("pow(2, 2)"), '4\n')

    def test_file_withouterror(self):
        self.assertEqual(pycreator_core.execute_file("code.py", "print('oui')"), "oui\n")
        self.assertEqual(pycreator_core.execute_file("code.py", "x = 3"), '')
        self.assertEqual(pycreator_core.execute_file("code.py", "abs(-4)"), '')
        self.assertEqual(pycreator_core.execute_file("code.py", "pow(2, 2)"), '')

    def test_interactive_withsyntaxerror(self):
        self.assertEqual(pycreator_core.execute_interactive("print)"), "  File \"<input>\", line 1\n    print)\n      "
                                                                       "   ^\nSyntaxError: invalid syntax\n")
        self.assertEqual(pycreator_core.execute_interactive("x === 3"), "  File \"<input>\", line 1\n    x === 3\n    "
                                                                        "    ^\nSyntaxError: invalid syntax\n")

    def test_file_withsyntaxerror(self):
        self.assertEqual(pycreator_core.execute_file("code.py", "print)"),
                         "  File \"code.py\", line 1\n    print)\n         ^\nSyntaxError: invalid syntax\n")
        self.assertEqual(pycreator_core.execute_file("code.py", "x === 3"),
                         "  File \"code.py\", line 1\n    x === 3\n        ^\nSyntaxError: invalid syntax\n")

    def test_interactive_witherrorinexecution(self):
        self.assertEqual(pycreator_core.execute_interactive("print(y)"), "Traceback (most recent call last):\n  File \""
                                                                         "<input>\", line 1, in <module>\nNameError: "
                                                                         "name 'y' is not defined\n")
        self.assertEqual(pycreator_core.execute_interactive("x = 3/0"), "Traceback (most recent call last):\n  File \""
                                                                        "<input>\", line 1, in <module>\n"
                                                                        "ZeroDivisionError: division by zero\n")

    def test_file_witherrorinexecution(self):
        self.assertEqual(pycreator_core.execute_file("code.py", "print(y)"),
                         "Traceback (most recent call last):\n  File \"code.py\", line 1, in <module>\n    \"\"\""
                         "Utilities needed to emulate Python's interactive interpreter.\nNameError: name 'y' is not "
                         "defined\n")
        self.assertEqual(pycreator_core.execute_file("code.py", "x = 3/0"),
                         "Traceback (most recent call last):\n  File \"code.py\", line 1, in <module>\n    \"\"\""
                         "Utilities needed to emulate Python's interactive interpreter.\nZeroDivisionError: division by"
                         " zero\n")
