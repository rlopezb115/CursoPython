# IF: se utiliza para la ejecucion condicional, 
# Quiere decir que evalua la expresion una por una
# hasta encontrar una que sea verdadera, 
# si todas las expresiones son falsas se ejecuta el bloque de else

# Puede tener cero, uno o más de bloque elif
# elif es una abreviatura de else if (si no si)
# else es opcional

resultado_operacion, cadena_multilinea = 0, ''
numero = 3

if numero == 10:
    cadena_multilinea = '''
Primer cadena multilinea,
esta cadena es un literal
...
    ''' '''
Segunda cadena multilinea,
esta cadena es un literal
    ''' '\nCumple la expresión de ser igual a 10.'
    resultado_operacion = (numero * 5 - 15) ** 5

elif numero > 10:

    cadena_multilinea = '''
Primer cadena multilinea,
esta cadena es un literal
...
    ''' '''
Segunda cadena multilinea,
esta cadena es un literal
    ''' '\nCumple la expresión de ser mayor a 10.'
    resultado_operacion = (numero * 2 + 5) ** 6

elif numero >= 5:

    cadena_multilinea = '''
Primer cadena multilinea,
esta cadena es un literal
...
    ''' '''
Segunda cadena multilinea,
esta cadena es un literal
    ''' '\nCumple la expresión de ser mayor e igual a 5 pero menor que 10.'
    resultado_operacion = (numero * 1 + 5) ** 2
else:
    cadena_multilinea = '''
Primer cadena multilinea,
esta cadena es un literal
...
    ''' '''
Segunda cadena multilinea,
esta cadena es un literal
    ''' '\nTodas las expresiones fueron falsas.'
    resultado_operacion = (numero * -1) ** 2

print(cadena_multilinea)
print(resultado_operacion)