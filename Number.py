10 #Entero
14.4 #Flotante

print(type(10))
print(type(14.4))

#Cuando sumamos un numero entero y uno flotante devuelve un flotante

# Exponente
print(2**3)
# Division
print(3/2)
# Division entera
print(3//2)
# Modulo, residuo
print(10%4)

# Input te permite insertar datos STRING por teclado
edad = input("Inserta tu edad: ")
print(type(edad))
# parseamos la edad ya que es un String, para que pueda realizar la operacion
nueva_edad = int(edad) + 5
print(nueva_edad)
