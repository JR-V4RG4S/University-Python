from abc import ABC, abstractmethod

class Figura_Geometrica(ABC):
    def __init__(self, alto, largo):
        self.__alto = alto
        self.__largo = largo 
    
    # Encapsulamiento Alto
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto (self,value):
        self.__alto = value

    # Encapsulamiento Largo 

    @property
    def largo(self):
        return self.__largo

    @largo.setter
    def largo(self,value):
        self.__largo = value

    # Definimos clase abstracta 

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'El Alto es: {self.alto}, el largo es {self.largo}'