print(" ") #para dejar una line en blanco 
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE LONGITUD DE PALABRAS") #nombre del creador 
print(" ") #para dejar una line en blanco 
def longitud_ultima_palabra(cadena): #se ingresa el nombre de la funcion 

    palabras = cadena.strip().split() # Dividir la cadena en palabras ignorando los espacios extra
    
    if len(palabras) == 0: # Verificar si hay palabras en la lista
        return 0  # Si no hay palabras, la longitud es 0
    
    return len(palabras[-1]) # Devolver la longitud de la última palabra
print(" ") #para dejar una line en blanco 

# Ejemplo de uso:
texto = input("Introduce una frase: ") #pide al usuaio poner una frase
print(" ") #para dejar una line en blanco 
resultado = longitud_ultima_palabra(texto) #se leera el texto escrito
print("La longitud de la última palabra es:", resultado) #muestra el resultado en pantalla
print(" ") #para dejar una line en blanco 