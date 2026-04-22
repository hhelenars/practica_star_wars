import pandas as pd


class SensibleALaFuerza:

    def __init__(self, nombre, rango, nivelpoder):
        self.__nombre = nombre
        self.__rango = rango
        self.__nivelpoder = nivelpoder
        self.__favoritos = False



    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
         self.__nombre = nombre

    @property
    def rango(self):
        return self.__rango

    @rango.setter
    def rango(self, rango):
        self.__rango = rango

    @property
    def nivelpoder(self):
        return self.__nivelpoder

    @nivelpoder.setter
    def nivelpoder (self, nivelpoder):
        self.__nivelpoder  = nivelpoder

    @property
    def favoritos(self):
        return self.__favoritos

    @favoritos.setter
    def favoritos(self, favoritos):
        self.__favoritos = favoritos

    def to_dict (self):
        return {'Nombre': self.nombre,
                'Bando': self.__class__.__name__,
                'Rango': self.rango,
                'Nivel de poder': self.nivelpoder}

    def to_dict_favoritos (self):
        return {'Nombre': self.nombre,
                'Bando': self.__class__.__name__,
                'Rango': self.rango,
                'Nivel de poder': self.nivelpoder,
                'Favoritos': self.favoritos}

    def __str__(self):
        return (f"Nombre: {self.__nombre}\n"
                f"Bando: {self.__class__.__name__}\n"
                f"Rango: {self.__rango}\n"
                f"Nivel de poder: {self.__nivelpoder}")