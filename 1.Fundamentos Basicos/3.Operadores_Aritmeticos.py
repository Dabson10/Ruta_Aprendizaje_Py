"""
Operadores Aritmeticos
En esta hoja se hablara sobre como se realizan las operaciones como: suma, resta, 
multiplicacion, divicion, potencia entre otros.
"""
numero1 = 35
numero2 = 20

cadena1 = "35.5"
cadena2 = " 12.3"

flot1 = 3.99
flot2 = 2.41

# Suma
print("--Suma--")

print("Suma de dos numeros: ", numero1+numero2)

# En la suma de cadenas solamente se concatenan estas, no se hace ninguna
# suma de operaciones solamente se concatena 
print("Suma de dos cadenas: "+ cadena1+cadena2)

print("Suma de numeros decimales: ",flot1+flot2)

# Resta
print("")
print("--Resta--")

print("Resta de dos numeros: ", numero1-numero2)

print("Resta de cadenas: ", cadena1,cadena1)
print("Al restar una cadena no es posible ya que estos son valores String por lo tanto no se pueden restar")

print("Resta de decimales: ", flot1-flot2)

# Multiplicacion 
print("")
print("--Multiplicación--")

print("Multiplicacion de numeros: ", numero1*numero2)
print("")
print("No se puede multiplicar una cadena de texto ya que no es INT o FLOAT")
print("Multiplicacion de cadenas: ", cadena1 , cadena2)


print("Multiplicacion de decimales: ", flot1 * flot2)


# Divicion 
print("")
print("--Divición--")
print("Divicion de dos numeros:",numero1/numero2)

print("De igualmanera no se puede dividir una cadena.")
print("Divicion de dos :",cadena1,cadena2)

print("Divicion de dos :", flot1/flot2)

# Potencia
print("")
print("--potencia--")
print("Potencia de un numero:",numero1**2)

print("De igualmanera no se puede hacer una potencia de una cadena de texto")
print("Divicion de dos :",cadena1,2)

print("Potencia de un decimal  :", flot1**2)


# Divicion con //
print("")
print("--Divicion con // --")
print("Al dividir dos numeros obtenemos: ", numero1/numero2, "resultado 1.75")
print("Pero al dividir con // obtendremos el numero entero sin decimales.")
print("Divicion con //: ", numero1//numero2, "resultado 1")