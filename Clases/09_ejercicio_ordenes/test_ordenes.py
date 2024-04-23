from Producto import *
from Ordenes import * 

producto1 = Producto("reloj 4z",200)
producto2 = Producto("cargador inalámbrico",100)
producto3 = Producto("funda",50)
producto4 = Producto("tablet",250)


productos1 = [producto1, producto2]
orden1 = Ordenes(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f'el total de la orden 1 es: {orden1.calcular_total()}')

productos2 = [producto3, producto4]
orden2 = Ordenes(productos2)
print(orden2)
print(f'El total de la orden 2: {orden2.calcular_total()}')
