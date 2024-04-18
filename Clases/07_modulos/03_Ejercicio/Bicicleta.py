from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.__tipo = tipo
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, value):
        self.__tipo == value

    def __str__(self):
        return super().__str__() + f' Tipo: {self.tipo}'
    

bicicleta0 = Bicicleta("gris",2,"Montañera")
print(bicicleta0)

bicicleta1 = Bicicleta("roja","3 ruedas","montañera")
print(f'La bicicleta es de color: {bicicleta1.color} de: {bicicleta1.ruedas} y del tipo: {bicicleta1.tipo}')