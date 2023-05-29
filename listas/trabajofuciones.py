import random
n=random.randint(10,15)
N = int(input('ingrese numero:'))
def llenarlista(N,n):
    lista=[]
    lista=[random.randrange(N)for x in range(n)]
    return lista



def suma(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma

def promedio(lista):
    return suma(l)/len(lista)

def mayor(lista):
    may=0
    for o in lista:
        if o >may:
            may=o
    return may

def menor(lista):
    men=N+1
    for o in lista:
        if o <men:
            men=o
    return men

def asender(lista):
    listam=lista
    for i in range(n):
        for o in range(i+1,n):
            if listam[i] > listam[o]:
                listam[i],listam[o] = listam[o],listam[i]
    return listam

def desender(lista):
    listap=lista
    for i in range(n):
        for o in range(i+1,n):
            if listap[i] < listap[o]:
                listap[i],listap[o] = listap[o],listap[i]
    return listap

# def moda(lista):
#     mod=0
#     listad=lista
#     for i in range(n):
#             for o in range(i+1,n):
#                 if listad[i] == listad[o]:
#     return listad




l=llenarlista(N,n)
print(l)
print('suma dee las lista :',suma(l))
print('promedio de lista :',promedio(l))
print('mayor de lista :',mayor(l))
print('menor de lista :',menor(l))
print(asender(l))
print(desender(l))
#print(moda(l))

