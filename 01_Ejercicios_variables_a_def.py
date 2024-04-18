
# EJericico Cómo estuvo tu día 
dia = int(input("Cómo estuvo tu día: "))
print(f'tu día estuvo de {dia}')

# EJericico Detalles de un libro
libro = input("Proporciona el nombre del libro: ")
autor = input("Proporciona el nombre del autor: ")

print(f'El libro {libro} fue escrito por el autor {autor}')

#  Ejercicio de rectangulo: 
"""Se solicita calcular el área y el perímetro de un rectangulo, 
   para ello crearemos las variables: alto(int), ancho(int) """
       
alto = int(input("proporciona el alto: "))
ancho = int(input("proporciona el ancho: "))

area = alto * ancho  
perimetro = (alto + ancho) * 2

print(f' El área del rectangulo es: {area} \n El perímetro del rectangulo es: {perimetro}')
    
# Ejercicio: identificar si un número es par o impar 
v1 = int(input("ingrese un número entero: "))
v1 = 'Par' if v1 % 2 == 0 else 'Impar'
print("El número es",v1)


# Ejercicio Determinar si es mayor de edad 
edad = int(input("indique su edad: "))
x = 'Mayor de edad' if edad >= 18 else 'Menor de edad'
print(f"la persona con edad {edad} es",x)


# Ejercicio Valor dentro de un rango, verificar si el número está dentro de 0 y 5 
num = int(input("indique un número: "))
x = 'en el rango' if 5 >= num >= 0 else 'fuerda de rango'
print(f"El número {num} está", x)


# Ejercicio Or: el padre puede asistir cuando sea uno de los 2 dias 
holiday = False
Sunday = True 

v1 = 'puede asistir' if holiday or Sunday is True else 'no puede asistir'
print("El padre",v1)

# Ejercicio Not: el padre puede No asistir cuando sea uno de los 2 dias 
holiday = True
Sunday = False 

v1 = 'no puede asistir' if not holiday or Sunday is True else 'puede asistir'
print("El padre",v1)


# Ejercicio:Rango de edad 20's, 30's 
edad = int(input("introduzca su edad: "))
x = "los 20\'s" if 20 <= edad < 30 else ("los 30\'s" if 30 <= edad < 40 else "fuera de rango" )
print('está en', x)

# Ejercicio: el mayor de 2 valores 
v1 = int(input("introduzca el primer valor: "))
v2 = int(input("introduzca el segundo valor: "))

x = v1 if v1 > v2 else v2 
print(f"el valor mayor es {x}")

# Ejercicio Libros 
print("Proporcione los siguientes datos del libro")

nombre = input("Proporcione el nombre: ")
idlibro = int(input("proporcione el Id del libro: "))
precio = float(input("proporcione el precio del libro: "))
envio = input("indique si el envio es gratuito Y/N: ")

print(f"Los datos del libro son: \n Nombre: {nombre} \n ID: {idlibro} \n Precio: {precio} \n Envio: {envio} ")

# Ejercicio: Convertir número en texto
texto = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
v1 =int(input("introduce un número del 1 al 10: "))

v1 = texto[v1-1] if 1 <= v1 <= 10 else "fuera de rango"
print("Número",v1)

# Ejercicio Estacion del año 
est = ["invierno","primavera","verano","otoño"]
mes = int(input("proporciona el mes del año (1-12): "))

indice = (mes - 1) // 3

print("La estacion es", est[indice])

# Ejercicio Proporciona tu edad 

edad = int(input("indica tu edad: "))
mensaje = ["la infancia es increible", "muchos cambios y mucho estudio","amor y trabajo"]

edad = mensaje[edad // 10] if 0 <= edad < 30 else "valor fuera de rango"

print(edad)


# Ejercicio sistema de calificaciones 

"""
9 - 10 = A
8 y < 9 = B
7 y < 8 = c
6 y < 7 = D
5 y < 6 = E
0 y < 5 = F

cualquier otro valor incorrecto
"""

calificacion = ["F","E","D","C","B","A", "valor no válido"]

nota = float(input("indique la nota del estudiante: "))

# INCLUYE EL 9 en A 
if 0 <= nota <= 10:     
   if 5 <= nota <= 10 :
       v2 = calificacion[int(nota) - 4] if nota != 10  else calificacion[5]
       print(f"su nota es {v2}")
   else:
       print(calificacion[0])
else: 
    print(calificacion[6])


# EXCLUYE EL 9 EN A 
calificacion2 = ["F","E","D","C","B","A"] 
nota = int(input("indique la nota: "))

if 0 <= nota <= 10:     
    indice = (nota - 5) if nota >= 5 else 0    
    print("la nota es",calificacion2[indice])
else:
    print("valor no válido")

# Ejercicio while: Imprimir del 0 al 5 

v1 = 0
while v1 <= 5:
    print(v1)
    v1 += 1        

# Ejercicio imprimir del 5 al 1 
v1 = 5
while v1 >= 1:
    print(v1)
    v1 -= 1
    
# Ejercicio: iterar numeros del 1 al 10 e imprimir los divisibles entre 3 

v1 = 0 
while v1 <= 10:
    v1 += 1 
    x = print(v1) if v1 % 3 == 0 else None
 
    
for i in range(11):
    x = print(i) if i % 3 == 0 else None

# Ejercicio: Crear un rango de numeros de 2 a 6

for i in range(2,7):
    print(i)

# Ejercicio: Crear un rango de numeros de 3 a 10 pero con incremento de 2 en 2
for i in range(3,11,2):
    print(i)


# Ejercicio: crea una lista que incluya los numeros menores a 5 de la sgte tupla

v1 = (13,1,6,3,9,5,4)
list1 = []

for i in v1:
    x = list1.append(i) if i < 5 else None    
print(list1)


# Ejercicio: sumar argumentos variables 
def sumar(*numeros):
    v1 = 0
    for i in numeros:
        v1 += i
    return v1
        
print(sumar(2,4,3,2,4))

# Ejercicio: multiplicar argumentos variables 
def multiplicar(*num):
    v1 = 1 
    for i in num:
        v1 *= i
    return v1
    
print(multiplicar(1,2,3,4,5))

# Ejercicio llamar a factorial 

def factorial(numero):
    return 1 if numero == 1 else numero * factorial(numero-1)
    
print("el resultado es:",factorial(5))

# Ejercicio imprimir valores descendente con recursividad 

def desc(numero):
    print(numero) 
    desc(numero - 1) if numero > 1 else (None if numero >= 1 else print("valor incorrecto"))
    
desc(-5)

# Ejercicio Calculadora de impuesto 

def calcular_impuesto(monto,impuesto):
    impuesto = monto * (impuesto / 100)
    print(f'El impuesto a pagar es {impuesto} \nEl total es: {monto + impuesto}')

monto = float(input("Indique el monto: "))
impuesto = float(input("Indique el impuesto a pagar: "))

calcular_impuesto(monto, impuesto)

# Ejercicio convertidor de temperaturas Cº a Fº
def temperatura (temp):
    C = temp * 1.8 + 32             # Formula para obtener Celcius
    F = (temp -32) /1.8             # Formula para obtener Farenheit
    
    x = f'Celcius: {temp} - Farenheit: {C}'
    y = f'Farenheit: {temp} - Celcius: {F}'
    
    print(x) if v1 == "1" else print(y)
            
v1 = input("1) C a F \n2) F a C \nIndique cual conversión desea realizar: ")
temp = float(input("indique la temperatura: "))

temperatura(temp)


# Ejercicio convertidor de temperaturas Cº a Fº V2 (CON VALIDACION IMPLEMENTADA)

def temperatura (temp):

    x = f'Celcius: {temp} - Farenheit: {temp * 1.8 + 32}'
    y = f'Farenheit: {temp} - Celcius: {(temp -32) /1.8}'    
    print(x) if v1 == "1" else print(y)
            
while True: 
    v1 = input("1) C a F \n2) F a C \nIndique cual conversión desea realizar: ")
    if v1 == "1" or v1 == "2": break    

temp = float(input("indique la temperatura: "))
temperatura(temp)



# EJercicios mejorados 

"""
9 - 10 = A
8 y < 9 = B
7 y < 8 = c
6 y < 7 = D
5 y < 6 = E
0 y < 5 = F

cualquier otro valor incorrecto
"""

calificacion =["F","E","D","C","B","A","valor incorrecto"]
nota=int(input("ingrese una nota: "))

resultado = 6 if nota < 0 or nota > 10  else (nota - 5 if nota >= 5 else 0)

print(f'la nota del estudiante es: {calificacion[resultado]} ')

#               3           4-6      7-9     10-12
estacion = ["invierno","primavera","verano","otoño"]
dato = int(input("indique el mes del año: "))
dato = (dato - 1) // 3

print(f'La estacion del año es: {estacion[dato]}')


# Ejercicio: crea una lista que incluya los numeros menores a 5 de la sgte tupla

v1 = (13,1,6,3,9,5,4)

l1 = []

for i in v1:
    if i < 5:
        l1.append(i)        
print(l1)