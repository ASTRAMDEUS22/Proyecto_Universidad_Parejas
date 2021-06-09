'''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                         Creadores:                            #
#                                                               #
#                     Josthin Soto Sánchez                      #
#                     Axel Flores Lara                          #
#                                                               #
#                          Grupo 4                              #
#                                                               #
#                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
'''
#BIBLIOTECAS A USAR
import pygame
import random

pygame.init()


#PANTALLA
Largo , Alto = 1366,768


SCREEN = pygame.display.set_mode((Largo,Alto))







icono = pygame.image.load("imagenes_adicionales/logo LOL.png")
pygame.display.set_icon(icono)

#FONDO ANIMADO
fondo = pygame.image.load("Fondo_juego/fondo experimental.png").convert()

#COLORES
BLANCO = (255,255,255)
MORADO_LINDO = (39,22,56)


#Música de fondo
pygame.mixer.music.load('musica/Four brave Champios-theme.ogg')
pygame.mixer.music.play(-1)

#FONDO DE LA PANTALLA


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
            self.acceleracion_inicialX = -15

        # MOVIMIENTO HACIA LA DERECHA
        if teclas[pygame.K_d]:
            self.acceleracion_inicialX = 15

        # MOVIMIENTO HACIA LA ARRIBA
        if teclas[pygame.K_w]:
            self.acceleracion_inicialY = -15

        # MOVIMIENTO HACIA LA ABAJO
        if teclas[pygame.K_s]:
            self.acceleracion_inicialY = 15

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
        if self.rect.bottom > 650:
            self.rect.bottom = 650

#_______________________________________________CLASE ENEMIGO__________________________________________________________#

class Enemigo(pygame.sprite.Sprite):
    global spawn_X
    global spawn_Y
    # Sprite del barco
    def __init__(self):
        # Se hereda el init de la clase Sprite de pygame
        super().__init__()
        # La bala/rectangulo
        self.image = pygame.image.load("imagenes_adicionales/bomba_class1.png").convert()
        self.image.set_colorkey("black")

        # Se obtiene el rectangulo
        self.rect = self.image.get_rect()
        # ACOMODAR EL RECTANGULO/CENTRO
        self.rect.center = (Largo // 4, Alto // 4)
        self.rect.x = random.randrange(1,100)
        self.rect.y = random.randrange(1,Alto)

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
        elif self.rect.bottom >= 650:#CON ESTE LA BALA SUBE HACIA LA DERECHA
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


class Enemigo2(pygame.sprite.Sprite):
    global spawn_X
    global spawn_Y
    # Sprite del barco
    def __init__(self):
        # Se hereda el init de la clase Sprite de pygame
        super().__init__()
        # La bala/rectangulo
        self.image = pygame.image.load("imagenes_adicionales/bomba_class2.png").convert()
        self.image.set_colorkey("black")

        # Se obtiene el rectangulo
        self.rect = self.image.get_rect()
        # ACOMODAR EL RECTANGULO/CENTRO
        self.rect.center = (Largo // 4, Alto // 4)
        self.rect.x = random.randrange(1,100)
        self.rect.y = random.randrange(1,Alto)

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
        elif self.rect.bottom >= 650:#CON ESTE LA BALA SUBE HACIA LA DERECHA
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

class Enemigo3(pygame.sprite.Sprite):
    global spawn_X
    global spawn_Y
    # Sprite del barco
    def __init__(self):
        # Se hereda el init de la clase Sprite de pygame
        super().__init__()
        # La bala/rectangulo
        self.image = pygame.image.load("imagenes_adicionales/bomba_class3.png").convert()
        self.image.set_colorkey("black")

        # Se obtiene el rectangulo
        self.rect = self.image.get_rect()
        # ACOMODAR EL RECTANGULO/CENTRO
        self.rect.center = (Largo // 4, Alto // 4)
        self.rect.x = random.randrange(1,100)
        self.rect.y = random.randrange(1,Alto)

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
        elif self.rect.bottom >= 650:#CON ESTE LA BALA SUBE HACIA LA DERECHA
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
Enemigo_1 = pygame.sprite.Group()
Enemigo_2 = pygame.sprite.Group()
Enemigo_3 = pygame.sprite.Group()

#TEMPORIZADOR PARA EL JUEGO
Contador = 0

def mostrar_texto(pantalla,fuente,texto,color,dimensiones,x,y):
    tipo_fuente = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_fuente.render(texto, True, color)
    rectangle = superficie.get_rect()
    rectangle.center((500),(600))
    pantalla.blit(superficie, rectangle)




#MOSTRAR CONTADOR EN PANTALLA

#SPRITE ENEMIGOS
Bullets = Enemigo()
Enemigo_1.add((Bullets))

Bullets2 = Enemigo2()
Enemigo_2.add((Bullets2))

Bullets3 = Enemigo3()
Enemigo_3.add((Bullets3))
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

#FUENTES

Fuente_texto = pygame.font.Font(None,19)



def actualizacionPantalla():
    global cuentaPasos
    global x
    #COLOR DE FONDO
    SCREEN.fill(MORADO_LINDO)
    #UBICACION DE LOS TEXTOS EN LA PANTALLA
    SCREEN.blit(miTexto2, (100, 700))
    SCREEN.blit(miTexto,(250,700))
    SCREEN.blit(miTexto3,(600,700))
    SCREEN.blit(miTexto4,(800,700))

    #FONDO EN MOVIMIENTO
    x_bucle = x % fondo.get_rect().width
    SCREEN.blit(fondo,(x_bucle - fondo.get_rect().width,0))
    if x_bucle < Largo:
        SCREEN.blit(fondo,(x_bucle,0))
    x -= 1
    pygame.draw.line(SCREEN, BLANCO, (0, 650), (1366, 650), 11)

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
aux_Tiempo = 1
while Dios:
#________FPS________________________________________________________________________________________________
    RELOJ.tick(100)
    Tiempo = pygame.time.get_ticks()//1000
    #PUNTAJES
    Puntaje_level1 = Tiempo
    Puntaje_level2 = Tiempo*3
    Puntaje_level3 = Tiempo*5



    if aux_Tiempo == Tiempo:
        aux_Tiempo += 1

    #TEXTOS EN LA PANTALLA
    miTexto = Fuente_texto.render(str(Tiempo), bool(0), (BLANCO))
    miTexto2 = Fuente_texto.render(("TEMPORIZADOR   :"), bool(0), (BLANCO))
    miTexto3 = Fuente_texto.render(("PUNTAJE   :"), bool(0), (BLANCO))
    miTexto4 = Fuente_texto.render(str(Puntaje_level1), bool(0), (BLANCO))
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

    #ALEATORIOS ARRIBA-ABAJO-DERECHA-IZQUIERDA
    Up_down_direction = random.randint(1, 2)
    Right_left_direction = random.randint(1, 2)
    #VALORES DE LOS EJES X y Y
    Direccion_aleatoria_X = random.randint(4, 8)
    Direccion_aleatoria_Y = random.randint(4, 8)


#___________________________________________ZONA DE VENTANA________________________________________________#
    #ACTUALIZACION DE LA VENTANA
    pygame.display.update()

    actualizacionPantalla()

    # Actualizar los sprites
    sprites.update()
    Enemigo_1.update()

    Enemigo_2.update()

    Enemigo_3.update()

    #COLISIONES
    Colission_1 = pygame.sprite.spritecollide(Jugador, Enemigo_1, True)
    Colission_2 = pygame.sprite.spritecollide(Jugador, Enemigo_2, True)
    Colission_3 = pygame.sprite.spritecollide(Jugador, Enemigo_3, True)




    # PERSONALIZACION

    sprites.draw(pantalla)

    Enemigo_1.draw(pantalla)
    Enemigo_2.draw(pantalla)
    Enemigo_3.draw(pantalla)

    # REFRESCA LA PANTALLA
    pygame.display.flip()




pygame.quit()
