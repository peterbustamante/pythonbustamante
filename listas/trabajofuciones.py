import random
n=random.randint(10,15)

def llenarlista(rango,n):
    lista=[]
    lista=[random.randrange(rango)for x in range(n)]
    return lista

l=llenarlista(N,n)
print(l)