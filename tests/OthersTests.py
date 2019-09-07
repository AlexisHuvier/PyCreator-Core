import unittest
import pycreator_core


class InformationsTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual(pycreator_core.__version__, "1.0.0")


class FileSystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.filesys = pycreator_core.FileSystem

    def test_save(self):
        self.filesys.save("files/test.py", "print('oui')")
        with open("files/test.py", "r") as f:
            self.assertEqual(f.read(), "print('oui')")

    def test_open(self):
        with open("files/test.py", "w") as f:
            f.write("print('oui')")
        self.assertEqual(self.filesys.open("files/test.py"), "print('oui')")

    def test_list(self):
        with open("files/wtf.txt", "w") as f:
            f.write(str(self.filesys.list_files(".")))
        self.assertEqual(self.filesys.list_files("."), {
            'AnalyseTests.py': None, 'AutoCompletionTests.py': None, 'DocumentationTests.py': None,
            'ExecuteTests.py': None, 'files': {'test.py': None, 'wtf.txt': None}, 'launch_tests.py': None,
            'OthersTests.py': None, 'SnippetsTests.py': None, '__pycache__': {
                'AnalyseTests.cpython-37.pyc': None, 'AutoCompletionTests.cpython-37.pyc': None,
                'DocumentationTests.cpython-37.pyc': None, 'ExecuteTests.cpython-37.pyc': None,
                'OthersTests.cpython-37.pyc': None, 'SnippetsTests.cpython-37.pyc': None
            }
        })


class ConfigTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = pycreator_core.Config()

    def test_get_set(self):
        self.assertEqual(self.config.get("EXISTE PAS", "oui"), "oui")
        self.assertEqual(self.config.get("folder", "oui"), "")
        self.config.set("folder", "test")
        self.assertEqual(self.config.get("folder", "oui"), "test")


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