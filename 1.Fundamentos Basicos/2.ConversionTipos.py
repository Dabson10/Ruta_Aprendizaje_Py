"""
Python es un lenguaje tipado dinamico en el cual no es necesario definir la que tipo de varible sera
solamente se da un nombre y se le asigna un valor sin especificar si es string, int o float,
ya que se detecta al momento de asignar un valor a la variable.
Solamente que si tienes una variable numerica o int y quieres sumarla o con un numero en forma de cadena
no se podra por esot mismo es necesario convertir una cadena a numero para poder hacer una operacion
correcta.
En los ejemplos siguientes se ve como se asigna una variable y como se hace el cambio del tipo
ya sea de int a float o a cadena 
"""

print("Conversion de cadena a numero")
cadena1 ="225"
# Convercion de cadena a numero
print(type(cadena1))
print(int(cadena1))
print(type(int(cadena1)))
print(int(cadena1))

print("--Conversion de numero a cadena--")
numero1 = 51
# Conversion de numero a cadena
print(type(numero1))
print(str(numero1))
print(type(str(numero1)))
print(str(numero1))

# Conversion de cadena a float
print("--Conversion de cadena a float--")
cadena2 = "3.99"
print(type(cadena2))
print(float(cadena2))
print(type(float(cadena2)))
print(float(cadena2))

# Conversion de float a cadena
print("--Conversion de float a cadena--")
decimal1 = 2.99 
print(type(decimal1))
print(str(decimal1))
print(type(str(decimal1)))
print(str(decimal1))

# Conversion de float a int 
print("--Conversion de float a int-")
decimal2 = 9.2
print(decimal2)
print(type(int(decimal2)))
print(int(decimal2))

# Conversion de int a float
numero2 = 20
print(type(numero2))
print(numero2)

print(type(float(numero2)))
print(numero2)