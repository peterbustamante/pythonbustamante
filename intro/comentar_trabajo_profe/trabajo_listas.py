import random
lista=[]
cuadrado=[]
suma=0
promedio=0
mayor=0
menor=101
tam=random.randint(10,20)
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
    suma+= num
    n= num
    if n > mayor:
        mayor = n

    if n < menor:
        menor = n
    
for l in range(mayor, menor -1):
        print(l)






promedio=suma/tam
print(lista)

print(suma)
print(promedio)
print(mayor,'numero mayor')
print(menor,'numero menor')

for l in range(mayor, menor -1):
        print(l)



