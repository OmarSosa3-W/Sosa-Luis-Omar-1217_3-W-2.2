print(" ")#se coloca para dejar un espacio
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE FACTORIAL")
print(" ")#se coloca para dejar un espacio
n = int(input("Ingresa un número entero positivo: "))#Solicitar un número al usuario


factorial = 1#Inicializar el factorial en 1
# Calcular el factorial multiplicando los números de n a 1
for i in range(1, n + 1):#el range para mostrar los numeros enteros del factorial
    
    factorial = factorial * i #Multiplicar directamente
#mostrar el resultado
print(" ")#se coloca para dejar un espacio
print("El factorial de", n, "es", factorial)#mostrar el resultado en pantalla
print(" ")#se coloca para dejar un espacio