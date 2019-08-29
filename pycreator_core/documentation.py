import sys

from pycreator_core.utils import FakeStdout

__all__ = ["get_doc", "get_help"]


def get_doc(name):
    return "https://docs.python.org/3/search.html?q="+name


def get_help(name):
    saveout = sys.stdout
    fake = FakeStdout()
    sys.stdout = fake
    help(name)
    sys.stdout = saveout
    return fake.contenu
