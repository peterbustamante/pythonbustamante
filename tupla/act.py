#realiza una tupla de un valor 100 con rango de 5
import random
n=random.randint(5,15)
t=()
for i in range(n):
    m=random.randrange(100)
    t+=(m,)
print(t)
print(t//2)
