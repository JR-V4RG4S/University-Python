


""" Escribe una función que tome una lista de números y devuelva una nueva 
    lista que contenga solo los números pares de la lista original."""
    
def filtrar_pares(*numeros):
    lista = []
    for i in numeros:
        if i % 2 == 0:
            lista.append(i)
    print(lista)            

filtrar_pares(1,3,4,7,8,2,9,5)


""" Escribe una función que tome una cadena de texto y devuelva un diccionario 
donde las claves sean los caracteres de la cadena y los valores sean el número 
    de veces que aparece cada caracter en la cadena."""
    

def mensaje(frase):
    diccionario = {}
    for letras in frase:
        if letras in diccionario:
            diccionario[letras] += 1 
        else:
            diccionario[letras] = 1 
    print(diccionario)

mensaje("prueba hola")

"""
  Escribe una función recursiva que tome un número entero positivo n 
  y devuelva el factorial de n.
"""
def factorial(n):
    
    if n > 0:     
        return 1 if n == 1 else n * factorial(n-1)
    else: 
        print("solo numeros positivos")
factorial(5)
    
   
    
def favto(numero):
    if numero > 0:
        return 1 if numero == 1 else numero * favto(numero - 1)        
        print(numero)
    else:
        print("ingrese numeros positivos")
favto(5)


# Escribe una función que tome una lista de números y devuelva la lista 
# ordenada de menor a mayor.

def ordenar_lista(*lista):
    lista = list(sorted(lista))
    print(lista)
    
ordenar_lista(2,8,5,0,9,1)


# Escribe una función que tome una lista de números y devuelva la lista 
# ordenada de  mayor a menor.

def ordenar_lista(*lista):
    
    lista = sorted(list(lista),reverse = True)
    print(lista)
    
ordenar_lista(2,8,5,0,9,1)


# Escribe una función recursiva que tome una cadena de texto y devuelva la cadena invertida.
def invertir_cadena(cadena):
    if cadena == "":
        return cadena 
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]
    
invertir_cadena("hola")

# invertir las palabras
v1 = "hola ben"
print(v1[::-1])

# muestre las palabras pares 
v1 = "hola ben"
print(v1[1::2])

# Ordenar una cadena por orden alfabetico
cad="zxywv"
cad = sorted(cad)
print("".join(cad))

# Escribe una función que tome una lista de números y devuelva el producto de todos los números en la lista.
def producto_lista(*lista):
    lista = list(lista)
    print(f"el producto es: {sum(lista) / len(lista)}")
producto_lista(10,10,10,10,10)

# Escribe una función que tome una lista de números y devuelva el número más grande en la lista.
def maximo(*lista):
    print(max(lista))

maximo(2,3,4,5,98)


# Escribe una función que tome una cadena de texto y devuelva la misma cadena pero con cada palabra capitalizada.
def capitalizar(cadena):
    print(cadena.upper())

capitalizar("hola como estan")


# Escribe una función recursiva que tome un número entero positivo n y devuelva la suma de todos los números enteros desde 1 hasta n.
def suma_hasta_n(n):
    if n > 1:
        return n + suma_hasta_n(n-1)
    elif n == 1:
        return 1     
    else:
        print("solo numeros positivos")
    
suma_hasta_n(10)






