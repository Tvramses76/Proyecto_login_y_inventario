import json


import aplicacion

usuario = []

contrasena = []

datos = {}

lugar = 0
def menu():
    global lugar
    while True:
        print('\nBIENVENIDO AL SIMULADOR DE LOGIN')
        print('\n1. Registrar usuario')
        print('2. Iniciar sesión')
        print('3. Salir')

        lugar = int(input('\nSeleccione una opción: '))

        if lugar == 1:
            registrar_usuario()


        elif lugar == 2:
            iniciar_secion()

        elif lugar == 3:
            print('Saliste...')
            break




def cargar_datos():
    global datos, usuario, contrasena

    try:
        with open('json.json', 'r') as archivo:
            datos = json.load(archivo)
            usuario = list(datos.keys())
            contrasena = list(datos.values())

            return datos
    except (FileNotFoundError, json.JSONDecodeError, AttributeError):
        datos = {}

def guardar_datos():
    with open('json.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

cargar_datos()

def registrar_usuario():
    while True:
        print('\nREGISTRO DE USUARIO')
        persona = input('\nIngrese su nombre de usuario: ')

        for i in range(len(usuario)):
            if persona in datos:
                print('El usuario ya existe. inicia sesion.')
                return iniciar_secion()

        clave = input('Ingrese su contraseña: ')
        datos[persona] = clave
        usuario.append(persona)
        contrasena.append(clave)

        print('Usuario registrado con éxito. Vuelve iniciar sesion')
        break

def iniciar_secion():
    global lugar
    while True:
        print('\nINICIAR SESION')
        usuario_iniciar = input('\nIngrese su nombre de usuario: ')
        if usuario_iniciar in datos:
            print(f'Bienvenido {usuario_iniciar}')
        else:
            print('Usuario no encontrado')
            respuesta = input('\nDesea registrar un usuario? Si/No')
            if respuesta.lower() == 'si':
                return registrar_usuario()
            else:
                print('Regresando al menu...')
                return menu()



        pase = input('Ingrese su contraseña: ')
        if datos[usuario_iniciar] == pase:
            print('Has iniciado correctamente')
            app = 0
            while app == 0:
                if datos[usuario_iniciar] == pase:
                    aplicacion.pagina()
                    break
            break



        else:
            print('Contraseña incorrecta, vuelvelo intentar')
            return iniciar_secion()



menu()
guardar_datos()

