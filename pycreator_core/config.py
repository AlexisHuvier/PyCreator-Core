import json
import os


class Config:
    def __init__(self):
        with open(os.path.join(os.path.abspath(os.path.split(__file__)[0]), "config.json"), "r") as f:
            self.config = json.load(f)

    def get(self, key, default):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(os.path.join(os.path.abspath(os.path.split(__file__)[0]), "config.json"), "w") as f:
            json.dump(self.config, f)
