lista_nombres = ['José Antonio', 'Ricardo', 'Alma Patricia', 'Marcos']

print('La lista tiene una longitud de: ', len(lista_nombres))

print('Simple:')
for nombre in lista_nombres:
    print('Nombre: ', nombre)
    print('Longitud: ', len(nombre))

print('\nAnidado:')
for nombre in lista_nombres:
    print('Nombre: ', nombre)
    print('Longitud: ', len(nombre))
    for letra in nombre:
        print('Letra: ', letra)

# La función enumerate(), obtiene el indice de posición y valor correspondiente 
# de una secuencia que se esta iterando.
for key, value in enumerate(['abc', 'def', 'ghi']):
    print(key, value)

print('##### Copia de una colección #####')
lista_alumnos = {'nombre':'Ricardo', 'edad': 25, 'sexo': 'Masculino'}
lista_registrar = {}

# El método items() en un diccionario obtiene al mismo tiempo clave y valor correspondiente
for clave, value in lista_alumnos.copy().items():
    if clave == 'edad' : del lista_alumnos[clave]
    print(clave, ' : ', value)

for clave, value in lista_alumnos.items():
    if clave == 'nombre' : lista_registrar[clave] = value
    # print(clave, ' : ', value)

print(lista_alumnos)
print(lista_registrar)
print('Fin de la iteración!!!')