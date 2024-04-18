class Persona:
    def __init__(self, nombre, apellido, edad ):
        self.__nombre = nombre 
        self.__apellido = apellido
        self.__edad = edad

    @property           # Para poder traer los valores de las variables encapsuladas 
    def nombre(self):
        return self.__nombre        
    
    def datos(self):
        print(f'los datos son: \n Nombre: {self.__nombre} \n Apellido: {self.__apellido} \n Edad: {self.__edad}')

    @nombre.setter      # Para poder modificar los valores de las variables encapsuladas
    def nombre(self,value):
        self.__nombre = value

persona1 = Persona("Juan","Perez",24)
persona1.datos()

persona1.nombre = "pepe"
print(persona1.nombre)
