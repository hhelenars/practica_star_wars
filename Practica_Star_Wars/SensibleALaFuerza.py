import pandas as pd


class SensibleALaFuerza:

    def __init__(self, nombre, rango, nivelpoder, movil):
        self.__id = None
        self.__nombre = nombre
        self.__rango = rango
        self.__nivelpoder = nivelpoder
        self.__favoritos = False
        self.__movil = movil
        self.__maestros_ids = list()
        self.__alumnos_ids = list()

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

    @property
    def movil(self):
        return self.__movil

    @movil.setter
    def movil(self, movil):
        self.__movil = movil

    @property
    def id(self):
        return self.__id

    def asignar_id_agenda(self, id):
        self.__id = id

    @property
    def maestros_ids(self):
        return self.__maestros_ids

    @maestros_ids.setter
    def maestros_ids(self, maestros_ids):
        self.__maestros_ids = maestros_ids

    @property
    def alumnos_ids(self):
        return self.__alumnos_ids

    @alumnos_ids.setter
    def alumnos_ids(self, alumnos_ids):
        self.__alumnos_ids = alumnos_ids


    def to_dict (self):
        return {'Nombre': self.nombre,
                'Bando': self.__class__.__name__,
                'Rango': self.rango,
                'Nivel de poder': self.nivelpoder,
                'Móvil': self.movil}

    def to_dict_favoritos (self):
        return {'Nombre': self.nombre,
                'Bando': self.__class__.__name__,
                'Rango': self.rango,
                'Nivel de poder': self.nivelpoder,
                'Móvil': self.movil,
                'Favoritos': self.favoritos}

    def __str__(self):
        return (f"Nombre: {self.__nombre}\n"
                f"Bando: {self.__class__.__name__}\n"
                f"Rango: {self.__rango}\n"
                 f"Nivel de poder: {self.__nivelpoder}\n"
                f"Móvil: {self.__movil}")