import random


def llenar(m,n):
    lista=[]
    lista=[random.randrange(m) for x in range(n)]
    return lista
r=llenar(100,10)
r2=llenar(100,10)
#cual de los 2 tiene la suma mas alta
def suma(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma

if suma(r) > suma(r2):
    sumamayor=suma(r)
else:
    sumamayor=suma(r2)

def mayor(lista):
    may=0
    for o in lista:
        if o >may:
            may=o
    return may


if mayor(r) > mayor(r2):
    ayor=mayor(r)
else:
    ayor=mayor(r2)






print(r)
print(r2)
print(suma(r))
print(suma(r2))
print(sumamayor)
print('mayor lista 1 :',mayor(r))
print('mayor lista 2 :',mayor(r2))
print(ayor)
