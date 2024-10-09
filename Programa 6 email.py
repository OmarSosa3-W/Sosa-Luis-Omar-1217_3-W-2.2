print(" ") #se coloca para dejar un espacio
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE CORREO")
print(" ") #se coloca para dejar un espacio

# Función que revisa si un correo es válido
def revisar_email(correo):
    print(" ") #se coloca para dejar un espacio
    if "@" in correo:  # Revisar si contiene @
        return True
    else:
        return False
    print(" ") #se coloca para dejar un espacio

correo_ingresado = input("Escribe tu dirección de correo electrónico: ") #Pedir que ingrese su correo
print(" ") #se coloca para dejar un espacio

if revisar_email(correo_ingresado): # Verificar si es válido o no
    print("La dirección de correo es válida.") #marca la opcion valida
    print(" ") #se coloca para dejar un espacio
else:
    print("Dirección de correo inválida. No contiene '@'.") #marca la opcion no valida
    print(" ") #se coloca para dejar un espacio