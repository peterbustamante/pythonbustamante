try:
    arch=open('C:\\pythonbustamante\\Archivo\\himno.txt', 'r',encoding='utf-8')
    cont=1
    linea=arch.readline()

    while linea !='':
        print(f'{cont}{linea}')
        linea=arch.readline()

        cont+=1

except IOError as e:
    print(e)




