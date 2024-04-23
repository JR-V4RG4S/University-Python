class Producto:

    contador_productos = 0 
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio

    # Encapsulamiento
    @property
    def id_producto(self):
        return self.__id_producto
        
    @id_producto.setter
    def id_producto(self,value):
        self.__id_producto = value 

    @property
    def nombre(Self):
        return Self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, value):
        self.__precio = value
    
    # Funcion __STR__
    def __str__(self):
        return f' ID: {self.id_producto} \n Nombre: {self.nombre} \n Precio: {self.precio} $'


if __name__ == '__main__' :
    producto1 = Producto("reloj 4z",200)
    print(producto1)


