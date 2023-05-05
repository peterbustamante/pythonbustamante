import random
lista1=[]
lista2=[]
cuadrado=[]
suma1=0
suma2=0
promedio=0
mayor=0
menor=101
tam=random.randint(10,20)
for i in range(tam):
    num=random.randrange(100)
    lista1.append(num)
    suma1+= num
    n= num
    if n > mayor:
        mayor = n


    if n < menor:
        menor = n
for i in range(tam):
    num=random.randrange(100)
    lista2.append(num)
    suma2+= num
    n= num
    if n > mayor:
        mayor = n

    if n < menor:
        menor = n

print(lista1)
print(lista2)
print (f"El menor de las dos filas es: {menor}")
print (f"El mayor de las dos filas es: {mayor}")
print(f"las suma de los numeros de la lista1 es: {suma1} ")
print(f"las suma de los numeros de la lista2 es: {suma2} ")
if suma1 > suma2 :
    print('la suma1 es mayor que suma2')
else:
    print('la suma2 es mayor que suma1')