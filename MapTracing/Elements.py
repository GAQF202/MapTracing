class Rute(object):

    def __init__(self):
        self.nombre = ""
        self.peso = ""
        self.inicio = ""
        self.fin = ""

    def get(self):
        return self.nombre, self.inicio, self.fin, self.peso