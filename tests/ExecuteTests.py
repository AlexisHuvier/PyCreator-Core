import unittest
import pycreator_core


class BasicRunTests(unittest.TestCase):
    def test_interactive_withouterror(self):
        self.assertIsNone(pycreator_core.execute_interactive("print('oui')"))
        self.assertIsNone(pycreator_core.execute_interactive("x = 3"))
        self.assertIsNone(pycreator_core.execute_interactive("abs(-4)"))
        self.assertIsNone(pycreator_core.execute_interactive("pow(2, 2)"))

    def test_file_withouterror(self):
        self.assertIsNone(pycreator_core.execute_file("print('oui')"))
        self.assertIsNone(pycreator_core.execute_file("x = 3"))
        self.assertIsNone(pycreator_core.execute_file("abs(-4)"))
        self.assertIsNone(pycreator_core.execute_file("pow(2, 2)"))

    def test_interactive_withsyntaxerror(self):
        self.assertIsNotNone(pycreator_core.execute_interactive("print)"))
        self.assertIsNotNone(pycreator_core.execute_interactive("x === 3"))

    def test_file_withsyntaxerror(self):
        self.assertIsNotNone(pycreator_core.execute_file("print)"))
        self.assertIsNotNone(pycreator_core.execute_file("x === 3"))

    def test_interactive_witherrorinexecution(self):
        self.assertIsNotNone(pycreator_core.execute_interactive("print(y)"))
        self.assertIsNotNone(pycreator_core.execute_interactive("x = 3/0"))

    def test_file_witherrorinexecution(self):
        self.assertIsNotNone(pycreator_core.execute_file("print(y)"))
        self.assertIsNotNone(pycreator_core.execute_file("x = 3/0"))
