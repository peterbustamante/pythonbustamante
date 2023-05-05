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
    num=random.randrange(10)
    lista.append(num)
    suma+= num
    n= num
    if n > mayor:
        mayor = n

    if n < menor:
        menor = n


promedio=suma/tam
print(lista)

print('suma :',suma)
print('promedio :',promedio)
print('numero mayor es :',mayor)
print('numero menor es:',menor)

lista.sort()
if tam % 2 !=0:
    m= (tam//2)
    print('la mediana es :',m)
else:
    m= (tam//2)
    m= (lista[m-1])+(lista[m])
    m/=2
    print('la mediana es :',m)

print(lista)
p=0
cont=0
cont=0
moda2=0
while True:
    moda = lista[p]

    p+=1

    if moda>= 0:
        moda2=moda+1
        if moda2 >= moda:
            cont+=1
        else:
            cont=0


    print(moda,moda2,cont)











