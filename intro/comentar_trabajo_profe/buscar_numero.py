import random
lista=[]
tam=random.randint(15,20)
cont=0
print(tam)
for i  in range(tam):

    num=random.randrange(0,9)
    lista.append(num)
print(lista)

n=int(input('escriba numero: '))

for i in range(len(lista)):
        if n == lista[i] :
            cont+=1
            print(f"El numero {n} si esta en la posicion {i}")
print(f'el numero esta repetido {cont} veces')





