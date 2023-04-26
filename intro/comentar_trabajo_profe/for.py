# se utuliza para contar hasta el numero anterior epecifico
# siempre comenzara desde 0 amenos que se especifique
# en este caso se contara desde 0 hasta 10,puesto que no indica con caul numero comenzar y indica el 10
# la variable i srea definido como todos los numeros que se desea contar
for i in range(11):
    # creamos ete comando if para espicificar que a los multiplos de 3 seran identificados
    # si el modulo de la divicion del numero de la variable i con el 3 si da 0 se ejecuta if
    if i % 3 == 0:
        # al ejecutarse if imprimira el mensaje de que es un multiplo de 3
        print(f'{i} es multiplo de 3')
# al no cumplise la fucion if de lo contrio solo imprimira el numero
    else:
        print(i)
# como indica la variable for comiensa con el numero 1, terminara hasta el numero 10 .
for j in range(1, 11):
    print(j)
# como indica la variable for comiensa con el numero 1, terminara hasta el numero 10, su tercer numero definira cuanto en cuanto hara la cuenta
# en este caso lo contara en dos en dos .
for k in range(0, 11, 2):
    print(k)
# como indica la variable for comiensa con el numero 20, terminara hasta el numero 1, su tercer numero es negativo para idicar que contara del mayor al menor
# en este caso contar 2 en 2 desde 20 hasta 0
for i in range(20, 0, -2):
    print(i)
