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

for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
listam=lista
print(listam)
for i in range(tam):
    for j in range(i+1,tam):
        if listam[j]>listam[i]:
            aux=listam[i]
            listam[i]=listam[j]
            listam[j]=aux
print(listam)            



if tam % 2 !=0:
  m= (tam//2)
  print('la mediana es :',listam[m])
else:
       m= (tam//2)
       m= (listam[m-1])+(listam[m])
       m/=2
       print('la mediana es :',m)
       
n=int(input('escriba numero: '))
cont =0
pos =0
for i in range(len(lista)):
    if n == lista[i] :
        cont+=1
        print("en la pocicion",)
        
           
if cont !=0:
     print(f"El numero {n} si esta en la lista")
     print(f'el numero esta repetido {cont} veces')
