#hallar hipotenusa un triangulo
import Matematica as math

a=int(input("ingrese valor de cateto a :"))
b=int(input("ingrese valor de cateto b :"))
#primero con la funcion xpnt se eleva los dos valores para sumar sus resultados
#con el nRoot sacamos el cuadrado al resultado de la suma, dando resultado a la ipotenusa
h=math.nRoot(math.xpnt([a])+math.xpnt([b]))

print("el tamaño de la hipotenusa es :",h)