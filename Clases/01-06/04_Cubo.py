class Cubo:
    def __init__(self, alto,ancho,profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad
    
    def calcular_volumen(self):
        return self.alto * self.ancho * self.profundidad

alto = int(input("Ingrese el alto:"))
ancho = int(input("Ingrese el ancho:"))
profundidad = int(input("Ingrese la profundidad :"))

operacion = Cubo(alto,ancho,profundidad)

print(f'El área del cubo es: {operacion.calcular_volumen()}')