import sys

from pycreator_core.utils import FakeStdout

__all__ = ["get_doc", "get_help"]


def get_doc(name):
    return "https://docs.python.org/3/search.html?q="+name


def get_help(name, write):
    saveout = sys.stdout
    fake = FakeStdout(write)
    sys.stdout = fake
    help(name)
    sys.stdout = saveout
