import random
print('Adivina adivinador\n')

number= random.randrange(1,50)
while True:
    try:
        jugador = int (input("Adivina un numero entre 1 y 50: "))
        break
    except ValueError:
        print("Solo puedes ingresar numeros, tu puedes crack")


while jugador != number:
    if jugador < number:
        print("Es un numero mas alto. Intenta de nuevo")

        while True:
            try:
                jugador = int (input("Adivina un numero entre 1 y 50: "))
                break
            except ValueError:
                print("Solo puedes ingresar numeros, tu puedes crack")
    else:
        print("Es un numero mas bajo. Intenta de nuevo")
        while True:
            try:
                jugador = int (input("Adivina un numero entre 1 y 50: "))
                break
            except ValueError:
                print("Solo puedes ingresar numeros, tu puedes crack")
            

print("Adivinaste el numero amiguito :)")