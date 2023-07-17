# from math import sqrt

# a= int(input("ingresar numero :"))
# b= int(input("ingresar numero :"))
# c= int(input("ingresar numero :"))

# cuadratica1= (b**2)-(4*a*c)
# cuadratica2= (-b)
# cuadratica3=(2*a)
# raiz=sqrt(cuadratica1)

# suma=((cuadratica2 + raiz)/cuadratica3)
# resta=((cuadratica2 - raiz)/cuadratica3)

# print(suma,resta)

from math import sqrt
try:
    a= int(input("ingresar numero del valor a: "))
    b= int(input("ingresar numero del valor b: "))
    c= int(input("ingresar numero del valor c: "))
except ValueError:
    print("toca ingresar numeros")
try:
    cuadratica1= (b**2)-(4*a*c)
    cuadratica2= (-b)
    cuadratica3=(2*a)
    raiz=sqrt(cuadratica1)

    suma=((cuadratica2 + raiz)/cuadratica3)
    resta=((cuadratica2 - raiz)/cuadratica3)
    print(f'la suma es {suma},la resta es {resta}')

except ValueError:
    print("el numero es negativo")

except ZeroDivisionError:
    print("la division es entre cero")