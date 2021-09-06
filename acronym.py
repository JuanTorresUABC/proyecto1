print('Bienvenido')
palabra = str(input('Ingrese su palabra: '))
palabra_list = palabra.split()
acron=" "

for i in palabra_list:
    acron = acron+str(i[0].upper())
print('Su acronimo es: '+acron)