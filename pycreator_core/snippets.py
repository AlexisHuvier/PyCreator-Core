snippets = {
    "whileT": "while True:"
}


def get_snippet(code):
    text = code.split(" ")[-1]
    if len(code.split(" ")[:-1]) > 0:
        return " ".join(code.split(" ")[:-1]) + " " + snippets.get(text, text)
    else:
        return snippets.get(text, text)
