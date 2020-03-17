#Los Strin son Arrays de caracteres

myStr = "Como Vamos?"

# dir es una ayuda para saber los metodos que se pueden utilizar con esta variable
# # print(dir(myStr))

# # upper sirve para convertir un string en mayusculas o minusculas
# print(myStr.upper())
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.capitalize())

# # Esto sirva para remplazar en una variable str un valor por otro
# print(myStr.replace("Como", "A Tomar"))
# # myStr = myStr.replace("Como", "A Tomar")

# # Cuenta cuantas letras "a" hay
# print(myStr.count("a"))

# # Esto sirva para ver si una cadena texto empieza o acaba con algo determinado
# print(myStr.startswith("Co"))
# print(myStr.endswith("os!"))

# # Devuelve el numero de caracteres que tiene un str
# print(len(myStr))

# # Devuelve la posicion en la que se encuentra "o"
# print(myStr.index("o"))

# # Devulve True o False si la variable es numerica o solo de letras
# print(myStr.isnumeric())
# print(myStr.isalpha())#El signo "?" no es alfa

# # Devuelveel valor de la posicion
# print(myStr[5])
# print(myStr[2])
# print(myStr[0])

# #Se puede obtener los valores del str a la inversa con poner indices negativos
# print(myStr[-1])
# print(myStr[-3])

# Concatenar 
print("Saludo: " + myStr)
# "interpolacion" la f le dice que la variable entre llaves hace referencia a la que a sido creada anteriormente
print(f"Saludo: {myStr}")
# En el valor 0 va a colocar la variable que le paso al metodo format
print("Saludo: {0}".format(myStr))