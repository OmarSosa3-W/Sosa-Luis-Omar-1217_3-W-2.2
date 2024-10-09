print(" ") #se colca para dejar un eapacio
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE SALUDOS DESEADOS") #nombre del creador
print(" ")#se colca para dejar un eapacio

def mostrar_saludo(): #definir una funcion
    """Función que muestra un saludo."""
    print("Hey amigos!") #coloca el mensaje que se quiere mostrar

# Inicializar un contador
contador = 0 #servirá para llevar la cuenta de cuántas veces se ha ejecutado

# Solicitar cuántas veces quiere ver el saludo
veces = int(input("¿Cuántas veces quieres ver el saludo? ")) #pregunta al usuario el numero de veces por saludo

# Bucle para mostrar el saludo
while contador < veces: #el contador es menor que el numero de veces a mostrar
    print(" ")#se colca para dejar un eapacio
    mostrar_saludo() #mostrar el saludo
    contador += 1 #el contador sumara uno por cada ves 

print("¡Hasta luego!") #imprime el mensaje al terminar el bucle
print(" ")#se colca para dejar un eapacio#mostrar mensaje cada ves que el usuario desee

