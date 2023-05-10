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
# resultado=[(x,"aprobado") for x in calificaciones if x>3 ]
# print(resultado)
# resultado2=[(x,"reprobado") for x in calificaciones if x<3 ]
# print(resultado2)
# #generar lista nueva de

prom=0
prom2=0

for q in range(tam):
    for i in range(q+1,tam):
        if calificaciones[q] > calificaciones[i]:
            calificaciones[q], calificaciones[i] = calificaciones[i], calificaciones[q]
            if calificaciones[i] <=3:
                prom+=1
            if calificaciones[i] >=3:
                prom2+=1



print(calificaciones)

var=["reprobado" if x < 3 else "aprovado" for x in calificaciones]
l=4
print(var)
grupo1 =[x for x in calificaciones if 1>=x  ]
print(grupo1)
grupo2 =[x for x in calificaciones if 2>=x and x>=1 ]
print(grupo2)
grupo3 =[x for x in calificaciones if 3>=x and x>=2 ]
print(grupo3)
grupo4 =[x for x in calificaciones if 4>=x and x>=3 ]
print(grupo4)
grupo5 =[x for x in calificaciones if 5>=x and x>=4 ]
print(grupo5)
print(prom)




