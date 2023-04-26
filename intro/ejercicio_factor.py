num = 0
mod = 0

while mod == 0:
    num1 = int(input("ingrese el numero :"))
    num2 = int(input("ingrese el numero :"))
    mod = num1 % num2
    print(f'{num1} no es dividible de {num2} vuelva a igresar los numeros')
print(f"{num1} es divisible de {num2}")
