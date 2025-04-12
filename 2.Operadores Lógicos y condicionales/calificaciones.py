# Calificaciones de un curso 
cali1 = 10
cali2 = 7
cali3 = 8

prom =(cali1+cali2+cali3) /3

if( prom >= 9 ):
    print("Tu calificacion",prom," es una A")
elif( prom > 8 and prom < 9):
    print("Tu calificacion ",prom,"es una B")
elif( prom > 7 and prom < 8):
    print("Tu calificacion",prom," es una C")
elif( prom > 6 and prom < 7):
    print("Tu calificacion",prom," es una d")
elif( prom < 5):
    print("Tu calificacion",prom," es F")
else:
    print("Ingresa una calificacio correcta")