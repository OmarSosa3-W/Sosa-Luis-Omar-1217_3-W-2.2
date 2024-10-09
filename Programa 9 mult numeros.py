print(" ") #para una linea en blanco en la ejecución
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE SUMA Y MULT") #creador del programa
print(" ") #para una linea en blanco en la ejecución
def sumar_lista(lista): #el nombre de la funcion 
    resultado = 0 #iniciando una variable 0
    for num in lista: #bucle que recorre cada elemento de la lista
        resultado += num #línea que suma cada número a la variable
    return resultado

def multiplicar_lista(lista): #se realizara la funcion y se mostrara 
    resultado = 1 #solo se mostrara un resultado
    for num in lista:  #bucle que recorre cada elemento de la lista
        resultado *= num #línea que suma cada número a la variable
    return resultado 

# Ejemplo de uso
mis_numeros = [1, 2, 3, 4]
print(" ") #para una linea en blanco en la ejecución
print("La suma es:", sumar_lista(mis_numeros))# Debería devolver 10
print(" ") #para una linea en blanco en la ejecución
print("La multiplicación es:", multiplicar_lista(mis_numeros))  # Debería devolver 24
print(" ") #para una linea en blanco en la ejecución