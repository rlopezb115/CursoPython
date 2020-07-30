# -*- coding: cp1252 -*-
# Este es un comentario y no se imprime

# #####################################################
# ################### Variables #######################
# #####################################################

# ¿Que es un variable? Es un espacio en memoria y tiene asignado un valor
# Esto quiere decir que ha definido una variable
userName = "Mi nombre de usuario es admin"
print(userName)

# si intento usar una variable que no esta definida genera un error.
# print(password)

# Asignacion multiple
userName, edad = 'admin', 60
print(userName)
print(edad)


# #####################################################
# ################### Números #########################
# #####################################################

# Una division siempre devuelve un dato de tipo coma flotante
# El signo =, se utiliza para asignar un valor a una variable
# En este ejemplo la 
resultado = 17 / 5
print("Resultado de 17 / 5 = ", resultado)

# División, descartar la parte fraccional
resultado = 17 // 5
print("Resultado de 17 // 5 = ", resultado)

# Obtener el resto de la división
resultado = 17 % 5
print("Resultado de 17 % 5 = ", resultado)

# Una multiplicación se resuelve antes que la suma
resultado = 10 * 5 + 5
print("Resultado de 10 * 5 + 5 = ", resultado)

# Calcular Potencias
resultado = 2 ** 2
print("Resultado de 2 ** 2 = ", resultado)

resultado = 2 ** 7
print("Resultado de 2 ** 7 = ", resultado)

# Soporte completo para punto flotante
# Si realizas una operacion de entero con punto flotante,  
# automaticamente el entero se convierte a punto flotante
resultado = 2 * 5.5 + 10
print("Resultado: 2 * 5.5 + 10 = ", resultado)

# #####################################################
# ################### Cadenas #########################
# #####################################################

# Se puede utilizar comillas dobles y simples
texto = "Utilizando comillas dobles"
print(texto)

texto = 'Utilizando comillas simples'
print(texto)

texto = "Utilizando comillas 'simples' dentro de comillas dobles"
print(texto)

texto = 'Utilizando comillas "dobles" dentro de comillas simples'
print(texto)

# Escapar: mostrar caracteres especiales utilizando una barra invertida
texto = "Utilizando comillas \"dobles\" dentro de comillas dobles"
print(texto)

texto = 'Utilizando comillas \'simples\' dentro de comillas simples'
print(texto)

# Evitar que caracteres precesidos por la barra invertida \
# sean interpretados como especiales
texto = r'Utilizando comillas \'simples\' dentro de comillas simples'
print(texto)

# Cadenas multilinea
texto = """
Este es un texto multilinea,
esta utilizando comillas dobles
y puedo utilizar comillas 'simples'
...
"""
print(texto)

texto = '''
Este es un texto multilinea,
esta utilizando comillas simples
y puedo utilizar comillas "dobles"
...
'''
print(texto)

# Repetir una cadena
texto = 3 * "Hola "
print(texto)

texto = texto * 2
print(texto)

# Concatenar variable con literal
texto = texto + "Mundo!!!"
print(texto)

# Concatenar solo literales
texto = ("Esta forma de concatena es util para cuando" 
        " quiera dividir cadenas largas"
        " solo funciona con literales y no con variables ni expresiones")
print(texto)

# texto2 = "texto2 es otra variable "
# texto = texto2 "Esta forma de concatenar no funciona con varibles"
# print(texto)

## texto = (3 * "Esto es una expresión ") "Esta forma de concatenar no funciona con expresiones."
## print(texto)

# Las cadenas se pueden indexar (subindices)
# el primer carácter de la cadena tiene el índice 0
texto = "Planeta"
print(texto[0])
print(texto[1])
print(texto[-2])
# Comienza a contar del lado derecho
print(texto[0:2])
print(texto[2:7])
print(texto[:2])
print(texto[2:])

# Esto mandara error, solo es de lectura
# texto[0] = "c"
# print(texto)

# Retornar longitud de una cadena
print(len(texto))

# #####################################################
# ################### Listas ##########################
# #####################################################

# Puede agrupar valores de diferentes tipos, 
# normalmente almacena valores del mismo tipo
# Se pueden indexar
edades = [18,19,20,21,25]
print(edades)
print(edades[:])
print(edades[0])
print(edades[-1])

edades = edades + [30,31,32,33,34,35]
print(edades[:])
# Una cadena es inmutable, quiere decir que no se puede modificar cuando nos colocamos en un indice
# Una lista es mutable, cuando no coloquemos en un indice si es posible modificar el valor
edades[0] = 100
print(edades[:])

# Utilizando el metodo append(), agregar elementos al final de la lista
edades.append(200 ** 2)
print(edades[:])
edades.append(201 ** 2)
print(edades[:])

# Remplazar valores
edades[2:5] = [100, 101, 102]
print(edades[:])

# Remover elementos
edades[5:7] = []
print(edades[:])

# Vaciar toda la lista
edades[:] = []
print(edades[:])

# La funcion len() sirve para contar la cantidad de elemento que contiene la lista
edades[:] = [2020,2021]
print(len(edades))