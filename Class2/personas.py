from operator import truediv


class Persona:
    def __init__(self,nombre,edad):
        self.set_nombre(nombre)
        self.set_edad(edad)

    def set_edad(self,edad):
        if 0 <= edad <= 125:
            self.__edad= edad

    def get_edad(self):
        return self.__edad

    def set_nombre(self,nombre):
        if nombre!="":
            self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def print_persona(self):
        print("{} {}".format(self.get_nombre(),self.get_edad()))

    def es_mayor_de_edad(self):
        if(self.get_edad() >= 18):
            return True
        else:
            return False
        