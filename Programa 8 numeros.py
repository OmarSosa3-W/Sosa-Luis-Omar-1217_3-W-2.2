print(" ") #para una linea en blanco en la ejecución
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE NUMEROS MAYORES") #nombre del creador 
print(" ") #para una linea en blanco en la ejecución
def mayor_de_tres(num1, num2, num3):
    # Inicialmente asumimos que el primero es el mayor
    mayor = num1
    
    # Comparamos con el segundo número
    if num2 > mayor:
        mayor = num2
    
    # Comparamos con el tercer número
    if num3 > mayor:
        mayor = num3
    
    # Devolvemos el mayor de los tres
    return mayor
print(" ") #para una linea en blanco en la ejecución
# Ejemplo de uso
n1 = float(input("Ingresa el primer número: ")) #pide al usuario ingresar un numero 
print(" ") #para una linea en blanco en la ejecución
n2 = float(input("Ingresa el segundo número: ")) #pide al usuario ingresar un numero
print(" ") #para una linea en blanco en la ejecución
n3 = float(input("Ingresa el tercer número: ")) #pide al usuario ingresar un numero
print(" ") #para una linea en blanco en la ejecución 
print("El número mayor es:", mayor_de_tres(n1, n2, n3)) #muestra el resultado en pantalla
print(" ") #para una linea en blanco en la ejecución