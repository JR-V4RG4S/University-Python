
class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad 
    def mostrar_detalle(self):
        print(f'Persona: Nombre {self.nombre} edad: {self.edad}')
        

persona1 = Persona("Juan",28)
persona1.mostrar_detalle()

persona2 = Persona("Karla",30)
persona2.mostrar_detalle()
