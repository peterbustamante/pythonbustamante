class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__curso = []
    def gestdatos(self):
        return f"{self.__nombre}{self.__edad}{self.__curso}"
    
    def set


