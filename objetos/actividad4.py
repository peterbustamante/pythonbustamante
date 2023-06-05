#
class empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def getdatos(self):
        return f"{self.nombre,self.cargo,self.salario}"

    def tpcargo(self):
        return self.cargo

    def tpsalario(self):
        return self.salario

    def horas(self,salario):
        hr = self.salario//22
        hr = hr//8

    def  ipc(self):
