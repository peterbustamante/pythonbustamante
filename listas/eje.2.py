#llenar una lista con numeros aleatorios (reales con un decimal) que represente
#calificaciones de un curso .
#se evalua de 05.
#el curso puede tener entre 20 y 30 aprendise.

import random
tam=(random.randint(20,31))
calificaciones=[round(random.random()*5,2) for x in range(tam)]

print(calificaciones)
#hallar
#genere lista nuevas para los aprobados y reprobados (se aprueba con 3)
resultado=[(x,"aprobado") for x in calificaciones if x>3 ]
print(resultado)
resultado2=[(x,"reprobado") for x in calificaciones if x<3 ]
print(resultado2)
# #generar lista nueva de


var=["reprobado" if x < 3 else "aprovado" for x in calificaciones]
print(var)
for q in range(tam):
    for i in range(q+1,tam):
        if calificaciones[q] > calificaciones[i]:
            calificaciones[q], calificaciones[i] = calificaciones[i], calificaciones[q]
print(calificaciones)
print(resultado)
resultado2=[(x,"reprobado") for x in calificaciones if x<3 ]
print(resultado2)

