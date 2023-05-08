import random
lista = [random.randrange(100)for i in range(random.randint(5,10))]
print(lista)

par =[x for x in lista if x%2==0]
print(par)
parimpar=[x if x%2==0 else x for x in lista]

#si el numero es par sacar raiz si es impar elevar al cuadrado