import pandas as pd
from LadoOscuro import LadoOscuro
from Fuerza import Fuerza

class Agenda:
    def __init__(self):
        self.__listafuerza = list()
        self.__listaladooscuro = list()
        self.__limite_por_bando = 50

    def __obtener_lista_por_nombre_bando(self, nombre_bando):
        if nombre_bando == "Fuerza":
            return self.__listafuerza
        if nombre_bando == "LadoOscuro":
            return self.__listaladooscuro
        return None

    def __obtener_lista_por_usuario(self, usuariosensiblealafuerza):
        return self.__obtener_lista_por_nombre_bando(usuariosensiblealafuerza.__class__.__name__)

    def __todos_los_usuarios(self):
        return self.__listafuerza + self.__listaladooscuro

    def __usuario_exixtente(self, usuariosensiblealafuerza):
        listabando = self.__obtener_lista_por_usuario(usuariosensiblealafuerza)
        if listabando is None:
            return False, None

        for usuario in listabando:
            if usuario.nombre == usuariosensiblealafuerza.nombre:
                return True, usuario
        return False, None

    def __pasar_lista_dataframe(self):
        listadiccionario = [usuario.to_dict() for usuario in self.__todos_los_usuarios()]
        return pd.DataFrame(listadiccionario)

    def __pasar_lista_dataframe_favoritos(self):
        listadiccionario = [usuario.to_dict_favoritos() for usuario in self.__todos_los_usuarios()]
        return pd.DataFrame(listadiccionario)

    def __limite_bando(self, nombre_bando):
        listabando = self.__obtener_lista_por_nombre_bando(nombre_bando)
        if listabando is None:
            numerobando = 0
        else:
            numerobando = len(listabando)
        if numerobando < self.__limite_por_bando:
            return True
        return False

    def anadir_usuario(self, usuariosensiblealafuerza):
        error, _ = self.__usuario_exixtente(usuariosensiblealafuerza)
        if error:
            return f"El usuario {usuariosensiblealafuerza.nombre} ya existe dentro del bando"
        limitebando = self.__limite_bando(usuariosensiblealafuerza.__class__.__name__)
        if not limitebando:
            return f"No se puede añadir un nuevo usuario a ese bando, supera el límite permitido"

        listabando = self.__obtener_lista_por_usuario(usuariosensiblealafuerza)
        listabando.append(usuariosensiblealafuerza)
        return f"Usuario {usuariosensiblealafuerza.nombre} añadido con exito"

    def modificar_usuario(self, usuariosensiblealafuerza,modificacion):
        error, usuarioexixtente = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"

        listabando = self.__obtener_lista_por_usuario(usuariosensiblealafuerza)
        indice = listabando.index(usuarioexixtente)
        listabando[indice] = modificacion
        return f"Usuario  {usuarioexixtente.nombre} modificado con exito"

    def consultar(self, usuariosensiblealafuerza):
        error, usuarioexixtente = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"
        return pd.Series(usuarioexixtente.to_dict())

    def eliminar(self, usuariosensiblealafuerza):
        error, usuarioexixtente = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"

        listabando = self.__obtener_lista_por_usuario(usuariosensiblealafuerza)
        listabando.remove(usuarioexixtente)
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

        if bando == 1:
            if usuarioexixtente.__class__.__name__ == "Fuerza":
                return f"El usuario {usuarioexixtente.nombre} ya pertenece al bando Fuerza"
            limitebando = self.__limite_bando("Fuerza")
            if not limitebando:
                return f"No se puede cambiar de bando al usuario, supera el límite permitido"
            nuevousuario = Fuerza(usuarioexixtente.nombre, usuarioexixtente.rango, usuarioexixtente.nivelpoder)
            nuevousuario.favoritos = usuarioexixtente.favoritos
            self.__listaladooscuro.remove(usuarioexixtente)
            self.__listafuerza.append(nuevousuario)

        elif bando == 2:
            if usuarioexixtente.__class__.__name__ == "LadoOscuro":
                return f"El usuario {usuarioexixtente.nombre} ya pertenece al bando LadoOscuro"
            limitebando = self.__limite_bando("LadoOscuro")
            if not limitebando:
                return f"No se puede cambiar de bando al usuario, supera el límite permitido"
            nuevousuario = LadoOscuro(usuarioexixtente.nombre, usuarioexixtente.rango, usuarioexixtente.nivelpoder)
            nuevousuario.favoritos = usuarioexixtente.favoritos
            self.__listafuerza.remove(usuarioexixtente)
            self.__listaladooscuro.append(nuevousuario)
        else:
            return "El bando seleccionado no es válido"
        return f"Usuario {usuarioexixtente.nombre} ha cambiado de bando con exito"

    def crear_excel_contactos(self):
        try:
            df = self.__pasar_lista_dataframe()
            df.to_excel("Agenda_de_contactos.xlsx", index=False)
            return "Agenda_de_contactos.xlsx creado con exito"
        except Exception:
            return "No se ha podido crear Agenda_de_contactos.xlsx"


    def anadir_favoritos(self, usuariosensiblealafuerza):
        error, usuariosensiblealafuerza = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"

        if not usuariosensiblealafuerza.favoritos:
            usuariosensiblealafuerza.favoritos = True
            return f"El usuario {usuariosensiblealafuerza.nombre} añadido a favoritos con exito"
        return f"El usuario {usuariosensiblealafuerza.nombre} ya estaba en favoritos"

    def eliminar_favoritos(self, usuariosensiblealafuerza):
        error, usuariosensiblealafuerza = self.__usuario_exixtente(usuariosensiblealafuerza)
        if not error:
            return f"El usuario {usuariosensiblealafuerza.nombre} no existe"

        if usuariosensiblealafuerza.favoritos:
            usuariosensiblealafuerza.favoritos = False
            return f"El usuario {usuariosensiblealafuerza.nombre} eliminado a favoritos con exito"
        return f"El usuario {usuariosensiblealafuerza.nombre} no estaba en favoritos"

    def mostrar_favoritos(self):
        dffavoritos = self.__pasar_lista_dataframe_favoritos()
        if dffavoritos.empty:
            return dffavoritos
        dffavoritos = dffavoritos[dffavoritos['Favoritos'] == True]
        return dffavoritos.drop(columns=['Favoritos'])



