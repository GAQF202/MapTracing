class Rute(object): #ARISTAS

    def __init__(self):
        self.nombre = ""
        self.peso = ""
        self.inicio = ""
        self.fin = ""
        self.marca = ""
        self.elim =""

    def get(self):
        return self.nombre, self.inicio, self.fin, self.peso
    def get_edge(self):
        return self.inicio.lower(), self.fin.lower(), float(self.peso)
    def get_marca(self):
        return self.marca
    def get_elim(self):
        return self.elim



class Estation(object): #VERTICES

    def __init__(self):
        self.nombre = ""
        self.estado = ""
        self.color = ""
        self.posicion = 0

    def get(self):
        return self.nombre, self.estado, self.color, self.posicion


class Map(object):
    def __init__(self):
        self.nombre = ""
    def get(self):
        return self.nombre