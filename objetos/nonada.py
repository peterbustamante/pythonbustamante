class Cola:
    def __init__(self):
        self.cola = []
#metodo para agregar elementos en la estructura tipo cola
    def agregar(self, elemento):
        self.cola.append(elemento)

def ingreso():
    frecuente = input("  ¿Es cliente frecuente? (s/n):  ")
    if frecuente == "s" or "S" or "SI" or "si":
        tipo = "Cliente frecuente"
    else:
        tipo = "Otro tipo"
    nombre = input("  Nombre de cliente:  ")
    apellido = (input("  Apellido:  "))
    return [nombre, apellido, tipo]

cola_item = Cola()
cola_item.agregar(ingreso())
