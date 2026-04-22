import sys
import pandas as pd
from colorama import Fore, Style, init
from Agenda import Agenda
from Fuerza import Fuerza
from LadoOscuro import LadoOscuro

init()

def pedir_instruccion():
    try:
        instruccion = int(input("INTRODUCE NUMERO DE LA INSTRUCCIÓN: "))
        return instruccion
    except ValueError:
        print(Fore.RED+ Style.BRIGHT + "Introduzca un numero" + Style.RESET_ALL)
        return pedir_instruccion()

def pedir_nombre():
    nombre = input("Ingrese el nombre: ").capitalize().strip()
    if nombre == "":
        print(Fore.RED+ Style.BRIGHT + "El nombre no puede estar vacio"+ Style.RESET_ALL)
        return pedir_nombre()
    return nombre

def pedir_nivelpoder():
    try:
        nivelpoder = int(input("Ingrese el nivel de poder (max 1000): "))
        if nivelpoder < 0:
            print(Fore.RED+ Style.BRIGHT + "El nivel de poder no puede ser menor que 0" + Style.RESET_ALL)
            return pedir_nivelpoder()
        elif nivelpoder > 1000:
            print(Fore.RED+ Style.BRIGHT + "El nivel de poder no puede ser mayor que 1000" + Style.RESET_ALL)
            return pedir_nivelpoder()
    except ValueError:
        print(Fore.RED+ Style.BRIGHT + "Introduzca un número"+ Style.RESET_ALL)
        return pedir_nivelpoder()
    return nivelpoder

def pedir_rango(rangos):
    print("Seleccione el rango")
    for clave in rangos.keys():
        print(f"{clave}.{rangos[clave]}")

    rango_numero = pedir_instruccion()
    if 1 > rango_numero or rango_numero > len(rangos):
        print(Fore.RED+ Style.BRIGHT + "El rango no es correcto"+ Style.RESET_ALL)
        return pedir_rango(rangos)

    return rangos[rango_numero]

def pedir_rango_fuerza():
    return pedir_rango({1:"Padawan", 2:"Caballero", 3:"Maestro"})

def pedir_rango_ladooscuro():
    return pedir_rango({1:"Aprendiz", 2:"Darth", 3:"Lord"})

def pedir_bando():
    print("Seleccione el bando")
    print("1.Fuerza")
    print("2.Lado Oscuro")
    bando = pedir_instruccion()
    if bando == 1 or bando == 2:
        return bando
    else:
        print(Fore.RED+ Style.BRIGHT + "El número del bando no es correcto" + Style.RESET_ALL)
        return pedir_bando()


def crear_sesiblealafuerza():
    print("-------------------------------------------")
    print("CREAR USUARIO")
    nombre = pedir_nombre()
    nivelpoder = pedir_nivelpoder()
    bando = pedir_bando()
    if bando == 1:
        rango = pedir_rango_fuerza()
        return Fuerza(nombre, rango, nivelpoder)
    else:
        rango = pedir_rango_ladooscuro()
        return LadoOscuro(nombre, rango, nivelpoder)


def indentificar_usuario():
    print("-------------------------------------------")
    print("IDENTIFICAR USUARIO")
    nombre = pedir_nombre()
    bando = pedir_bando()
    if bando == 1:
        return Fuerza(nombre, None, None)
    else:
        return LadoOscuro(nombre,None, None)


def modificar_usuario(usuarioseleccionado):
    print("-------------------------------------------")
    print("MODIFICAR USUARIO")
    print("¿Que desea modificar?")
    print("1.Nombre")
    print("2.Rango")
    print("3.Nivel de poder")
    cambiar = list(input("Introduce los números separados por comas (1,2,3) en caso de que desee modificar diferentes cosas: ").split(","))
    for numero in cambiar:
        try:
            numero_correcto = int(numero)
            if numero_correcto not in [1,2,3]:
                print("El numero introducido no es valido")
                return modificar_usuario(usuarioseleccionado)

        except ValueError:
            print("Introduzca números entre [1-3]")
            return modificar_usuario(usuarioseleccionado)

    if '1' in cambiar:
        nombrenuevo = pedir_nombre()
        usuarioseleccionado.nombre = nombrenuevo
    if '2' in cambiar:
        if usuarioseleccionado.__class__.__name__ == "Fuerza":
            rango = pedir_rango_fuerza()
        else :
            rango = pedir_rango_ladooscuro()
        usuarioseleccionado.rango = rango
    if '3' in cambiar:
        nivelpoder = pedir_nivelpoder()
        usuarioseleccionado.nivelpoder = nivelpoder

    return usuarioseleccionado

def buscar_usuario():
    print("-------------------------------------------")
    print("BUSCAR POR: NOMBRE, RANGO Y NIVEL DE PODER")
    print("¿Por qué desea buscar?")
    print("1.Nombre")
    print("2.Rango")
    print("3.Nivel de poder")
    busqueda = list(input("Introduce los números separados por comas (1,2,3) en caso de que desee buscar por diferentes cosas: ").split(","))
    for numero in busqueda:
        try:
            numero_correcto = int(numero)
            if numero_correcto not in [1, 2, 3]:
                print("El numero introducido no es valido")
                return buscar_usuario()

        except ValueError:
            print("Introduzca números entre [1-3]")
            return buscar_usuario()

    listabusqueda = list()
    if '1' in busqueda:
        nombrebusqueda = pedir_nombre()
        listabusqueda.append(f"Nombre=='{nombrebusqueda}'")

    if '2' in busqueda:
        rangobusqueda = pedir_rango({1:"Padawan", 2:"Caballero", 3:"Maestro", 4:"Aprendiz", 5:"Darth", 6:"Lord"})
        listabusqueda.append(f"Rango=='{rangobusqueda}'")

    if '3' in busqueda:
        nivelpoder = pedir_nivelpoder()
        listabusqueda.append(f"`Nivel de poder`=={nivelpoder}")

    query = " and ".join(listabusqueda)
    return query


def menu_agenda():
    print("-------------------------------------------")
    print("MENU")
    print("1. Añadir un nuevo sith/jedi a la agenda.")
    print("2. Modificar un sith/jedi existente.")
    print("3. Consultar los datos de un sith/jedi.")
    print("4. Eliminar un sith/jedi.")
    print("5. Buscar por nombre, por rango o por nivel de poder.")
    print("6. Mostrar toda la agenda")
    print("7. Cambiara de lado a un sith/jedi.")
    print("8. Favoritos")
    print("9. Crear un excel de contactos")
    print("10. Salir")
    print("-------------------------------------------")
    instruccion = pedir_instruccion()
    while instruccion < 1 or instruccion > 10:
        print("El numero es incorrecto")
        instruccion = pedir_instruccion()
    return instruccion

def menu_favoritos():
    print("-------------------------------------------")
    print("MENU FAVORITOS")
    print("1. Añadir un nuevo sith/jedi favorito.")
    print("2. Eliminar un sith/jedi de favoritos.")
    print("3. Mostar lista de favoritos.")
    print("4. Atrás")
    print("-------------------------------------------")
    return pedir_instruccion()

#####################################################################

agenda = Agenda()

while True:

    instruccion = menu_agenda()

    match instruccion:
        case 1:
            usuario = crear_sesiblealafuerza()
            if usuario is not None:
                print(Fore.YELLOW + Style.BRIGHT + agenda.anadir_usuario(usuario) + Style.RESET_ALL)
        case 2:
            usuario = indentificar_usuario()
            modificacion = modificar_usuario(usuario)
            print(Fore.YELLOW + Style.BRIGHT + agenda.modificar_usuario(usuario,modificacion) + Style.RESET_ALL)
        case 3:
            usuario = indentificar_usuario()
            print("-------------------------------------------")
            print("DATOS DEL USUARIO")
            print(Fore.YELLOW + Style.BRIGHT)
            print(agenda.consultar(usuario))
            print(Style.RESET_ALL)

        case 4:
            usuario = indentificar_usuario()
            print("-------------------------------------------")
            print("ELEMINAR USUARIO")
            print(Fore.YELLOW + Style.BRIGHT + agenda.eliminar(usuario) + Style.RESET_ALL)

        case 5:
            query = buscar_usuario()
            print(agenda.buscar(query))

        case 6:
            print("-------------------------------------------")
            print("AGENDA")
            print(Fore.YELLOW + Style.BRIGHT)
            print(agenda.mostrar_todos())
            print(Style.RESET_ALL)

        case 7:
            usuario = indentificar_usuario()
            print("-------------------------------------------")
            print("CAMBIAR DE BANDO")
            bando = pedir_bando()
            print(Fore.YELLOW + Style.BRIGHT + agenda.cambiar_bando(usuario, bando) + Style.RESET_ALL)


        case 8:
            instruccion_facorito = menu_favoritos()
            match instruccion_facorito:
                case 1:
                    usuario = indentificar_usuario()
                    print("-------------------------------------------")
                    print("AÑADIR USUARIO A FAVORITOS")
                    print(Fore.YELLOW + Style.BRIGHT + agenda.anadir_favoritos(usuario) + Style.RESET_ALL)
                case 2:
                    usuario = indentificar_usuario()
                    print("-------------------------------------------")
                    print("ELIMINAR USUARIO A FAVORITOS")
                    print(Fore.YELLOW + Style.BRIGHT + agenda.eliminar_favoritos(usuario) + Style.RESET_ALL)
                case 3:
                    print(Fore.YELLOW + Style.BRIGHT)
                    print(agenda.mostrar_favoritos())
                    print(Style.RESET_ALL)
        case 9:
            print("-------------------------------------------")
            print("CREAR UN EXCEL")
            print(Fore.YELLOW + Style.BRIGHT + agenda.crear_excel_contactos() + Style.RESET_ALL)

        case 10:
            print("QUE LA FUERZA TE ACOMPAÑE")
            sys.exit()

        case _ :
            print("El número es incorrecto")




