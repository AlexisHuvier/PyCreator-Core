from pycreator_core.filesystem import FileSystem

import re


double_car = {
    "'": "'",
    '"': '"',
    "(": ")",
    "{": "}",
    "[": "]"
}


class Analyser:
    def __init__(self, config):
        self.config = config

    def update_code(self, code):
        if len(code):
            if self.config.get("doublechar", True):
                code = double_car.get(code[-1], "")
            else:
                code = ""
        return code

    @staticmethod
    def information_file(file):
        code = FileSystem.open(file)

        return {
            "lines": tuple(code.split("\n")),
            "comments": tuple([i for i in re.findall(r"#+([^\n]+)", code) if i != ""]),
            "variables": tuple(set(re.findall(r"(\w+)\s*=[^=]", code)))
        }

