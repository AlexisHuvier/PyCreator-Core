import sys

__all__ = ["get_doc", "get_help"]


class FakeStdout:
    def __init__(self):
        self.contenu = ""

    def write(self, data):
        self.contenu += data


def get_doc(name):
    return "https://docs.python.org/3/search.html?q="+name


def get_help(name):
    saveout = sys.stdout
    fake = FakeStdout()
    sys.stdout = fake
    help(name)
    sys.stdout = saveout
    return fake.contenu
