"""
Operadores Logicos
Los operadores logicos son herramientas que permiten moldear la 
logica de un codigo con respecto a lo que necesitemos al momento de
programar, por esto mismo es necesario aprender a usarlas en su totalidad
"""
# AND o and
"""
Este operador logico tiene la funcion de devolver un True solamente 
si dos o mas expresiones son correctas podemos ver un ejemplo a continuacion.
"""
a = 20 
b = 10

# En  el siguiente if la condicion es si a es mayor a 10 y b es menor a 20 pero eso que 
# como tal ejecutara cuando ambos cumplan la condicion ya que de ambas pertes debe de devolver un 
# true 
if (a > 10 and b <20 ):
    print(a,"es mayor a 10 y ", b,"es menor a 20")
else:
    print("No se ejecuto")

# El siguiente ejemplo no cumple
if (a < 10 and b > 20):
    print(a,"es menor a 10 y ", b,"es mayor a 20")
else:
    print("No se cumple la condiocinal")

# Otro ejemplo es cuando se cumple uno pero el otro no 
if (a > 10 and b >20 ):
    print(a,"es mayor a 10 y ", b,"es menor a 20")
else:
    print(a,"es mayor a 10, pero", b ,"es menor a 20")
    print("Por lo tanto no cumple")

# OR o or
"""
Este operador logico tiene la funcion de tener dos valores y se ejecutara aunque uno sea falso 
en el caso de and ambos tenian que ser true, pero con or no es necesario que ambos 
cumplan la condicion.
"""

edad1 = 17
edad = 19
# vivo = True
vivo = False
# En este ejemplo la condicion es ser mayor a 18 o que vivo tenga true, 
# si planteamos que tengo menos de 18 y en vivo devuelve true me manda al else
# mostrando en este caso que eres menor de edad y estas muerto.
if (edad1 > 18 or vivo):
    print("Eres mayor de edad o aun sigues vivo")
else:
    print("Eres menor de edad y estas muerto")


# NOT o not
"""
Este operador logico tiene la funcion de invertir los valores en la condicion.
como acontinuacion se presentara.
"""

verdad = True
falso = False 
"""
Como vimos en los valores pesados un if procede siempre que haya un valor 
True, en el siguiente if se ve que no procede por el hecho que verdad se hizo 
contraria osea False con el uso de not
"""
if (not verdad ):
    print("El valor es falso")
else:
    print("El valor es verdad")

"""
En este caso el if procedera y mostrara que el valor es verdadero, esto por que 
falso siendo False con not se convirtio en True, por esto mismo se logra ejecutar el if
"""
if( not falso):
    print("El valor es verdadero")
else:
    print("El valor es falso")












