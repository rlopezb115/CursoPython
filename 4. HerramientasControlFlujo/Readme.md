# Herramientas de Control de Flujo

## Sentencia IF

## Sentencia __for__
Itera sobre los items de cualquier secuencia en el orden que aparecen.  
__¿Que es una secuencia?__ Es una lista o una cadena de texto.

Si ya tienes experiencia programando en otros lenguajes como Java, C o C# te daras cuenta que la sentencia __for__ difiere un poco en python.

En otros lenguajes como los antes mencionados, utilizan las expresiones siguientes:

* Inicialización de variable.
* Condición para salir del bucle.
* Incremento de la variable contador.

    for (int contador = 1; contador <= 10; contador++)

En python la sentencia __for__ tiene la sintaxis siguiente:

![Sentencia for simple y anidado](/././assets/images/4-HerramientasControlFlujo/Sentencia_for_simple_anidado.PNG)

Como se muestra en la imagen anterior una sentencia for puede estar dentro del boque de intrucciones de otro for, a esto se le llama bucles anidados y puede tener cualquier nivel de anidamiento

## Función _range()_

Puede hacer uso de esta función en los siguientes casos:
1. Iterar sobre una secuencia de números, el valor final nunca es parte de la secuencia;  
   es posible hacer que el rango empiece con otro número y especificar un incremento diferente
2. Iterar sobre los indices de una secuencia, combinar range y len.