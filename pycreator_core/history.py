class History:
    def __init__(self):
        self.history = []
        self.current = len(self.history)

    def get_back(self):
        if self.current > 0:
            self.current -= 1
        return self.history[self.current]

    def get_forward(self):
        self.current += 1
        if self.current < len(self.history):
            return self.history[self.current]
        return ""

    def add(self, texte):
        self.history.append(texte)
        self.current = len(self.history)
