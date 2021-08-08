import sqlite3
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Creación de la base de datos
conexion = sqlite3.connect("bd1.db")

try:
    # Se intenta crear una tabla
    conexion.execute(
        "create table users(username varchar(25) 		primary key, password varchar(25), level integer)")
    conexion.execute("INSERT INTO users VALUES('root','root',3)")
    conexion.commit()
    print("Se creo la tabla de usuarios")
except sqlite3.OperationalError:
    # Si ya está creada
    print("La tabla de usuarios ya existe")


def usuarios():
    cur = conexion.cursor()
    cur.execute("SELECT * FROM users")
    return cur.fetchall()


def crear_usuario():
    print("Crear usuario")
    usr = input("Ingrese nombre de usuario: ")
    # clear()
    if existe_usuario(usr):
        print("ERROR: El nombre", usr, "ya está siendo utilizado")
    else:
        pwd = input("Ingrese contraseña: ")
        lvl = input("Ingrese nivel (1,2 o 3): ")
        conexion.execute("INSERT INTO users VALUES('" + usr + "','" + pwd + "'," + lvl + ")")
        conexion.commit()
        print("Usuario", usr, "creado correctamente")


def eliminar_usuario():
    print("Eliminar usuario")
    usr = input("Ingrese nombre de usuario: ")
    # clear()
    if existe_usuario(usr):
        conexion.execute("DELETE FROM users WHERE username = '" + usr + "'")
        conexion.commit()
        print("Usuario", usr, "eliminado correctamente")
    else:
        print("El usuario", usr, "no existe")


def existe_usuario(usr):
    cur = conexion.cursor()
    cur.execute("SELECT * FROM users WHERE username = '" + usr + "'")
    return cur.fetchall()


# Menu
# clear()
salir = False
while not salir:
    print("Programa Épico-Fantástico")
    print("1-Ver Usuarios\n2-Crear Usuario\n3-Eliminar Usuario\n4-Salir")
    opcion = input("Opción: ")
    # clear()
    if opcion == "1":
        print("Usuarios en el sistema: ")
        print(usuarios(), "\n")
    elif opcion == "2":
        crear_usuario()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        salir = True
    else:
        print("ERROR: Opción incorrecta")

# Antes de salir del prog
if not usuarios():
    conexion.execute("INSERT INTO users VALUES('root','root',3)")
    conexion.commit()

conexion.close()
