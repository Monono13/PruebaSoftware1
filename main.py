import getpass
import json
import os

#iniciar sesión
def iniciar_sesion(username=None, password=None):
    if username is None:
        username = input("Ingrese su nombre de usuario: ")
    if password is None:
        password = getpass.getpass("Ingrese su contraseña maestra: ")


    print("Inicio de sesión exitoso.")
    

#guardar credenciales
def guardar_credenciales(app_name=None, username=None, password=None):
    if app_name is None:
        app_name = input("Ingrese el nombre de la aplicación: ")
    if username is None:
        username = input("Ingrese su nombre de usuario para {}: ".format(app_name))
    if password is None:
        password = getpass.getpass("Ingrese su contraseña para {}: ".format(app_name))

    #archivo JSON para guardar las credenciales
    filename = "credenciales.json"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    #verificar si password fue guardada anteriormente
    if app_name in data:
        print("Ya se ha guardado una contraseña para esta aplicación.")
    else:
        data[app_name] = {"username": username, "password": password}
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Credenciales guardadas correctamente para {}.".format(app_name))

#main funcion
def main():
    print("Bienvenido a la aplicación de gestión de credenciales.")

    while True:

        print("LogIn: \n")
        iniciar_sesion()

        while True:

            print("Detectando Aplicacion... \n")
            guardar_credenciales()  

            print("¿Desea guardar otra contraseña? (y/n)")
            opcion = input()
            if opcion == "y":
                continue
            elif opcion == 'n':
                break
        
        print("LogIn Out... \n")
        break


if __name__ == "__main__":
    main()