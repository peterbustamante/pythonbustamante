def crear_archivo(nombrearchivo):
    try:
        archivo=open(f'files\{nombrearchivo}','x')
        escribir1=input('ingrese nombre:')

        archivo.write(escribir1)
        archivo.close()

    except FileExistsError:
        print('archivo ya existente ')




nombre=input('escribir nombre del archivo  :')
crear_archivo(nombre)