# VERSION MEJORADA

class Vehiculo():
    def __init__(self, ruedas):
        self.__ruedas = ruedas

    def desplazarse(self):
        print(f"Desplazandose con {self.__ruedas} ruedas")

class Carro(Vehiculo):
    def __init__(self):
        super().__init__(4)

class Moto(Vehiculo):
    def __init__(self):
        super().__init__(2)

class Trailer(Vehiculo):
    def __init__(self):
        super().__init__(8)

for vehiculo in Carro(), Moto(), Trailer():
    vehiculo.desplazarse()