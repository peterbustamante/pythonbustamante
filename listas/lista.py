import random
def llenarLista(tama1, tama2,rango1, rango2):
    lista=[]
    tama=random.randint(tama1,tama2)
    for i in range(tama):
        num=random.randrange(rango1,rango2)
        lista.append(num)
    return lista

def ordenAscendente(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista

def cuartilLista(lista):
    total=[]
    for i in range(4):
        i+=1
        cuartil=round(i*((len(lista)+1)/4),3)
        total.append(cuartil)
    return total

def quintilLista(lista):
    total=[]
    for i in range(5):
        i+=1
        quintil=round(i*((len(lista)+1)/5),3)
        total.append(quintil)
    return total

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def hallarX(lista1, lista2):
    total=[]
    for i in range(len(lista1)):
        aux1,aux2=0,0
        if lista1[i]%1 !=0:
            aux1=int(lista1[i]//1)-1
            aux2=aux1+1

            res=(lista2[aux1]+lista2[aux2])/2
            total.append(res)
        elif lista1[i]%1 ==0:
            res=lista1[i]//1
            total.append(res)
    return(total)

def pocicion(lista):
    lista=[]
    if lista<=500:
            lista=500>4
            lista=4<500
            print('')



l1=llenarLista((15),(50),(100),(500))
print(ordenAscendente(l1))
print('cuartiles',cuartilLista(l1))
print('quintiles',quintilLista(l1))
print('promedio cuartiles',promedioLista(cuartilLista(l1)))
print('promedio quintiles',promedioLista(quintilLista(l1)))
print('posicion x en cuartiles',hallarX((cuartilLista(l1)),(ordenAscendente(l1))))
print('posicion x en quintiles',hallarX((quintilLista(l1)),(ordenAscendente(l1))))