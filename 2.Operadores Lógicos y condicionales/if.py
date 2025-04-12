"""
A la ora de programar linealmente es necesario en ocaciones que cierto
bloque de codigo no se ejecute, para esto mismo sirven las condicionales 
o if, para que cuando se cumpla una accion se ejecute cierto bloque de 
codigo.
La sintaxis de el condicional if es 

if condicional:
    linea_de_codigo_que_se_ejecutara

Un punto clave en condicionales es que se maneja la separacion u orden
mediante tabulaciones
"""
# Ejemplos de uso de if, verificar si un numero es mayor a otro

a = 1 
b = 5 

if (a < b):
    print("El valor de ",a,"es menor a ",b)
# El codigo anterior se ejecutara siempre y cuando a sea menor a b 

if (b > a) :
    print("El valor de ",b,"es mayor a:",a)

"""
Otro caso de uso con respecto a las condicionales es cuando se 
ingresa una condicional sin eso condicionar con otro valor u operacion 
¿Qué es lo que se ejecuta o como funciona el if?
para empezar hay dos secciones valores con peso y sin peso

Los valores sin peso son aquellos que estan vacios, indefinidos , falsos, sin numero o 0

Los valores con peso son valores que se pueden moldear a nuestro gusto,
como una cadena de texto, un numero, un true, objetos o arrays aunque este vacio

A continuacion un ejemplo de esto 
"""
# -------------Valores sin peso----------------------
v1 = ""
v2 = ''
v3 = 0
v4 = False
if (v1):
    print("Cadena Vacia")

if(v2):
    print("Cadena Vacia")

if (v3):
    print("Numero = 0")

if (v4):
    print("Un valor falso")

# -------------Valores con peso----------------------

vv1 = "Hola"
vv2 = 'Mundo'
vv3 = 6
vv4 = True

if (vv1):
    print(vv1)

if (vv2):
    print(vv2)

if (vv3):
    print(vv3)

if (vv4):
    print(vv4)



# Ahora si sabemos como funciona la condicional if en python
# Se podria decir que no aplica en todos los lenguajes, en este caso aplica a los
# lenguajes dinamicos y por ejemplo en c/c++  el 0 es comparado a un valor False
# y en java debes de hacer de afuerza una comparacion o algo para proceder