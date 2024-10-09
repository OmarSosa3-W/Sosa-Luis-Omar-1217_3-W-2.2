print(" ") #se coloca para un espacio en blanco al ejecutar
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE IVA") #nombre del creador
print(" ") #se coloca para un espacio en blanco al ejecutar

sin_iva = float(input("Escribe el precio sin IVA: ")) #Pedir la cantidad sin IVA
print(" ") #se coloca para un espacio en blanco al ejecutar

iva = float(input("Porcentaje de IVA: ")) # Preguntar el porcentaje de IVA
print(" ") #se coloca para un espacio en blanco al ejecutar

total = sin_iva * (1 + iva / 100) # Sumar el IVA a la cantidad original
print(" ") #se coloca para un espacio en blanco al ejecutar

print("El precio final con IVA es:", total) # Mostrar el resultado
print(" ") #se coloca para un espacio en blanco al ejecutar