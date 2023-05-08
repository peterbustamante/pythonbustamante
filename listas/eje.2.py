#llenar una lista con numeros aleatorios (reales con un decimal) que represente
#calificaciones de un curso .
#se evalua de 05.
#el curso puede tener entre 20 y 30 aprendise.

import random

calificaciones=[round(random.random()*5,2) for x in range(random.randint(20,31))]

print(calificaciones)
#hallar
#genere lista nuevas para los aprobados y reprobados (se aprueba con 3)
resultado=["aprobado" if x>3 else 0 for x in calificaciones]
print(resultado)

