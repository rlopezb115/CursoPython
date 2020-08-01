# Lista de Colores
lista_colores = ['blanco', 'amarillo', 'verde']
print(lista_colores)

# append: agrega un nuevo item al final de una lista.
lista_colores.append('rojo')
print(lista_colores)

# Equivalente de la función append:
lista_colores[len(lista_colores):]  = ['marron']
print(lista_colores)

lista_colores_segundo = ['gris', 'negro']
lista_colores_tercero = ['cafe', 'morado']
# extend: extiende la lista agregandole todos los items del iterable
lista_colores.extend(lista_colores_segundo)
print(lista_colores)

# Equivalente de la función extend
lista_colores[len(lista_colores):] = lista_colores_tercero
print(lista_colores)

# insert: es una función que inserta un item en una posición indicada.
lista_colores.insert(0, 'rosa')
print(lista_colores)