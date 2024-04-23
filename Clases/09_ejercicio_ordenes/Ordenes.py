from Producto import Producto

class Ordenes(Producto):    
    contador_ordenes = 0
    def __init__(self, productos):
        Ordenes.contador_ordenes += 1    
        self.__id_orden = Ordenes.contador_ordenes     
        self.__productos = list(productos)

    @property
    def productos(self):
        return self.__productos

    @productos.setter 
    def productos(self, value):
        self.__productos = value 

    @property
    def id_orden(self):
        return self.__id_orden
    
    @id_orden.setter
    def id_orden(self,value):
        self.__id_orden = value
    
    def agregar_producto(self, producto): 
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + '\n'
        
        return f'Orden: {self.id_orden} \n Productos \n{productos_str} '
    
if __name__ == '__main__':
    producto1 = Producto("reloj 4z",200)
    producto2 = Producto("iphone 14pro",1500)

    productos = [producto1,producto2]
    orden1 = Ordenes(productos)
    print(orden1)