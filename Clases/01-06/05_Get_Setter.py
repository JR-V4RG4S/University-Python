class Persona:
    def __init__(self,nombre):
        self.__nombre = nombre        

    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self,value):
        self.__nombre = value

persona1 = Persona("juan")  

print(persona1.Nombre)
persona1.Nombre = "Pepe"
print(persona1.Nombre)