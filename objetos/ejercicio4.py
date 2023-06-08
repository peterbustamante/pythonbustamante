#
class empleado:
    def __init__(self,nombre,cargo,salario,extras):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.extras = extras


    def getdatos(self):
        return f"{self.nombre,self.cargo,self.salario,self.extras}"



    def horas(self):

        hr =self.salario//30
        hr//=8
        return hr
    def ipc

    def horasex(self):
        salarioex= self.horas()
        trabajo= self.extras
        if salarioex > 2:
            trabajo *= salarioex
            return(trabajo)
        else:
            print("no es posible")

h= empleado("pepe","chef",1200000,2)

print(h.getdatos())
print(h.horas())
print(h.horasex())
    # def  ipc(self):

