import json
import os


class Config:
    def __init__(self):
        with open(os.path.join(os.path.abspath(os.path.split(__file__)[0]), "config.json"), "r") as f:
            self.config = json.load(f)

    def get(self, key, default):
        l = key.split(".")
        if len(l) == 1:
            return self.config.get(key, default)
        else:
            value = self.config
            for i in l:
                if i != l[-1]:
                    value = value[i]
                else:
                    value = value.get(i, default)
            return value

    def set(self, key, value):
        l = key.split(".")
        if len(l) == 1:
            self.config[key] = value
        else:
            tochange = self.config
            for i in l:
                if i != l[-1]:
                    tochange = tochange[i]
                else:
                    tochange[i] = value

    def save(self):
        with open(os.path.join(os.path.abspath(os.path.split(__file__)[0]), "config.json"), "w") as f:
            json.dump(self.config, f)
