# Ejercicio de si un numero es primo o no
import math
num = 15

if(num > 2):
    if (num % 2 ==0):
        print(num,"No es primo")
    else:
        if(num % 3 == 0 ):
            print("Tu numero no es primo ")
            print("el")
        
elif(num == 2 ):
    print("Tu numero es primo ")
else:
    print("Tu numero no es primo")