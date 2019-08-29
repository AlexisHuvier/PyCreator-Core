class FakeStdout:
    def __init__(self):
        self.contenu = ""

    def write(self, data):
        self.contenu += data

    def flush(self):
        pass
