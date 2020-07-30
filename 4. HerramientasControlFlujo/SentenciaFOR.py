lista_nombres = ['José Antonio', 'Ricardo', 'Alma Patricia', 'Marcos']

print('La lista tiene una longitud de: ', len(lista_nombres))

print('Simple:')
for nombre in lista_nombres:
    print('Nombre: ', nombre)
    print('Longitud: ', len(nombre));

print('\nAnidado:')
for nombre in lista_nombres:
    print('Nombre: ', nombre)
    print('Longitud: ', len(nombre));
    for letra in nombre:
        print('Letra: ', letra);

print('Fin de la iteración!!!')