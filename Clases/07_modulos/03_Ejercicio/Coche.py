from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.__velocidad = velocidad

    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self,value):
        self.__velocidad = value

    def __str__(self):
        return super().__str__() + f" velocidad Km/hr: {self.velocidad}"


coche0 = Coche("verde",4,180)
print(coche0)


coche1 = Coche("negro","2 ruedas",200)
print(f"El vehiculo es de color: {coche1.color} con {coche1.ruedas} y va a una velocidad de {coche1.velocidad}")