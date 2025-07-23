# Nuestro código tiene que ser capaz de:
# * Crear contraseñas al azar
# * Guardar las contraseñas
# * Mostrar las contraseñas guardadas
# * Borrar contraseñas (cuenta y su contraseña)

# "Para lograr esto podriamos pedir los siguientes valores:
# * Plataforma: Sitio web, app o similar del cual sera guardada nuestra contraseña y usuario. facebook.com por ejemplo
# * Nombre de cuenta/usuario: El nombre de nuestro usuario ya sea cuenta o nombre simple. MarckZuckerberg12
# * Contraseña: Esta sera generada por la plataforma asi que no la pediremos mas que la longitud que tendra esta.
# 15 =  bzar3idf97s6ad2

#Importación de la libreria de "secrets" en nuestro proyecto
#Nos servira para poder hacer aleatorias y mas seguras nuestras contraseñas
import secrets
# Creamos una variable en la cual guardaremos y le diremos al programa que caracteres usara
# para crear nuestras contraseñas, estrictamente lo que le indiquemos, ningun otro
baul_de_caracteres = 'abcdfghijklmnopqrstuvwxyz0123456789'

# Me va a permitir elegir un valor aleatorio de una secuencia (lista, cadena de texto)
#caracter_aleatorio = secrets.choice(baul_de_caracteres)
#print(caracter_aleatorio)


# De ciclos (while/for)

# Quiero que agarres la variable I y le des 8 vueltas
# Variable de control

# Esta función nos ayudará a crear contraseñas de diferente longitud
def crear_password(caracteres_, longitud_):
    password_final = ''

    for i in range(longitud):
        caracter_aleatorio = secrets.choice(caracteres_)

        password_final += caracter_aleatorio

    print(password_final)

print('Bienvenido a nuestro cajón de contraseñas =D \n\rElige una acción a realizar por favor: ')
#Nota: El \n\r es un salto de línea, osea un espacio/enter
while True:
    print('1. Crear una nueva cuenta')
    print('2. Ver listado de cuentas')
    print('3. Borrar una cuenta')
    print('0. Salir del programa')

    opcion = int(input('Selecciona la opción: '))

    if opcion == 0:
        print('Nos vemos a la siguiente ;)')
        break

    elif opcion == 1:

        longitud = int(input('Dame la longitud de la contraseña: '))
        crear_password(baul_de_caracteres, longitud)





