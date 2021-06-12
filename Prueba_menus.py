#BIBLIOTECAS A USAR
import pygame, sys
from pygame.locals import *
import random

#PANTALLAS DE JUEGO
Alto = 500
Largo = 500
Alto_2 = 1366
Largo_2 = 768

#CONTROL DE FPS/PESTAÑA ABIERTA
Clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("PRUEBA DE MENUS")
SCREEN = pygame.display.set_mode((500,500),0,32)

#FUENTES
font = pygame.font.Font (None, 30)

Metalic_sound = pygame.mixer.Sound('musica/Sonido colision (mp3cut.net).ogg')

# COLORES
BLANCO = (255, 255, 255)
MORADO_LINDO = (39, 22, 56)

#VIDA DEL JUGADOR
Health = 3

#FONDO DEL JUEGO
fondo = pygame.image.load("Fondo_juego/fondo experimental.png").convert()

#FUENTE DE TEXTO Y TAMAÑO DE LETRA
Fuente_texto = pygame.font.Font(None, 19)

#pantalla de no se que
pantalla = pygame.display.set_mode((Largo_2, Alto_2))

def draw_text(text, font, color, surface,x,y):
    textobjet = font.render(text, 1, color)
    textrect = textobjet.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobjet, textrect)

#VARIABLE PARA ACTIVAR EL BOTON
click = False
def main_menu():
    while True:


        #VENTANA
        SCREEN.fill((255,255,255))
        draw_text("Main_menu", font,(0,0,0), SCREEN,20,20)
        #Detectar el click del mouse
        mx,my = pygame.mouse.get_pos()


        #BOTON
        Button_1 = pygame.Rect(50,200,300,50)
        Button_2 = pygame.Rect(50,400,300,50)
        if Button_1.collidepoint((mx,my)):
            if click:
                Nivel_Uno()
        if Button_2.collidepoint((mx,my)):
            if click:
                Options()

        pygame.draw.rect(SCREEN,(0,255,0),Button_1)
        pygame.draw.rect(SCREEN, (255, 0, 0), Button_2)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    Nivel_Uno()
        pygame.display.update()
        Clock.tick(60)

def Nivel_Uno():
    running = True
    Musica = True
    while running:
        # TIEMPO
        Tiempo = pygame.time.get_ticks() // 1000
        #PUNTAJE EN EL JUEGO
        Puntaje_level1 = Tiempo
        # MUSICA A UTILIZAR
        if Musica:
            pygame.mixer.music.load('musica/Remix Four brave champions.ogg')
            pygame.mixer.music.play(0)



        SCREEN2 = pygame.display.set_mode((1366, 768), 0, 32)

        SCREEN2.fill((255,255,255))
        draw_text("Juego", font, (0, 0, 0), SCREEN2, 20, 20)

        # TEXTOS EN LA PANTALLA
        miTexto = Fuente_texto.render(str(Tiempo), bool(0), BLANCO)
        miTexto2 = Fuente_texto.render("TEMPORIZADOR   :", bool(0), BLANCO)
        miTexto3 = Fuente_texto.render("PUNTAJE   :", bool(0), BLANCO)
        miTexto4 = Fuente_texto.render(str(Puntaje_level1), bool(0), BLANCO)
        Life_counter = Fuente_texto.render(str("VIDA DEL JUGADOR  :"), bool(0), BLANCO)
        Player_life = Fuente_texto.render(str(Health), bool(0), BLANCO)
        Texto_fin_del_juego = Fuente_texto.render("GAME OVER", bool(0), BLANCO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        Clock.tick(60)

    class Pirate_ship(pygame.sprite.Sprite):
        # Sprite del barco
        def __init__(self):
            # Se hereda el init de la clase Sprite de pygame
            super().__init__()
            # La bala/rectangulo
            self.image = pygame.image.load("Imagenes_personajes/Barcos estatico.png").convert()
            self.image.set_colorkey("black")

            # Se obtiene el rectangulo
            self.rect = self.image.get_rect()
            # ACOMODAR EL RECTANGULO/CENTRO
            self.rect.center = (Largo // 2, Alto // 2)
            # VELOCIDAD INICIAL DE LA NAVE
            self.acceleracion_inicialX = 0
            self.acceleracion_inicialY = 0
            # VIDA DE LA NAVE

        # ______________________________________MOVIMIENTO NAVE 2___________________________________________#
        def update(self):  # el UPDATE esta heredado, si se utiliza otra cosa dejará de funcionar
            # SE ACTUALIZA EL RECTANGULO EN CADA BUCLE

            # VELOCIDAD PREDETERMINADA CADA VUELTA DEL BUCLE si no se pulsa algo
            self.acceleracion_inicialX = 0
            self.acceleracion_inicialY = 0
            # Mantiene las teclas pulsadas
            teclas = pygame.key.get_pressed()

            # MOVIMIENTO HACIA LA IZQUIERDA
            if teclas[pygame.K_a]:
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

            # ACTUALIZA LA VELOCIDAD DEL PJ
            self.rect.x += self.acceleracion_inicialX
            self.rect.y += self.acceleracion_inicialY

            # LIMITAR EL BORDE  IZQUIERDO
            if self.rect.left < 0:
                self.rect.left = 0

            # LIMITAR EL BORDE DERECHO
            if self.rect.right > Largo:
                self.rect.right = Largo

            # LIMITAR EL BORDE  SUPERIOR
            if self.rect.top < 0:
                self.rect.top = 0

            # LIMITAR EL BORDE INFERIOR
            if self.rect.bottom > 650:
                self.rect.bottom = 650
    # _______________________________________________CLASE ENEMIGO__________________________________________________________#

    class Enemigo(pygame.sprite.Sprite):

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
            self.rect.x = random.randrange(1, 100)
            self.rect.y = random.randrange(1, 100)

            self.acceleracion_inicialX = -1
            self.acceleracion_inicialY = -1

        def update(self):
            # ACTUALIZA LA VELOCIDAD DEL PJ
            self.rect.x += self.acceleracion_inicialX
            self.rect.y += self.acceleracion_inicialY

            # LIMITAR EL BORDE  IZQUIERDO
            if self.rect.left <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()

                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE DERECHO
            elif self.rect.right >= Largo:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE INFERIOR
            elif self.rect.bottom >= 650:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y


                elif Up_down_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE  SUPERIOR
            elif self.rect.top <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y


                elif Up_down_direction == 2:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y

    class Enemigo2(pygame.sprite.Sprite):

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
            self.rect.x = random.randrange(1, 100)
            self.rect.y = random.randrange(1, 100)

            self.acceleracion_inicialX = -1
            self.acceleracion_inicialY = -1

        def update(self):
            # ACTUALIZA LA VELOCIDAD DEL PJ
            self.rect.x += self.acceleracion_inicialX
            self.rect.y += self.acceleracion_inicialY

            # LIMITAR EL BORDE  IZQUIERDO
            if self.rect.left <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE DERECHO
            elif self.rect.right >= Largo:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE INFERIOR
            elif self.rect.bottom >= 650:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y

                elif Up_down_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE  SUPERIOR
            elif self.rect.top <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y


                elif Up_down_direction == 2:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y

    class Enemigo3(pygame.sprite.Sprite):

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
            self.rect.x = random.randrange(1, 100)
            self.rect.y = random.randrange(1, 100)

            self.acceleracion_inicialX = -1
            self.acceleracion_inicialY = -1

        def update(self):
            # ACTUALIZA LA VELOCIDAD DEL PJ
            self.rect.x += self.acceleracion_inicialX
            self.rect.y += self.acceleracion_inicialY

            # LIMITAR EL BORDE  IZQUIERDO
            if self.rect.left <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE DERECHO
            elif self.rect.right >= Largo:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE INFERIOR
            elif self.rect.bottom >= 650:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y


                elif Up_down_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE  SUPERIOR
            elif self.rect.top <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y


                elif Up_down_direction == 2:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y




            # LIMITAR EL BORDE DERECHO
            elif self.rect.right >= Largo:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE INFERIOR
            elif self.rect.bottom >= 650:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y


                elif Up_down_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = -Direccion_aleatoria_Y




            # LIMITAR EL BORDE  SUPERIOR
            elif self.rect.top <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y


                elif Up_down_direction == 2:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -Direccion_aleatoria_X
                    self.acceleracion_inicialY = Direccion_aleatoria_Y
                # ALEATORIOS ARRIBA-ABAJO-DERECHA-IZQUIERDA
    Up_down_direction = random.randint(1, 2)
    Right_left_direction = random.randint(1, 2)
    # VALORES DE LOS EJES X y Y
    Direccion_aleatoria_X = random.randint(4, 9)
    Direccion_aleatoria_Y = random.randint(4, 9)

    jugador = pygame.sprite.Group()
    Enemigo_1 = pygame.sprite.Group()
    Enemigo_2 = pygame.sprite.Group()
    Enemigo_3 = pygame.sprite.Group()

    Bullets = Enemigo()
    Enemigo_1.add(Bullets)

    Bullets2 = Enemigo2()
    Enemigo_2.add(Bullets2)

    Bullets3 = Enemigo3()
    Enemigo_3.add(Bullets3)
    # SPRITE JUGADOR

    Jugador = Pirate_ship()
    jugador.add(Jugador)

    # ACTUALIZACION DE LA VENTANA
    pygame.display.update()

    actualizacionPantalla()

    # Actualizar los sprites
    jugador.update()

    Enemigo_1.update()

    Enemigo_2.update()

    Enemigo_3.update()

    jugador = pygame.sprite.Group()
    Enemigo_1 = pygame.sprite.Group()
    Enemigo_2 = pygame.sprite.Group()
    Enemigo_3 = pygame.sprite.Group()

    # SPRITE ENEMIGOS
    Bullets = Enemigo()
    Enemigo_1.add(Bullets)

    Bullets2 = Enemigo2()
    Enemigo_2.add(Bullets2)

    Bullets3 = Enemigo3()
    Enemigo_3.add(Bullets3)
    # SPRITE JUGADOR

    Jugador = Pirate_ship()
    jugador.add(Jugador)
    # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
    jugador.draw(pantalla)
    Enemigo_1.draw(pantalla)
    Enemigo_2.draw(pantalla)
    Enemigo_3.draw(pantalla)




def Options():
    running = True
    while running:
        SCREEN.fill((255,255,255))
        draw_text("Opciones", font, (0, 0, 0), SCREEN, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        Clock.tick(60)
def actualizacionPantalla():
    global x

    # COLOR DE FONDO
    SCREEN.fill(MORADO_LINDO)

    # UBICACION DE LOS TEXTOS EN LA PANTALLA
    SCREEN.blit(miTexto2, (50, 700))
    SCREEN.blit(miTexto, (200, 700))
    SCREEN.blit(miTexto3, (400, 700))
    SCREEN.blit(miTexto4, (520, 700))
    SCREEN.blit(Life_counter, (1000, 700))
    SCREEN.blit(Player_life, (1200, 700))

    if Health == 0 or Tiempo >= 60:
        SCREEN.blit(Texto_fin_del_juego, (700, 700))
    Linea_divisora = pygame.draw.line(SCREEN, ((0,0,0)), (0, 650), (1366, 650), 20)

    # FONDO EN MOVIMIENTO
    x_bucle = x % fondo.get_rect().width
    SCREEN.blit(fondo, (x_bucle - fondo.get_rect().width, 0))
    if x_bucle < Largo:
        SCREEN.blit(fondo, (x_bucle, 0))
    x -= 1
main_menu()