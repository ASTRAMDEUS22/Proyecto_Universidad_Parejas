import pygame


#Iniciación de Pygame
pygame.init()

#Pantalla - ventana
W, H = 1366, 768
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('BATLE SHIP!')
icono=pygame.image.load('logo LOL.png')
pygame.display.set_icon(icono)

#Fondo del juego
fondo = pygame.image.load('fondo experimental.png').convert()

#Música de fondo
pygame.mixer.music.load('Arcangel two steps from hell.ogg')
pygame.mixer.music.play(-1)


#Personaje
quieto = pygame.image.load('Barcos estatico.png')

caminaDerecha = [pygame.image.load('Barcos piratas derecha_1.png'),
                 pygame.image.load('Barcos piratas derecha_2.png'),
                 pygame.image.load('Barcos piratas derecha_3.png'),
                 pygame.image.load('Barcos piratas derecha_4.png'),]

caminaIzquierda = [pygame.image.load('Barcos piratas izquierda_1.png'),
                   pygame.image.load('Barcos piratas izquierda_2.png'),
                   pygame.image.load('Barcos piratas izquierda_3.png'),
                   pygame.image.load('Barcos piratas izquierda_4.png'),]


x = 0
px = 583
py = 293
ancho = 40
velocidad = 2

#Control de FPS
RELOJ = pygame.time.Clock()




#Variables dirección
izquierda = False
derecha = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables globales
    global cuentaPasos
    global x

    #Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 1
    #Contador de pasos
    if cuentaPasos + 1 >= 4:
        cuentaPasos = 0
    #Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

        # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

#Bucle de acciones y controles
while ejecuta:
    #FPS
    RELOJ.tick(100)

    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opción tecla pulsada
    keys = pygame.key.get_pressed()

    #Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    #Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and px < 1232 - velocidad - ancho:
        px += velocidad
        derecha = True
        izquierda = False

    #Personaje quieto
    else:
        izquierda = False
        derecha = False

        cuentaPasos = 0

    #Tecla W - Moviemiento hacia arriba
    if keys[pygame.K_w] and py > 4:
        py -= velocidad

    #Tecla S - Moviemiento hacia abajo
    if keys[pygame.K_s] and py < 610:
        py += velocidad



    # Actualización de la ventana
    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

#Salida del juego
pygame.quit()
