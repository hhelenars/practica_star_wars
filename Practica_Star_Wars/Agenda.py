import pandas as pd
from LadoOscuro import LadoOscuro
from Fuerza import Fuerza

class Agenda:
    def __init__(self):
        self.__listausuariosensiblealafuerza = list()

    def __usuario_exixtente(self, usuariosensiblealafuerza):
        for usuario in self.__listausuariosensiblealafuerza:
            if usuario.nombre == usuariosensiblealafuerza.nombre and usuario.__class__.__name__ == usuariosensiblealafuerza.__class__.__name__:
                return True, usuario
        return False, None

    def __pasar_lista_dataframe (self):
        listadiccionario = [usuario.to_dict() for usuario in self.__listausuariosensiblealafuerza]
        return pd.DataFrame(listadiccionario)
    def __pasar_lista_dataframe_favoritos (self):
        listadiccionario = [usuario.to_dict_favoritos() for usuario in self.__listausuariosensiblealafuerza]
        return pd.DataFrame(listadiccionario)

    def anadir_usuario(self, usuariosensiblealafuerza):
        error, _ = self.__usuario_exixtente(usuariosensiblealafuerza)
        if error:
            return f"El usuario {usuariosensiblealafuerza.nombre} ya existe dentro del bando"
        else:
            self.__listausuariosensiblealafuerza.append(usuariosensiblealafuerza)
            return f"Usuario {usuariosensiblealafuerza.nombre} añadido con exito"

    def modificar_usuario(self, usuariosensiblealafuerza,modificacion):
        error, usuarioexixtente = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"
        else:
            indice = self.__listausuariosensiblealafuerza.index(usuarioexixtente)
            self.__listausuariosensiblealafuerza[indice] = modificacion
            return f"Usuario  {usuarioexixtente.nombre} modificado con exito"

    def consultar(self, usuariosensiblealafuerza):
        error, usuarioexixtente = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"
        else:
            return pd.Series(usuarioexixtente.to_dict())

    def eliminar(self, usuariosensiblealafuerza):
        error, usuarioexixtente = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"
        else:
            self.__listausuariosensiblealafuerza.remove(usuarioexixtente)
            return f"Usuario {usuarioexixtente.nombre} eliminado con exito"

    def mostrar_todos(self):
        return self.__pasar_lista_dataframe()

    def buscar(self, query):
        df = self.mostrar_todos()
        df = df.query(query)
        return df

    def cambiar_bando(self, usuariosensiblealafuerza, bando):
        error, usuarioexixtente = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"
        else:
            posicion = self.__listausuariosensiblealafuerza.index(usuarioexixtente)
            if bando == 1:
                self.__listausuariosensiblealafuerza [posicion] = Fuerza(usuarioexixtente.nombre, usuarioexixtente.rango, usuarioexixtente.nivelpoder)
            elif bando == 2:
                self.__listausuariosensiblealafuerza[posicion] = LadoOscuro(usuarioexixtente.nombre, usuarioexixtente.rango, usuarioexixtente.nivelpoder)

            return f"Usuario {usuarioexixtente.nombre} ha cambiado de bando con exito"

    def crear_excel_contactos(self):
        #try:
            df = self.__pasar_lista_dataframe()
            df.to_excel("Agenda_de_contactos.xlsx",  index=False)
            return "Agenda_de_contactos.xlsx creado con exito"
        #except:
            return "No se ha podido crear Agenda_de_contactos.xlsx"


    def anadir_favoritos(self, usuariosensiblealafuerza):
        error, usuariosensiblealafuerza = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"
        else:
            if not usuariosensiblealafuerza.favoritos:
                usuariosensiblealafuerza.favoritos = True
                return f"El usuario {usuariosensiblealafuerza.nombre} añadido a favoritos con exito"
            return f"El usuario {usuariosensiblealafuerza.nombre} ya estaba en favoritos"

    def eliminar_favoritos(self, usuariosensiblealafuerza):
        error, usuariosensiblealafuerza = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"
        else:
            if usuariosensiblealafuerza.favoritos:
                usuariosensiblealafuerza.favoritos = False
                return f"El usuario {usuariosensiblealafuerza.nombre} eliminado a favoritos con exito"
            return f"El usuario {usuariosensiblealafuerza.nombre} no estaba en favoritos"

    def mostrar_favoritos(self):
        dffavoritos = self.__pasar_lista_dataframe_favoritos()
        dffavoritos = dffavoritos[dffavoritos['Favoritos'] == True]
        return dffavoritos.drop(columns=['Favoritos'])



