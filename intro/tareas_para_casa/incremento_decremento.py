n1 = int(input("escribe el numero con el que se desea empesar :"))
n2 = int(input("escribe el numero con el que se desea terminar :"))
n3 = int(input("escribe el numero con el que se desea incrementar o decrementar :"))
n = int(input("escribe el numero con el que se desea saber sus multiplos "))


for i in range(n1, n2, n3):
    if i % n == 0:
        print(f'{i} es multiplo de {n}')
    else:
        print(i)
