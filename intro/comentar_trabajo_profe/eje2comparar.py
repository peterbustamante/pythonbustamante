import random
lista1=[]
lista2=[]
cuadrado=[]
suma1=0
suma2=0
promedio=0
mayor=0
menor=101
t1,t2=0,0
imp1,par1,imp2,par2=0,0,0,0
tam1=random.randint(10,20)
tam2=random.randint(10,20)

for i in range(tam1):
    num=random.randrange(100)
    lista1.append(num)
    suma1+= num
    n= num
    if n > mayor:
        mayor = n

 
prom1=suma1//tam1
t1 =tam1

if n < menor:
        menor = n

for i in range(tam2):
    num=random.randrange(100)
    lista2.append(num)
    suma2+= num
    n= num

if n > mayor:
        mayor = n

if n < menor:
        menor = n

prom2=suma2//tam2
t2 = tam2
prom12=(suma2+suma1)//(t1+t2)



    



print(tam1)
print('fila 1 :',lista1)
print(tam2)
print('fila 2 :',lista2)
print (f"El menor de las dos filas es: {menor}")
print (f"El mayor de las dos filas es: {mayor}")
print(f"las suma de los numeros de la fila 1 es: {suma1} ")
print(f"las suma de los numeros de la fila 2 es: {suma2} ")




if suma1 > suma2 :
    print('la suma1 es mayor que suma2')
else:
    print('la suma2 es mayor que suma1')
print(f'el promedio de la fila 1 es :{prom1}')
print(f'el promedio de la fila 2 es :{prom2}')
print(f'el promedio de ambas filas es :{prom12}')
print(f'el promedio de las dos filas es :{prom12}')
if prom1 > prom2 :
    if prom1 > prom12:
        print("el promedio de fila 1 es el mayor ")
    else:
        print("el promedio de fila 12 es el mayor ")
else:
    if prom2>prom12:
         print("el promedio de fila 2 es el mayor ")
    else:
        print("el promedio de fila 12 es el mayor ")

for i in range(tam1):
    if lista1[i]%2 == 0 :
     par1+=1
    else:
        imp1+=1
for i in range(tam2):
    if lista2[i]%2 == 0 :
     par2+=1
    else:
        imp2+=1        
     
print(par1,imp1)
print(par2,imp2)   

if par1>par2:
    print("flia 1 tiene mayor cantidad de pares :",par1)
else:
    print("flia 2 tiene mayor cantidad de pares :",par2)
if par1>par2:
    print("flia 1 tiene mayor cantidad de pares :",imp1)
else:
    print("flia 2 tiene mayor cantidad de impares :",imp2) 
