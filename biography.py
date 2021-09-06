print('Bienvenido')

while True:
    try:
        nombre= input("Cual es tu nombre?\n")
        nombre.isalpha()
        break
    except ValueError:
        print("Solo puedes ingresar letras")
while True:
    try:
        fechaNac= input("Cual es tu fecha de nacimiento?\n")
        fechaNac.isspace()
        break
    except ValueError:
        print("Fecha invalida")
while True:
    try:
        direccion = input("Cual es tu direccion?\n")
        direccion.isspace()
        break
    except ValueError:
        print("Direccion invalida")
while True:
    try:
        goal= input("Cual es tu meta personal?\n")
        goal.isspace()
        break
    except ValueError:
        print("Error al ingresar tu meta")


print('\nNombre: '+ nombre)
print('Fecha de nacimiento: '+ fechaNac)
print('Direccion: '+ direccion)
print('Meta personal: '+ goal)