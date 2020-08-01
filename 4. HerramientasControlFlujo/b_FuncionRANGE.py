print('Inicio...')

print('\nSecuencia de números, básico')
# único parámetro, indica el final y no es parte de la secuencia.
for num in range(10):
    print('Número: ', num)

print('\nSecuencia de número, empieza con otro rango.')
# Primer parámetro indica el comienzo del rango.
# Segundo parámetro indica el final y no es parte de la secuencia.
for  num in range(1, 10):
    print('Número: ', num)

print('\nSecuencia de número, empieza con otro valor en rango e incremento.')
# Primer parámetro indica el comienzo del rango.
# Segundo parámetro indica el final y no es parte de la secuencia.
# Tercer parametro, indica el incremento
for  num in range(1, 10, 2):
    print('Número: ', num)

print('\nSecuencia de número, con valores negativos')
for num in range(10, -10, -2):
    print('Número: ', num)

print('\nIndice de una Secuencia, combinando range() y len()')
colores = ['amarillo', 'azul', 'rojo', 'verde', 'negro', 'morado']
for indice in range(len(colores)):
    print(indice, colores[indice])

print(sum(range(0, 10, 2)))
print(list(range(0, 10, 2)))
print('\n...final')