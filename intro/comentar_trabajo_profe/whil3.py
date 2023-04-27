# num=1
# print(type(num))
# num="sena"
# print(type(num))
num = 1  # se crea variable num que sera igual a 1, para almacenar numero.

# se crea variable cont que sera igual a 0, para almacenar un contador .
cont = 0
sum = 0  # se crea variable sum que sera igual a 0, para almacenar una suma .
menor = 1000000  # se crea variable menor para almacenar el numero menor.
mayor = 0  # crea variable mayor, para almacenar el numero mayor .
while num != 0:
    num = int(input('ingrese numero'))
    cont = cont+1
    sum = sum+num
    if num > mayor:
        mayor = num
        if num < menor and num != 0:
            menor = num

print(f'fueron ingresados {cont-1} numeros')
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')
