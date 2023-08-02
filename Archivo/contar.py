#cuantas letras tiene cada linea del hino de soacha escribir la respuesta en otro archvo
try:
    arch=open('C:\\pythonbustamante\\Archivo\\himno.txt', 'r',encoding='utf-8')
    cont=1
    linea=arch.readline()
    caracter=0

    while linea !='':
        print(f'{linea}{caracter}')
        linea=arch.readline()
        for i in linea:
            caracter+=1



except IOError as e:
    print(e)