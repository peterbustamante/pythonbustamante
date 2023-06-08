class persona:
    def __init__(self,nombre,documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__curso=[]
    def getnombre(self):
        return self.__nombre
    def getdocumento(self):
        return self.__documento
    def getdatos(self):
        return f"{self.__nombre} {self.__documento}"
    def getcurso(self,c):
        self.__curso.append()

p=persona("peter",15)
g=persona("alexander",56)
print(p.getnombre())
print(p.getdocumento())
print(g.getnombre())
print(g.getdocumento())

# print(p.getdatos())
# print(p.getcurso())


