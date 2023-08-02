class Aprndices:
    def __init__(self,codigo,puntaje_matematicas,puntaje_español,puntaje_sociales):
        self.__codigo = codigo
        self.__puntaje_matematicas = puntaje_matematicas
        self.__puntaje_español = puntaje_español
        self.__puntaje_sociales = puntaje_sociales
        def verDatos(self):
            return f'{self.__codigo}{self.__puntaje_matematicas}{self.__puntaje_español}{self.__puntaje_sociales}'