class Carro():
    
    def __init__(self):
        self.__ruedas = 4
    
    def desplazarse(self):
        print(f"Desplazandose con {self.__ruedas} ruedas")
        
class Moto():
    
    def __init__(self):
        self.__ruedas = 2
    
    def desplazarse(self):
        print(f"Desplazandose con {self.__ruedas} ruedas")
        
class Trailer():
    
    def __init__(self):
        self.__ruedas = 8
        
    def desplazarse(self):
        print(f"Desplazandose con {self.__ruedas} ruedas")


for obj in Carro(),Moto(),Trailer():
    obj.desplazarse()