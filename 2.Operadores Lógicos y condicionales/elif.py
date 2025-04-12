"""
Ahora ya manejamos correctamente if y else, pero que sucede cuando
en base a una condicion que necesitemos tenemos muchas opciones o mas de una
condicion, esto en otros lenguajes como java, c y c++ es switch, en kotlin when 
y en python es elif, es necesario usar y y tal vez else por si no se cumple 
ninguna, su sintaxis es la siguiente : 

if (condicion):
    linea_de_codigo_que_se_ejecutara
elif (otra condicion):
    linea_de_codigo_que_se_ejecutara
else:
    linea_de_codigo_que_se_ejecutara_si_no_se_cumple_el_if_o_elif

"""

num = 14

if (num < 10):
    print(num,"es menor a 10")
elif (num <20):
    print(num,"es menor a 20")
else:
    print("No hay un numero definido") 