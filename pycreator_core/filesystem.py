class FileSystem:
    @staticmethod
    def save(filename, code):
        with open(filename, "w") as f:
            f.write(code)

    @staticmethod
    def open(filename):
        with open(filename, "r") as f:
            return f.read()
