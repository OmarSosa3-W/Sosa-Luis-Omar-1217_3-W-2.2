print(" ") #para una linea en blanco en la ejecución
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE DISTANCIA") #nombre de creador
print(" ") #para una linea en blanco en la ejecución
def distancia_dirigida(x1, y1, x2, y2):
    # Calculamos la distancia sin usar math
    dx = x2 - x1 #la diferencia entre las coordenadas
    dy = y2 - y1 #la diferencia entre las coordenadas
    distancia = (dx**2 + dy**2)**0.5
    return distancia
print(" ") #para una linea en blanco en la ejecución

# Ejemplo de uso
x1 = float(input("Coordenada x del primer punto: ")) #pide ingresar un numero
print(" ") #para una linea en blanco en la ejecución
y1 = float(input("Coordenada y del primer punto: ")) #pide ingresar un numero
print(" ") #para una linea en blanco en la ejecución
x2 = float(input("Coordenada x del segundo punto: ")) #pide ingresar un numero
print(" ") #para una linea en blanco en la ejecución 
y2 = float(input("Coordenada y del segundo punto: ")) #pide ingresar un numero
print(" ") #para una linea en blanco en la ejecución
print("La distancia dirigida es:", distancia_dirigida(x1, y1, x2, y2)) #imprimir el resultado en pantalla 
print(" ") #para una linea en blanco en la ejecución