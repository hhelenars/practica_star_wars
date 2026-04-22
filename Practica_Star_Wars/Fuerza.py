from SensibleALaFuerza import SensibleALaFuerza


class Fuerza(SensibleALaFuerza):

    def __init__(self, nombre, rango, nivelpoder, movil, istamaestros=None, listaalumnos=None):
        super().__init__(nombre, rango, nivelpoder, movil,istamaestros,listaalumnos)