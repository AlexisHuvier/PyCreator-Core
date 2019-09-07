class FakeStdout:
    def __init__(self, function):
        self.function = function

    def write(self, data):
        self.function(data)

    def flush(self):
        pass
