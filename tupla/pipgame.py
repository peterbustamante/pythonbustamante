import pygame
run = True
width = 400
height = 100
# pygame.init es un metodo para inicializar la pantalla o la ventana, en este caso podemos ver como el metodo pygame.init() nos permite crear una ventana para que se visualice en la pantalla
pygame.init()
# El metodo pygame.display.set_mode: es un metodo que tambien se utiliza para inicializar, pero en este caso con argumentos ingresados, como las dimensiones. Como podemos ver las dimensiones que se le estan asignando como parametro ya estan inicializadas en la parte de arriba como width y height y height
screen = pygame.display.set_mode((width, height))
# El metodo pygame.font.SysFont nos permite crear un nuevo objeto de fuente a partir de un archivo, en este caso nos permite cambiar el tamaño de la letra que se va a visualizar en la nueva ventana
font = pygame.font.SysFont(None, 48)
# El método font.render nos permite representar la intesidad de una imagen / texto de dicha imagen
text = font.render("Bienvenido a pygame", True, (250, 250, 250))
# El método screen.blit nos permite dibujar una imágen sobre otra, En este caso estamos pasando la variable "text" encima de las variables width y height, esto hace que lo que se encuentre dentro de la variable "text" se muestre por encima de la ventana principal
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
#El método pygame.display.flip nos permite actualizar la superficie de visualización completa de la ventana, En este caso nos permite visualizar cualquier cambio el cual efectuar en los códigos anteriormente explicados.
pygame.display.flip()

while run:
    #El método pygame.event.get nos permite obtener eventos de la cola, En este caso guarda un estado de acciones las cuales son Pygame.quit (lo que hace es desinicializar todos los módulos de pygame), Pygame.mousebuttomup\ (lo que hace es registrar las coordenadas de la posición que presiona y suelta el mouse), Pygame.keyup (lo que hace es que sirva para trabajar con el teclado)
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            #Cuando alguna de esos eventos se cumplan la variable run será falsa, lo que significa que cambiará su estado a false, ocacionando que cierre la ventana.
            run = False
