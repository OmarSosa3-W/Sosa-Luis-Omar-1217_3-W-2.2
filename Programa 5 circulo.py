print(" ") #para dejar una linea vacia
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE CIRCULOS Y CILINDROS") #Nombre del creador 
print(" ") #para dejar una linea vacia
#Cálculo del área de un círculo
def mi_area_circulo(r):
    pi_valor = 3.14  # Valor simplificado de Pi
    area = pi_valor * r * r  # Fórmula del área
    return area #se define y termina esta funcion 

#Cálculo del volumen de un cilindro usando el área del círculo
def mi_volumen_cilindro(r, h): #calculo del volumen
    return mi_area_circulo(r) * h #lo que mostrara el calculo (r)
print(" ") #para dejar una linea vacia

radio = float(input("Dame el radio del círculo: ")) #pide ingresar el radio del circulo
print(" ") #para dejar una linea vacia

resultado_area = mi_area_circulo(radio) # Mostrar el área del círculo
print("El área del círculo es:", resultado_area) #el resultado en pantalla
print(" ") #para dejar una linea vacia
 
altura = float(input("Dame la altura del cilindro: ")) # Pedir la altura para el cálculo del volumen
print(" ") #para dejar una linea vacia

resultado_volumen = mi_volumen_cilindro(radio, altura) #se coloca la condicion para mostrar el resultado 
print("El volumen del cilindro es:", resultado_volumen) # Mostrar el volumen del cilindro mostrado en panatlla
print(" ") #para dejar una linea vacia