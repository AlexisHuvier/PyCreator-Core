import __main__
import sys


def get_completion(text):
    namespace = {**__main__.__builtins__.__dict__, **__main__.__dict__, **sys.modules}
    bigl = eval("dir()", namespace)
    bigl.sort()

    liste = [x for x in bigl if x.startswith(text)]
    return liste + [x for x in bigl if text in x and x not in liste]