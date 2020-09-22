class Rute(object):

    def __init__(self):
        self.nombre = ""
        self.peso = ""
        self.inicio = ""
        self.fin = ""

    def get(self):
        return self.nombre, self.inicio, self.fin, self.peso


class Estation(object):

    def __init__(self):
        self.nombre = ""
        self.estado = ""
        self.color = ""
    def get(self):
        return self.nombre, self.estado, self.color
