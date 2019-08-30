import pycreator_core
import unittest


class AutoCompletionTests(unittest.TestCase):
    def test_autocompletion(self):
        self.assertEqual(pycreator_core.get_completion("is"), ['isinstance', 'issubclass', 'Ellipsis',
                                                               'FileExistsError', 'PermissionError',
                                                               'ZeroDivisionError', 'list', 'pycreator_core.history'])
        self.assertEqual(pycreator_core.get_completion("import"), ['importlib', 'importlib._bootstrap',
                                                                   'importlib._bootstrap_external', 'importlib.abc',
                                                                   'importlib.machinery', 'importlib.util',
                                                                   '__import__', '_frozen_importlib',
                                                                   '_frozen_importlib_external', 'zipimport'])
