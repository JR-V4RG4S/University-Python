
""" AÑADIREMOS TAMBIEN EL GET Y SETTER A LAS OTRAS 2 VARIABLES"""

class Persona:
    def __init__(self, nombre, apellido, edad ):
        self.__nombre = nombre 
        self.__apellido = apellido
        self.__edad = edad

# funciones GET     

    @property           # Para poder traer los valores de las variables encapsuladas 
    def nombre(self):
        return self.__nombre            

    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def edad(self):
        return self.__edad

# Funciones Setter
    
    @nombre.setter      # Para poder modificar los valores de las variables encapsuladas
    def nombre(self,value):
        self.__nombre = value

    @apellido.setter
    def apellido(self,value):
        self.__apellido = value

    @edad.setter
    def edad(self,value):
        self.__edad = value

# Otras funciones 

    def datos(self):
        print(f'los datos son: \n Nombre: {self.__nombre} \n Apellido: {self.__apellido} \n Edad: {self.__edad}')


persona1 = Persona("Juan","Perez",24)
persona1.datos()

# Asignamos nuevos datos a las variables 

persona1.nombre = "pepe"
persona1.apellido = "gonzales"
persona1.edad = 49
persona1.datos()
