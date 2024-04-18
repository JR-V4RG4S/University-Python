class Vehiculo:
    def __init__(self, color, ruedas):
        self.__color = color
        self.__ruedas = ruedas

    @property  # GET
    def color(self):
        return self.__color 
    
    @property 
    def ruedas(self):
        return self.__ruedas
    
    @ruedas.setter
    def ruedas(self,value):
        self.__ruedas == value

    @color.setter
    def color(self, value):
        self.__ruedas = value

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"

    
if __name__ == "__main__":
    vehiculo0 = Vehiculo("azul",4)
    print(vehiculo0)
    vehiculo1 = Vehiculo("rojo","4 ruedas")
    print(f'El vehiculo es de color: {vehiculo1.color} y de: {vehiculo1.ruedas}')