print(" ") #para una linea en blanco en la ejecución
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE VOCALES") #nombre del creador
print(" ") #para una linea en blanco en la ejecución
def es_vocal(c):
    # comparaciones que verifican si el carácter ingresado
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or \
       c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        return True #si es verdadero
    return False #si es falso
print(" ") #para una linea en blanco en la ejecución
# Ejemplo de uso
car = input("Escribe un carácter: ") #pide al usuario ingresar un caracter
print(" ") #para una linea en blanco en la ejecución
print(es_vocal(car)) #se lee el caracter
print(" ") #para una linea en blanco en la ejecución