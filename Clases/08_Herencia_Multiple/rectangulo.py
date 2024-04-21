from Figura_Geometrica import Figura_Geometrica
from Color import Color

class rectangulo(Figura_Geometrica,Color):
    def __init__(self, alto, largo, color):
        Figura_Geometrica.__init__(self,alto,largo)
        Color.__init__(self,color)

    def __str__(self):
        return f'{Figura_Geometrica.__str__(self)} {Color.__str__(self)}'
    
    def calcular_area(self):
        return self.alto * self.largo 
