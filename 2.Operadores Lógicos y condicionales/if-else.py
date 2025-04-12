"""
Ya vimos como funciona el condicional if, pero que pasa cuando queremos 
que cuando no se cumpla una accion muestre otro bloque de codigo,
para esto existe else, que se ejecuta al momento en que no se cumple una 
condicion en el if, es necesario el uso de un if para que funcione y su sintaxis es.

if (condicion):
    linea_de_codigo_que_se_ejecutara
else:
    linea_de_codigo_que_se_ejecutara_si_no_se_cumple_el_if

Ahora lo probaremos
"""

a = 5
b = 1

if (a < b):
    print(a," es menor a ",b)
else:
    print(a,"es mayor a ",b)

# a es 5 por lo tanto no puede ser menor a b que es 1, por lo tanto se ejecuta el else

if (b > a):
    print(b,"es mayor a ",a)
else:
    print(b,"es menor a ",a)

"""
Al igual que con if los valores pesados y no pesados siguen valiendo aqui
"""

v1 = 0

if (v1):
    print("Variable con 0")
else:
    print("Se ejecutara ya que no hay nada en la variable")

v2 = ''

if (v2):
    print("Cadena vacia")
else:
    print("Como esta vacia la cadena, se ejecutara el else")