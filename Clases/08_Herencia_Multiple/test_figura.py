from Cuadrado import *
from rectangulo import *

Cuadrado1 = Cuadrado(5,'rojo')

print(Cuadrado1)
print(f'El area del Cuadrado es: {Cuadrado1.calcular_area()}')

rectangulo1 = rectangulo(5,10,'verde')

print(rectangulo1)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')
