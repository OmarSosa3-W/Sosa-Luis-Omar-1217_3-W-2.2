# Sosa-Luis-Omar-1217_3-W-2.2
Envio de la segunda practica de la unidad 2
PROGRAMA 1

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

![image](https://github.com/user-attachments/assets/509e3297-31b4-4b93-abd1-32e4288b85bc)
![image](https://github.com/user-attachments/assets/b3613909-cc72-4ffc-a4e1-22e0dd4614cb)

PROGRAMA 2 
print(" ") #se coloca para dejar una linea vacia
print("SOSA LUIS OMAR 3-W 1217: MI PRACTICA DE SALUDAR (HOLA/NOMBRE)") #nombre del creador del codigo
print(" ") #se coloca para dejar una linea vacia
def saludo (nombre):
    print(f"Hola {nombre} ! ") #para que imprima el saludo

    print(" ") #se coloca para dejar una linea vacia
nombre = input("Ingrese su nombre: ") #pide al usuario ingresar un nombre
print(" ") #se coloca para dejar una linea vacia
saludo(nombre) #lo que se mostrara en pantalla

![image](https://github.com/user-attachments/assets/3c6b46ee-f582-402c-8a8f-ff5db1bce26e)
![image](https://github.com/user-attachments/assets/9789594a-2bf7-4934-a875-9bc48a18d91b)

PROGRAMA 3 
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

![image](https://github.com/user-attachments/assets/2dc97622-9fb4-47ce-9282-5f47c984b894)
![image](https://github.com/user-attachments/assets/4f24d2b7-f2fc-486d-8fa5-c4ee3501a408)

PROGRAMA 4 
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

![image](https://github.com/user-attachments/assets/728b9a5a-a35b-4156-bf69-63df42dbbb73)
![image](https://github.com/user-attachments/assets/8025feef-2100-491d-a28b-1a62b806e152)

PROGRAMA 5

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

![image](https://github.com/user-attachments/assets/2c543bd7-eb0c-48f8-b8ef-f5bcdbb12c00)
![image](https://github.com/user-attachments/assets/8b73f549-74de-428a-8845-160250e07382)

PROGRAMA 6

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

![image](https://github.com/user-attachments/assets/699f8b4e-b329-476f-a200-d76eb941fb49)
![image](https://github.com/user-attachments/assets/668513d0-0e3d-419a-99aa-f75db0bbe26a)

PROGRAMA 7 

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

![image](https://github.com/user-attachments/assets/e305b9b8-2242-49ad-b1da-afbdf4c34e17)
![image](https://github.com/user-attachments/assets/88d964bd-e980-4109-b78c-d9df8786e529)

PROGRAMA 8 

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

![image](https://github.com/user-attachments/assets/5174a892-4cc1-421c-8053-0522b51f4aff)
![image](https://github.com/user-attachments/assets/fa604240-5c5a-458c-a35d-82d1c103c9f5)

PROGRAMA 9

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

![image](https://github.com/user-attachments/assets/73c67d46-0489-47a3-9662-5726da6e7eda)
![image](https://github.com/user-attachments/assets/59f0db86-153f-46ce-ade3-6f57f718a7f9)

PROGRAMA 10

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

![image](https://github.com/user-attachments/assets/bf96ee67-55cc-437e-8129-92271f9dfbbe)
![image](https://github.com/user-attachments/assets/4c09adb6-55d7-4f8d-8e45-0cf09eea2c7a)

PROGRAMA 11

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

![image](https://github.com/user-attachments/assets/2555f75f-46e5-4933-bc6f-fe4b9ab41528)
![image](https://github.com/user-attachments/assets/dd3700cb-66b2-48bd-a471-383eebb5d301)


