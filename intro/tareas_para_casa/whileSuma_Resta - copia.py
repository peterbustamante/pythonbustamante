num1, num2 = 5, 5
mayor = 0
menor = 10000000000
while (num1-num2) == 0:
    print("ingresa de nuevo los numeros ")
    num1 = int(input('ingrese numero'))
    num2 = int(input('ingrese numero'))
    if (num1 < num2 or num1 > num2):
        if num1 > mayor:
            mayor = num1
            if num2 > mayor:
                mayor = num2
                print(f'{mayor-num1}es el mayor')
            else:
                print(f'{mayor-num2}es el resultado')
