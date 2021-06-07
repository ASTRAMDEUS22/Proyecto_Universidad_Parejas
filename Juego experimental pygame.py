import pygame
import random

pygame.init()


#PANTALLA
Largo , Alto = 1366,768
SCREEN = pygame.display.set_mode((Largo,Alto))

#LUGAR DE APARICION DE LAS NAVES
spawn_X = random.randrange(1,180)
spawn_Y = random.randrange(1,600)
#DIRECCION DE LA BALA POSS CHOQUE
Up_down_direction = random.randint(1,3)

Right_left_direction = random.randint(1,3)

Direccion_aleatoria_X = random.randrange(1,10)
Direccion_aleatoria_Y = random.randrange(1,10)
#TITULO DE LA VENTANA




icono = pygame.image.load("imagenes_adicionales/logo LOL.png")
pygame.display.set_icon(icono)

#FONDO ANIMADO
fondo = pygame.image.load("Fondo_juego/fondo experimental.png").convert()




#Música de fondo
pygame.mixer.music.load('musica/Four brave Champios-theme.ogg')
pygame.mixer.music.play(-1)

#PERSONAJE

#___________________________________________________CLASE BARCO________________________________________________________#
class Pirate_ship(pygame.sprite.Sprite):
    #Sprite del barco
    def __init__(self):
        #Se hereda el init de la clase Sprite de pygame
        super().__init__()
        #La bala/rectangulo
        self.image = pygame.image.load("Imagenes_personajes/Barcos estatico.png").convert()
        self.image.set_colorkey("black")


        #Se obtiene el rectangulo
        self.rect = self.image.get_rect()
        #ACOMODAR EL RECTANGULO/CENTRO
        self.rect.center = (Largo // 2, Alto // 2)

        self.acceleracion_inicialX = 0
        self.acceleracion_inicialY = 0


#______________________________________MOVIMIENTO NAVE 2___________________________________________#
    def update(self): #el UPDATE esta heredado, si se utiliza otra cosa dejará de funcionar
        #SE ACTUALIZA EL RECTANGULO EN CADA BUCLE


        # VELOCIDAD PREDETERMINADA CADA VUELTA DEL BUCLE si no se pulsa algo
        self.acceleracion_inicialX = 0
        self.acceleracion_inicialY = 0
        #Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()

        #MOVIMIENTO HACIA LA IZQUIERDA
        if teclas [pygame.K_a]:
            self.acceleracion_inicialX = -10

        # MOVIMIENTO HACIA LA DERECHA
        if teclas[pygame.K_d]:
            self.acceleracion_inicialX = 10

        # MOVIMIENTO HACIA LA ARRIBA
        if teclas[pygame.K_w]:
            self.acceleracion_inicialY = -10

        # MOVIMIENTO HACIA LA ABAJO
        if teclas[pygame.K_s]:
            self.acceleracion_inicialY = 10

        #ACTUALIZA LA VELOCIDAD DEL PJ
        self.rect.x += self.acceleracion_inicialX
        self.rect.y += self.acceleracion_inicialY

        #LIMITAR EL BORDE  IZQUIERDO
        if self.rect.left < 0:
            self.rect.left = 0

        #LIMITAR EL BORDE DERECHO
        if self.rect.right > Largo:
            self.rect.right = Largo

        # LIMITAR EL BORDE  SUPERIOR
        if self.rect.top < 0:
            self.rect.top = 0

        # LIMITAR EL BORDE INFERIOR
        if self.rect.bottom > Alto:
            self.rect.bottom = Alto

#_______________________________________________CLASE ENEMIGO__________________________________________________________#

class Enemigo(pygame.sprite.Sprite):
    global spawn_X
    global spawn_Y
    # Sprite del barco
    def __init__(self):
        # Se hereda el init de la clase Sprite de pygame
        super().__init__()
        # La bala/rectangulo
        self.image = pygame.image.load("imagenes_adicionales/bomba.png").convert()
        self.image.set_colorkey("black")

        # Se obtiene el rectangulo
        self.rect = self.image.get_rect()
        # ACOMODAR EL RECTANGULO/CENTRO
        self.rect.center = (100, 300)
        self.rect.x = random.randrange(Largo - self.rect.width)
        self.rect.y = random.randrange(Alto - self.rect.height)

        self.acceleracion_inicialX = 1
        self.acceleracion_inicialY = 1

    def update(self):

        # ACTUALIZA LA VELOCIDAD DEL PJ
        self.rect.x += self.acceleracion_inicialX
        self.rect.y += self.acceleracion_inicialY

        # LIMITAR EL BORDE  IZQUIERDO
        if self.rect.left <= 0:
            if Right_left_direction == 1:#CON ESTE LA BALA BAJA HACIA LA DERECHA
                self.acceleracion_inicialX = Direccion_aleatoria_X
                self.acceleracion_inicialY = Direccion_aleatoria_Y

            elif Right_left_direction == 2:#CON ESTE LA BALA SUBE HACIA LA DERECHA
                self.acceleracion_inicialX = Direccion_aleatoria_X
                self.acceleracion_inicialY = -Direccion_aleatoria_Y



        # LIMITAR EL BORDE DERECHO
        elif self.rect.right >= Largo:
            if Right_left_direction == 1:#CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                self.acceleracion_inicialX = -Direccion_aleatoria_X
                self.acceleracion_inicialY = Direccion_aleatoria_Y

            elif Right_left_direction == 2:#CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                self.acceleracion_inicialX = -Direccion_aleatoria_X
                self.acceleracion_inicialY = -Direccion_aleatoria_Y



        # LIMITAR EL BORDE INFERIOR
        elif self.rect.bottom >= Alto:#CON ESTE LA BALA SUBE HACIA LA DERECHA
            if Up_down_direction == 1:
                self.acceleracion_inicialX = Direccion_aleatoria_X
                self.acceleracion_inicialY = -Direccion_aleatoria_Y

            elif Up_down_direction == 2:#CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                self.acceleracion_inicialX = -Direccion_aleatoria_X
                self.acceleracion_inicialY = -Direccion_aleatoria_Y



        # LIMITAR EL BORDE  SUPERIOR
        elif self.rect.top <= 0:
            if Up_down_direction == 1:#CON ESTE LA BALA BAJA HACIA LA DERECHA
                self.acceleracion_inicialX = Direccion_aleatoria_X
                self.acceleracion_inicialY = Direccion_aleatoria_Y

            elif Up_down_direction == 2:#CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                self.acceleracion_inicialX = -Direccion_aleatoria_X
                self.acceleracion_inicialY = Direccion_aleatoria_Y



#_____________________________________________CREACION DE LA VENTANA_____________________________________________________#
pygame.init()
pantalla = pygame.display.set_mode(((Largo,Alto)))
pygame.display.set_caption("The pirates in the Sky")
clock = pygame.time.Clock()


#_______________________________________________SPRITES______________________________________________________________

sprites = pygame.sprite.Group()
Enemigoss =pygame.sprite.Group()




#SPRITE ENEMIGOS
Bullets = Enemigo()
Enemigoss.add((Bullets))

Bullets2 = Enemigo()
Enemigoss.add((Bullets2))

Bullets3 = Enemigo()
Enemigoss.add((Bullets3))
'''
Bullets4 = Enemigo()
Enemigoss.add((Bullets4))

Bullets5 = Enemigo()
sprites.add((Bullets5))

Bullets6 = Enemigo()
sprites.add((Bullets6))

Bullets7 = Enemigo()
sprites.add((Bullets7))'''
#SPRITE JUGADOR

Jugador = Pirate_ship()
sprites.add((Jugador))
#____________________________________________________________________________________________________________________




#VARIABLES PARA EL MOVIMIENTO

x = 0
px = 583
py = 293
ancho = 40
velocidad = 6



#CENTRO DE FPS
RELOJ = pygame.time.Clock()

#CONTROL DE DIRECCION
izquierda = False
derecha = False

#AVANCE
cuentaPasos = 0

#MOVIMIENTO
def actualizacionPantalla():
    global cuentaPasos
    global x


    #FONDO EN MOVIMIENTO
    x_bucle = x % fondo.get_rect().width
    SCREEN.blit(fondo,(x_bucle - fondo.get_rect().width,0))
    if x_bucle < Largo:
        SCREEN.blit(fondo,(x_bucle,0))
    x -= 1
#_________________________________________NAVE SIN CLASE______________________________#
    '''
    #CONTADOR DE PASOS
    if cuentaPasos + 1 >= 4:
        cuentaPasos = 0
    #MOVIMIENTO A LA IZQUIERDA
    if izquierda:
        SCREEN.blit(caminar_izquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    #MOVIMIENTO DERECHA
    elif derecha:
        SCREEN.blit(caminar_derecha[cuentaPasos // 1],(int(px), int(py)))
        cuentaPasos += 1
    #SI NO HAY MOVIMIENTO

    else:
        SCREEN.blit(quieto,(int(px), int(py)))'''


#BUCLE PARA LA VENTANA
Dios = True

while Dios:
    #FPS
    RELOJ.tick(100)
    #LOS NUMEROS RANDOM

    #BUCLE EN EL JUEGO
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Dios = False
#_____________________________________ZONA DE TECLAS_____________________________________________#
    #OPCIÓN TECLA PULSADA
    keys = pygame.key.get_pressed()

    # FLECHA IZQUIERDA/MOVIMIENTO A LA IZQUIERDA
    if keys[pygame.K_LEFT] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    # FLECHA DERECHA/MOVIMIENTO A LA DERECHA
    elif keys[pygame.K_RIGHT] and px < 1232 - velocidad - ancho:
        px += velocidad
        derecha = True
        izquierda = False

    #BARCO QUIETO
    else:
        izquierda = False
        derecha = False

        cuentaPasos = 0

    #MOVIMIENTO HACIA ARRIBA/MOVIMIENTO HACIA ARRIBA
    if keys[pygame.K_UP] and py > 4:
        py -= velocidad
    #MOVIMIENTO HACIA ABAJO

    if keys[pygame.K_DOWN] and py < 610:
        py += velocidad

    print("--------------NUMEROS ALEATORIOS GENERADOS-------------")
    Up_down_direction = random.randint(1, 3)
    Right_left_direction = random.randint(1, 3)
    print(Up_down_direction)
    print(Right_left_direction)
    Direccion_aleatoria_X = random.randint(4, 8)
    Direccion_aleatoria_Y = random.randint(4, 8)
    print(Direccion_aleatoria_X)
    print(Direccion_aleatoria_Y)
    print("--------------NUMEROS ALEATORIOS GENERADOS-------------")

#___________________________________________ZONA DE VENTANA________________________________________________#
    #ACTUALIZACION DE LA VENTANA
    pygame.display.update()
    actualizacionPantalla()

    # Actualizar los sprites
    sprites.update()
    Enemigoss.update()

    #COLISIONES
    Colission = pygame.sprite.spritecollide(Jugador, Enemigoss, True)


    # PERSONALIZACION

    sprites.draw(pantalla)
    Enemigoss.draw(pantalla)

    # REFRESCA LA PANTALLA
    pygame.display.flip()



pygame.quit()
