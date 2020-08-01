# def, es una palabra reservada para crear una función

def sumar(a, b):
    ''' Esta funcíon se encarga de sumar dos números y calcular el iva '''
    a = (a + b) * .16
    return a

print(sumar(50, 50))