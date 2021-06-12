#BIBLIOTECAS A USAR
import pygame, sys
from pygame.locals import *
import random
import pygame


#PANTALLAS DE JUEGO

Largo_2 = 1366
Alto_2 = 768

#CONTROL DE FPS/PESTAÑA ABIERTA
Clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("PIRATES IN THE SKY")
SCREEN = pygame.display.set_mode((1366,768),0,32)
SCREEN_Menu = pygame.display.set_mode((1366,768),0,32)
Screen_Welcome = pygame.display.set_mode((1366,768),0,32)
#FUENTES
font = pygame.font.Font (None, 30)
font_menu = pygame.font.Font(None,60)
font_buttons = pygame.font.Font(None,12)
#MUSICA/EFECTOS


Metalic_sound = pygame.mixer.Sound('musica/Sonido colision (mp3cut.net).ogg')

# COLORES
BLANCO = (255, 255, 255)
MORADO_LINDO = (39, 22, 56)

#VIDA DEL JUGADOR
Health = 3

#FONDO DEL JUEGO
fondo = pygame.image.load("Fondo_juego/desert better.jpg").convert()
fondo_Menu = pygame.image.load("Fondo_juego/Sky_ship2.jpg").convert()
#FUENTE DE TEXTO Y TAMAÑO DE LETRA
Fuente_texto = pygame.font.Font(None, 19)

#pantalla de no se que
pantalla = pygame.display.set_mode((Largo_2, Alto_2))

#X XD
x = 0




def draw_text(text, font, color, surface,x,y):
    textobjet = font.render(text, 1, color)
    textrect = textobjet.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobjet, textrect)

#VARIABLE PARA ACTIVAR EL BOTON
click = False

click_menu = False
Menu = False
def Welcome_Window():
    click_menu = False
    while True:

        # VENTANA
        pantalla.fill((54,45,45))
        draw_text("WELCOME TO PIRATES IN THE SKY", font, (0, 0, 0), pantalla, 520, 70)
        draw_text("Nivel 1", font, (0, 0, 0), pantalla, 110, 200)
        # Detectar el click del mouse
        mx, my = pygame.mouse.get_pos()

        # BOTON
        Button_Welcome = pygame.Rect(50, 200, 50, 50)

        if Button_Welcome.collidepoint((mx, my)):
            if click_menu:
                Menu_juego()

        pygame.draw.rect(pantalla, (0, 255, 0), Button_Welcome)


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
                    click_menu = True
        pygame.display.update()

def Menu_juego():
    pygame.mixer.music.load('musica/Imposible TSH remix.ogg')
    pygame.mixer.music.play(0)
    Menu = True
    click = False
    while Menu:


        #VENTANA
        SCREEN_Menu.blit(fondo_Menu,(1,1))
        #SCREEN_Menu.blit(fondo, (0, 0))
        draw_text("THE PIRATES IN THE SKY", font,(0,0,0), pantalla,520,70)
        draw_text("Nivel 1", font, (0, 0, 0), pantalla, 110, 200)
        #Detectar el click del mouse
        mx,my = pygame.mouse.get_pos()


        #BOTON
        Button_1 = pygame.Rect(50,200,50,50)
        Button_2 = pygame.Rect(50,400,50,50)
        Button_3 = pygame.Rect(50, 600, 50, 50)
        if Button_1.collidepoint((mx,my)):
            if click:
                Nivel_Uno()
        elif Button_2.collidepoint((mx,my)):
            if click:
                Nivel_Dos()
        elif Button_3.collidepoint((mx,my)):
            if click:
                Nivel_Tres()
        pygame.draw.rect(pantalla,(0,255,0),Button_1)
        pygame.draw.rect(pantalla, (255, 0, 0), Button_2)
        pygame.draw.rect(pantalla, (0, 0, 255), Button_3)

        for event in pygame.event.get():
            click = False
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

        pygame.display.update()
        Clock.tick(60)

def Nivel_Uno():
    running = True
    pygame.mixer.music.load('musica/Remix Four brave champions.ogg')
    pygame.mixer.music.play(0)
    global x
    while running:

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
                self.rect.center = (Largo_2 // 2, Alto_2 // 2)
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
                if self.rect.right > Largo_2:
                    self.rect.right = Largo_2

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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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

        # _____________________________________________CREACION DE LA VENTANA_____________________________________________________#
        pygame.init()
        pantalla = pygame.display.set_mode((Largo_2, Alto_2))

        pygame.display.set_caption("¡¡THE PIRATES IN THE SKY!!")

        clock = pygame.time.Clock()

        # _______________________________________________SPRITES______________________________________________________________

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

        # VARIABLES PARA EL BUCLE DE LA PANTALLA
        x = 0

        # CENTRO DE FPS
        RELOJ = pygame.time.Clock()

        # FUENTES
        Fuente_texto = pygame.font.Font(None, 19)

        #BOTONES
        Button_Menu = pygame.Rect(100,630,60,20)

        # BUCLE PARA LA VENTANA
        Dios = True

        aux_Tiempo = 1
        # VIDA DEL JUGADOR
        Health = 3

        def actualizacionPantalla():
            global x

            # COLOR DE FONDO
            SCREEN.fill(MORADO_LINDO)

            # UBICACION DE LOS TEXTOS EN LA PANTALLA
            SCREEN.blit(miTexto2, (50, 680))
            SCREEN.blit(miTexto, (220, 680))
            SCREEN.blit(miTexto3, (50, 720))
            SCREEN.blit(miTexto4, (220, 720))
            SCREEN.blit(Life_counter, (1000, 700))
            SCREEN.blit(Player_life, (1200, 700))

            if Health == 0 or Tiempo >= 60:
                #SCREEN.blit(Texto_fin_del_juego, (700, 700))
                Gamer_over()
            Linea_divisora = pygame.draw.line(SCREEN, BLANCO, (0, 650), (1366, 650), 20)

            # FONDO EN MOVIMIENTO
            x_bucle = x % fondo.get_rect().width
            SCREEN.blit(fondo, (x_bucle - fondo.get_rect().width, 0))
            if x_bucle < Largo_2:
                SCREEN.blit(fondo, (x_bucle, 0))
            x -= 1
        while Dios:

            # ________FPS________________________________________________________________________________________________
            RELOJ.tick(100)
            Tiempo = pygame.time.get_ticks() // 1000
            # PUNTAJES
            Puntaje_level1 = Tiempo
            Puntaje_level2 = Tiempo * 3
            Puntaje_level3 = Tiempo * 5

            # CONTADOR DE TIEMPO
            if aux_Tiempo == Tiempo:
                aux_Tiempo += 1

            # TEXTOS EN LA PANTALLA
            miTexto = Fuente_texto.render(str(Tiempo), bool(0), BLANCO)
            miTexto2 = Fuente_texto.render("TEMPORIZADOR   :", bool(0), BLANCO)
            miTexto3 = Fuente_texto.render("PUNTAJE   :", bool(0), BLANCO)
            miTexto4 = Fuente_texto.render(str(Puntaje_level1), bool(0), BLANCO)
            Life_counter = Fuente_texto.render(str("VIDA DEL JUGADOR  :"), bool(0), BLANCO)
            Player_life = Fuente_texto.render(str(Health), bool(0), BLANCO)
            Texto_fin_del_juego = Fuente_texto.render("GAME OVER", bool(0), BLANCO)

            # BUCLE EN EL JUEGO
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # ALEATORIOS ARRIBA-ABAJO-DERECHA-IZQUIERDA
            Up_down_direction = random.randint(1, 2)
            Right_left_direction = random.randint(1, 2)
            # VALORES DE LOS EJES X y Y
            Direccion_aleatoria_X = random.randint(4, 9)
            Direccion_aleatoria_Y = random.randint(4, 9)

            # ___________________________________________ZONA DE VENTANA________________________________________________#
            # ACTUALIZACION DE LA VENTANA
            pygame.display.update()

            actualizacionPantalla()

            # Actualizar los sprites
            jugador.update()

            Enemigo_1.update()

            Enemigo_2.update()

            Enemigo_3.update()

            # ______________________COLISIONES______________________________________________________________________________________

            Colission_1 = pygame.sprite.groupcollide(Enemigo_1, jugador, True, False, pygame.sprite.collide_rect)

            Colission_2 = pygame.sprite.groupcollide(Enemigo_2, jugador, True, False, pygame.sprite.collide_rect)

            Colission_3 = pygame.sprite.groupcollide(Enemigo_3, jugador, True, False, pygame.sprite.collide_rect)



            # SI LA BOMBA CHOCA CON LA NAVE SE RESTA LA VIDA
            if Colission_1:
                Health -= 1

            if Colission_2:
                Health -= 1

            if Colission_3:
                Health -= 1


            # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
            jugador.draw(pantalla)
            Enemigo_1.draw(pantalla)
            Enemigo_2.draw(pantalla)
            Enemigo_3.draw(pantalla)
            pygame.draw.rect(pantalla,(255,255,255),Button_Menu)



def Nivel_Dos():
    running = True
    Musica = True
    global x
    while running:

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
                self.rect.center = (Largo_2 // 2, Alto_2 // 2)
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
                if self.rect.right > Largo_2:
                    self.rect.right = Largo_2

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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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

        # _____________________________________________CREACION DE LA VENTANA_____________________________________________________#
        pygame.init()
        pantalla = pygame.display.set_mode((Largo_2, Alto_2))

        pygame.display.set_caption("¡¡THE PIRATES IN THE SKY!!")

        clock = pygame.time.Clock()

        # _______________________________________________SPRITES______________________________________________________________

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

        # VARIABLES PARA EL BUCLE DE LA PANTALLA
        x = 0

        # CENTRO DE FPS
        RELOJ = pygame.time.Clock()

        # FUENTES
        Fuente_texto = pygame.font.Font(None, 19)



        # BUCLE PARA LA VENTANA
        Dios = True

        aux_Tiempo = 1
        # VIDA DEL JUGADOR
        Health = 3

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

            Linea_divisora = pygame.draw.line(SCREEN, BLANCO, (0, 650), (1366, 650), 20)

            # FONDO EN MOVIMIENTO
            x_bucle = x % fondo.get_rect().width
            SCREEN.blit(fondo, (x_bucle - fondo.get_rect().width, 0))
            if x_bucle < Largo_2:
                SCREEN.blit(fondo, (x_bucle, 0))
            x -= 1
        while Dios:

            # ________FPS________________________________________________________________________________________________
            RELOJ.tick(100)
            Tiempo = pygame.time.get_ticks() // 1000
            # PUNTAJES
            Puntaje_level2 = Tiempo
            Puntaje_level1 = Tiempo * 3
            Puntaje_level3 = Tiempo * 5

            # CONTADOR DE TIEMPO
            if aux_Tiempo == Tiempo:
                aux_Tiempo += 1

            # TEXTOS EN LA PANTALLA
            miTexto = Fuente_texto.render(str(Tiempo), bool(0), BLANCO)
            miTexto2 = Fuente_texto.render("TEMPORIZADOR   :", bool(0), BLANCO)
            miTexto3 = Fuente_texto.render("PUNTAJE   :", bool(0), BLANCO)
            miTexto4 = Fuente_texto.render(str(Puntaje_level1), bool(0), BLANCO)
            Life_counter = Fuente_texto.render(str("VIDA DEL JUGADOR  :"), bool(0), BLANCO)
            Player_life = Fuente_texto.render(str(Health), bool(0), BLANCO)
            Texto_fin_del_juego = Fuente_texto.render("GAME OVER", bool(0), BLANCO)

            # BUCLE EN EL JUEGO
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # ALEATORIOS ARRIBA-ABAJO-DERECHA-IZQUIERDA
            Up_down_direction = random.randint(1, 2)
            Right_left_direction = random.randint(1, 2)
            # VALORES DE LOS EJES X y Y
            Direccion_aleatoria_X = random.randint(4, 9)
            Direccion_aleatoria_Y = random.randint(4, 9)

            # ___________________________________________ZONA DE VENTANA________________________________________________#
            # ACTUALIZACION DE LA VENTANA
            pygame.display.update()

            actualizacionPantalla()

            # Actualizar los sprites
            jugador.update()

            Enemigo_1.update()

            Enemigo_2.update()

            Enemigo_3.update()

            # ______________________COLISIONES______________________________________________________________________________________

            Colission_1 = pygame.sprite.groupcollide(Enemigo_1, jugador, True, False, pygame.sprite.collide_rect)

            Colission_2 = pygame.sprite.groupcollide(Enemigo_2, jugador, True, False, pygame.sprite.collide_rect)

            Colission_3 = pygame.sprite.groupcollide(Enemigo_3, jugador, True, False, pygame.sprite.collide_rect)



            # SI LA BOMBA CHOCA CON LA NAVE SE RESTA LA VIDA
            if Colission_1:
                Health -= 1

            if Colission_2:
                Health -= 1

            if Colission_3:
                Health -= 1

            # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
            jugador.draw(pantalla)
            Enemigo_1.draw(pantalla)
            Enemigo_2.draw(pantalla)
            Enemigo_3.draw(pantalla)

def Nivel_Tres():
    running = True
    Musica = True
    global x
    while running:

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
                self.rect.center = (Largo_2 // 2, Alto_2 // 2)
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
                if self.rect.right > Largo_2:
                    self.rect.right = Largo_2

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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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
                self.rect.center = (Largo_2 // 4, Alto_2 // 4)
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
                elif self.rect.right >= Largo_2:
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

        # _____________________________________________CREACION DE LA VENTANA_____________________________________________________#
        pygame.init()
        pantalla = pygame.display.set_mode((Largo_2, Alto_2))

        pygame.display.set_caption("¡¡THE PIRATES IN THE SKY!!")

        clock = pygame.time.Clock()

        # _______________________________________________SPRITES______________________________________________________________

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

        # VARIABLES PARA EL BUCLE DE LA PANTALLA
        x = 0

        # CENTRO DE FPS
        RELOJ = pygame.time.Clock()

        # FUENTES
        Fuente_texto = pygame.font.Font(None, 19)



        # BUCLE PARA LA VENTANA
        Dios = True

        aux_Tiempo = 1
        # VIDA DEL JUGADOR
        Health = 3

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

            Linea_divisora = pygame.draw.line(SCREEN, BLANCO, (0, 650), (1366, 650), 20)

            # FONDO EN MOVIMIENTO
            x_bucle = x % fondo.get_rect().width
            SCREEN.blit(fondo, (x_bucle - fondo.get_rect().width, 0))
            if x_bucle < Largo_2:
                SCREEN.blit(fondo, (x_bucle, 0))
            x -= 1
        while Dios:

            # ________FPS________________________________________________________________________________________________
            RELOJ.tick(100)
            Tiempo = pygame.time.get_ticks() // 1000
            # PUNTAJES

            Puntaje_level1 = Tiempo * 5

            # CONTADOR DE TIEMPO
            if aux_Tiempo == Tiempo:
                aux_Tiempo += 1

            # TEXTOS EN LA PANTALLA
            miTexto = Fuente_texto.render(str(Tiempo), bool(0), BLANCO)
            miTexto2 = Fuente_texto.render("TEMPORIZADOR   :", bool(0), BLANCO)
            miTexto3 = Fuente_texto.render("PUNTAJE   :", bool(0), BLANCO)
            miTexto4 = Fuente_texto.render(str(Puntaje_level1), bool(0), BLANCO)
            Life_counter = Fuente_texto.render(str("VIDA DEL JUGADOR  :"), bool(0), BLANCO)
            Player_life = Fuente_texto.render(str(Health), bool(0), BLANCO)
            Texto_fin_del_juego = Fuente_texto.render("GAME OVER", bool(0), BLANCO)

            # BUCLE EN EL JUEGO
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # ALEATORIOS ARRIBA-ABAJO-DERECHA-IZQUIERDA
            Up_down_direction = random.randint(1, 2)
            Right_left_direction = random.randint(1, 2)
            # VALORES DE LOS EJES X y Y
            Direccion_aleatoria_X = random.randint(4, 9)
            Direccion_aleatoria_Y = random.randint(4, 9)

            # ___________________________________________ZONA DE VENTANA________________________________________________#
            # ACTUALIZACION DE LA VENTANA
            pygame.display.update()

            actualizacionPantalla()

            # Actualizar los sprites
            jugador.update()

            Enemigo_1.update()

            Enemigo_2.update()

            Enemigo_3.update()

            # ______________________COLISIONES______________________________________________________________________________________

            Colission_1 = pygame.sprite.groupcollide(Enemigo_1, jugador, True, False, pygame.sprite.collide_rect)

            Colission_2 = pygame.sprite.groupcollide(Enemigo_2, jugador, True, False, pygame.sprite.collide_rect)

            Colission_3 = pygame.sprite.groupcollide(Enemigo_3, jugador, True, False, pygame.sprite.collide_rect)

            #Space_ship_collision = pygame.sprite.spritecollide(Jugador, Enemigo_1, True)

            # SI LA BOMBA CHOCA CON LA NAVE SE RESTA LA VIDA
            if Colission_1:
                Health -= 1

            if Colission_2:
                Health -= 1

            if Colission_3:
                Health -= 1

            # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
            jugador.draw(pantalla)
            Enemigo_1.draw(pantalla)
            Enemigo_2.draw(pantalla)
            Enemigo_3.draw(pantalla)

click_Menu = False
#VENTANA DEL GAMER OVER
def Gamer_over():
    running = True

    pygame.mixer.music.load('musica/Arcangel two steps from hell.ogg')
    pygame.mixer.music.play(0)
    while running:
        click_Menu = False
        SCREEN_Menu.fill((MORADO_LINDO))
        draw_text("¡GAMER OVER!", font_menu, (255, 255, 255), SCREEN_Menu, 520, 300)
        mx, my = pygame.mouse.get_pos()

        # BOTON
        Button_Menu = pygame.Rect(50, 200, 50, 50)
        #Button_2 = pygame.Rect(50, 400, 50, 50)
        #Button_3 = pygame.Rect(50, 600, 50, 50)
        pygame.draw.rect(SCREEN_Menu, (0, 255, 0), Button_Menu)




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
                    click_Menu = True

        if Button_Menu.collidepoint((mx, my)):
            if click_Menu:
                Menu_juego()

        pygame.display.update()
        Clock.tick(60)














Welcome_Window()
