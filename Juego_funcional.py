#BIBLIOTECAS A USAR
import random
import sys
import pygame
from pygame.locals import *

#PANTALLAS DE JUEGO
Largo_2 = 1366
Alto_2 = 768

#CONTROL DE FPS/PESTAÑA ABIERTA
Clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("PIRATES IN THE SKY")

#VENTANAS
SCREEN_Welcome = pygame.display.set_mode((Largo_2, Alto_2),0,32)
SCREEN_Menu = pygame.display.set_mode((Largo_2, Alto_2),0,32)
SCREEN_Level1 = pygame.display.set_mode((Largo_2, Alto_2),0,32)
SCREEN_Level2 = pygame.display.set_mode((Largo_2, Alto_2))
SCREEN_Level3 = pygame.display.set_mode((Largo_2, Alto_2),0,32)
SCREEN_Gamer_Over = pygame.display.set_mode((Largo_2, Alto_2),0,32)

#FUENTES
font_titulos = pygame.font.SysFont("Wide Latin", 30)
font_menu3 = pygame.font.SysFont("Amasis MT Pro Black",37)
font_menu2 = pygame.font.SysFont("Amasis MT Pro Black",45)
font_menu = pygame.font.SysFont("Amasis MT Pro Black",60)
font_Input = pygame.font.SysFont("Arial",20)
font_game = pygame.font.SysFont("Bodoni MT Black",40)
font_game2 = pygame.font.SysFont("Bodoni MT Black",22)
font_game3 = pygame.font.SysFont("Bodoni MT Black",32)

#MUSICA/EFECTOS
Metalic_sound = pygame.mixer.Sound('musica/Sonido colision (mp3cut.net).ogg')

# COLORES
BLANCO = (255, 255, 255)
MORADO_LINDO = (39, 22, 56)
MORADO_LINDO2 = (62,44,118)
GRIS = (60,60,60)
Cafe = (122,78,65)
Crema = (218,181,113)
Gris = (128,128,128)

#FONDO DEL JUEGO
fondo = pygame.image.load("Fondo_juego/fondo experimental.png").convert()
fondo2 = pygame.image.load("Fondo_juego/desert better.jpg").convert()
fondo3 = pygame.image.load("Fondo_juego/red-sun-between-mountains-minimal.jpg").convert()
fondo_Menu = pygame.image.load("Fondo_juego/Sky_ship2.jpg").convert()
fondo_gamerover = pygame.image.load("Fondo_juego/Broken ship.jpg").convert()
fondo_trofeos = pygame.image.load("Fondo_juego/Trofeos.jpg").convert()
#FUENTE DE TEXTO Y TAMAÑO DE LETRA
Fuente_texto = pygame.font.Font(None, 19)

Health = 3

user_name = "  "



def draw_text(text, font, color, surface,x,y):
    textobjet = font.render(text, 1, color)
    textrect = textobjet.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobjet, textrect)

#X XD
x = 0



#VARIABLE PARA ACTIVAR EL BOTON
click = False
click_menu = False
Menu = False
def Welcome_Window():
    Tiempo_menu = 0
    Auxiliar_tiempo_menu = 0.2
    while True:

        # VENTANA
        SCREEN_Welcome.fill((54,45,45))

        if Tiempo_menu == 10:
            Menu_juego()

        if Auxiliar_tiempo_menu == 0.2:
            Tiempo_menu += 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

#VENTANA MENU
def Menu_juego():


    pygame.mixer.music.load('musica/Imposble mejorada.ogg')
    pygame.mixer.music.play(-1)
    global user_name
    click = False
    Dios = True

    # INPUT

    while Dios:


        # CUADRO DE TEXTO
        Cuadrado_texto = pygame.Rect(185, 589, 320, 40)
        text_place = font_game3.render(user_name, False, (255, 255, 255))
        Cuadrado_texto.w = text_place.get_width() + 20
        #VENTANA
        SCREEN_Menu.blit(fondo_Menu,(0,-70))
        # CUADRO EN EL TITULO
        pygame.draw.rect(SCREEN_Menu, Cafe, (220, 55, 900, 50), 0)
        # SECCION DE NIVELES
        pygame.draw.rect(SCREEN_Menu, Cafe, (0, 628, 1366, 140), 0)
        # BOTON 1
        pygame.draw.rect(SCREEN_Menu, Gris, (40, 660, 70, 70), 0)
        Button_1 = pygame.Rect(50, 670, 50, 50)
        #BOTON 2
        pygame.draw.rect(SCREEN_Menu, Gris, (340, 660, 70, 70), 0)
        Button_2 = pygame.Rect(350, 670, 50, 50)
        #BOTON 3
        pygame.draw.rect(SCREEN_Menu, Gris, (640, 660, 70, 70), 0)
        Button_3 = pygame.Rect(650, 670, 50, 50)
        # BOTON 4
        pygame.draw.rect(SCREEN_Menu, Gris, (940, 660, 70, 70), 0)
        Button_4 = pygame.Rect(950, 670, 50, 50)
        #ABOUT
        Button_about = pygame.Rect(10, 10, 50, 50)
        #ZONA DE NOMBRE
        pygame.draw.rect(SCREEN_Menu, Cafe, (0, 568, 446, 60), 0)

        draw_text("THE PIRATES IN THE SKY", font_titulos,(255,255,255), SCREEN_Menu,285,67)
        draw_text("Nivel 1", font_game, (255, 255, 255), SCREEN_Menu, 130, 680)
        draw_text("Nivel 2", font_game, (255, 255, 255), SCREEN_Menu, 430, 680)
        draw_text("Nivel 3", font_game, (255, 255, 255), SCREEN_Menu, 730, 680)
        draw_text("Mejores puntajes", font_game, (255, 255, 255), SCREEN_Menu, 1030, 680)
        draw_text("Nombre :", font_game, (255, 255, 255), SCREEN_Menu, 40, 585)
        #Detectar el click del mouse
        mx,my = pygame.mouse.get_pos()

        SCREEN_Menu.blit(text_place, Cuadrado_texto)
        #SCREEN_Menu.blit(user_name, (50, 680))



        if Button_1.collidepoint((mx,my)):
            if click and user_name != "  ":
                Nivel_Uno()
            else:
                click = False
        elif Button_2.collidepoint((mx,my)):
            if click and user_name != "  ":
                Nivel_Dos()
            else:
                click = False
        elif Button_3.collidepoint((mx,my)):
            if click and user_name != "  ":
                Nivel_Tres()
            else:
                click = False
        elif Button_4.collidepoint((mx,my)):
            if click:
                Mejores_puntajes()
            else:
                click = False
        elif Button_about.collidepoint((mx,my)):
            if click:
                Pantalla_about()
            else:
                click = False
        pygame.draw.rect(SCREEN_Menu,Crema,Button_1)
        pygame.draw.rect(SCREEN_Menu, Crema, Button_2)
        pygame.draw.rect(SCREEN_Menu, Crema, Button_3)
        pygame.draw.rect(SCREEN_Menu, Crema, Button_4)
        pygame.draw.rect(SCREEN_Menu, Crema, Button_about)
        pygame.draw.rect(SCREEN_Menu, Cafe,Cuadrado_texto,2)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[0:-1]
                else:
                    user_name += event.unicode
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        pygame.display.flip()
        Clock.tick(60)

#NIVEL1
def Nivel_Uno():
    #Music
    pygame.mixer.music.load('musica/Remix Four brave champions.ogg')
    pygame.mixer.music.play(0)
    #FLAGS
    Dios = True
    click = False
    global user_name



    class Pirate_ship(pygame.sprite.Sprite):
        # Sprite del barco
        def __init__(self):
            # Se hereda el init de la clase Sprite de pygame
            super().__init__()
            # La bala/rectangulo
            self.image = pygame.image.load("Imagenes_personajes/Legendary ship.png").convert()
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
                self.acceleracion_inicialX = -20

            # MOVIMIENTO HACIA LA DERECHA
            if teclas[pygame.K_d]:
                self.acceleracion_inicialX = 20

            # MOVIMIENTO HACIA LA ARRIBA
            if teclas[pygame.K_w]:
                self.acceleracion_inicialY = -20

            # MOVIMIENTO HACIA LA ABAJO
            if teclas[pygame.K_s]:
                self.acceleracion_inicialY = 20

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
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE DERECHO
            elif self.rect.right >= Largo_2:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE INFERIOR
            elif self.rect.bottom >= 650:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)


                elif Up_down_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE  SUPERIOR
            elif self.rect.top <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)


                elif Up_down_direction == 2:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)

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
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE DERECHO
            elif self.rect.right >= Largo_2:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE INFERIOR
            elif self.rect.bottom >= 650:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)

                elif Up_down_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE  SUPERIOR
            elif self.rect.top <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)


                elif Up_down_direction == 2:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)

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
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE DERECHO
            elif self.rect.right >= Largo_2:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Right_left_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)



                elif Right_left_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE INFERIOR
            elif self.rect.bottom >= 650:  # CON ESTE LA BALA SUBE HACIA LA DERECHA
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)


                elif Up_down_direction == 2:  # CON ESTE LA BALA SUBE HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = -random.randint(4,9)




            # LIMITAR EL BORDE  SUPERIOR
            elif self.rect.top <= 0:
                Choque = True

                if Choque:
                    Metalic_sound.play()
                if Up_down_direction == 1:  # CON ESTE LA BALA BAJA HACIA LA DERECHA
                    self.acceleracion_inicialX = random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)


                elif Up_down_direction == 2:  # CON ESTE LA BALA BAJA HACIA LA IZQUIERDA
                    self.acceleracion_inicialX = -random.randint(4,9)
                    self.acceleracion_inicialY = random.randint(4,9)



    # _____________________________________________CREACION DE LA VENTANA_____________________________________________________#
    pygame.init()


    pygame.display.set_caption("¡¡THE PIRATES IN THE SKY!!")



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

    #BOTONES
    Button_Menu = pygame.Rect(350,700,60,30)

    Health = 3

    Tiempo = 0
    Aux_Tiempo = 61

    def actualizacionPantalla():
        global x

        # COLOR DE FONDO
        SCREEN_Level1.fill(MORADO_LINDO)

        # UBICACION DE LOS TEXTOS EN LA PANTALLA
        SCREEN_Level1.blit(miTexto2, (50, 680))
        SCREEN_Level1.blit(miTexto, (220, 680))
        SCREEN_Level1.blit(miTexto3, (50, 720))
        SCREEN_Level1.blit(miTexto4, (220, 720))
        SCREEN_Level1.blit(Life_counter, (1000, 700))
        SCREEN_Level1.blit(Player_life, (1200, 700))
        SCREEN_Level1.blit(Nombre_jugador, (800, 700))
        SCREEN_Level1.blit(El_jugador, (550, 700))

        if Health <= 0:
            Gamer_over()
        if Tiempo == 6100:
            Gamer_over()

        Linea_divisora = pygame.draw.line(SCREEN_Level1, BLANCO, (0, 650), (1366, 650), 20)

        # FONDO EN MOVIMIENTO
        x_bucle = x % fondo.get_rect().width
        SCREEN_Level1.blit(fondo, (x_bucle - fondo.get_rect().width, 0))
        if x_bucle < Largo_2:
            SCREEN_Level1.blit(fondo, (x_bucle, 0))
        x -= 1




    while Dios:


        # ________FPS________________________________________________________________________________________________
        RELOJ.tick(100)

        mx, my = pygame.mouse.get_pos()

        # TEXTOS EN LA PANTALLA
        miTexto = font_game2.render(str(Tiempo//100), bool(0), BLANCO)
        miTexto2 = font_game2.render("TEMPORIZADOR   :", bool(0), BLANCO)

        miTexto3 = font_game2.render("PUNTAJE   :", bool(0), BLANCO)
        miTexto4 = font_game2.render(str(Tiempo//100), bool(0), BLANCO)

        Life_counter = font_game2.render(str("VIDA DEL JUGADOR"), bool(0), BLANCO)
        Player_life = font_game2.render(str(Health), bool(0), BLANCO)
        El_jugador = font_game2.render(str("NOMBRE DEL JUGADOR : "), bool(0), BLANCO)
        Nombre_jugador = font_game2.render(str(user_name), bool(0), BLANCO)

        # BUCLE EN EL JUEGO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # ALEATORIOS ARRIBA-ABAJO-DERECHA-IZQUIERDA
        Up_down_direction = random.randint(1, 2)
        Right_left_direction = random.randint(1, 2)


        # ___________________________________________ZONA DE VENTANA________________________________________________#
        # ACTUALIZACION DE LA VENTANA
        pygame.display.update()

        actualizacionPantalla()

        # Actualizar los sprites
        jugador.update()

        Enemigo_1.update()

        Enemigo_2.update()

        Enemigo_3.update()

        #Timer()
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

        if Aux_Tiempo == 61:
            Tiempo += 1
        if Button_Menu.collidepoint((mx,my)):
            if click:
                Menu_juego()
        # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
        jugador.draw(SCREEN_Level1)
        Enemigo_1.draw(SCREEN_Level1)
        Enemigo_2.draw(SCREEN_Level1)
        Enemigo_3.draw(SCREEN_Level1)
        pygame.draw.rect(SCREEN_Level1,(255,255,255),Button_Menu)

#NIVEL2
def Nivel_Dos():

    click = False
    global x
    pygame.mixer.music.load('musica/Protectors.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(6.0)

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
                self.acceleracion_inicialX = -20

            # MOVIMIENTO HACIA LA DERECHA
            if teclas[pygame.K_d]:
                self.acceleracion_inicialX = 20

            # MOVIMIENTO HACIA LA ARRIBA
            if teclas[pygame.K_w]:
                self.acceleracion_inicialY = -20

            # MOVIMIENTO HACIA LA ABAJO
            if teclas[pygame.K_s]:
                self.acceleracion_inicialY = 20

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


    class Enemigo4(pygame.sprite.Sprite):

        # Sprite del barco
        def __init__(self):
            # Se hereda el init de la clase Sprite de pygame
            super().__init__()
            # La bala/rectangulo
            self.image = pygame.image.load("imagenes_adicionales/bomba_class4.png").convert()
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



    # _______________________________________________SPRITES______________________________________________________________

    jugador = pygame.sprite.Group()
    Enemigo_1 = pygame.sprite.Group()
    Enemigo_2 = pygame.sprite.Group()
    Enemigo_3 = pygame.sprite.Group()
    Enemigo_4 = pygame.sprite.Group()
    # SPRITE ENEMIGOS
    Bullets = Enemigo()
    Enemigo_1.add(Bullets)

    Bullets2 = Enemigo2()
    Enemigo_2.add(Bullets2)

    Bullets3 = Enemigo3()
    Enemigo_3.add(Bullets3)

    Bullets4 = Enemigo4()
    Enemigo_4.add(Bullets4)

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
    Health_Dos = 3
    Tiempo_Dos = 0
    Aux_Tiempo_Dos = 61


    # BOTONES
    Button_Menu = pygame.Rect(350, 700, 60, 30)
    def actualizacionPantalla():
        global x

        # COLOR DE FONDO
        SCREEN_Level1.fill(MORADO_LINDO2)

        # UBICACION DE LOS TEXTOS EN LA PANTALLA
        SCREEN_Level2.blit(miTexto2, (50, 680))
        SCREEN_Level2.blit(miTexto, (220, 680))
        SCREEN_Level2.blit(miTexto3, (50, 720))
        SCREEN_Level2.blit(miTexto4, (220, 720))
        SCREEN_Level2.blit(Life_counter, (1000, 700))
        SCREEN_Level2.blit(Player_life, (1200, 700))
        SCREEN_Level2.blit(Nombre_jugador, (800, 700))
        SCREEN_Level2.blit(El_jugador, (550, 700))

        if Health_Dos <= 0:
            Gamer_over()
        if Tiempo_Dos == 6100:
            Gamer_over()

        Linea_divisora = pygame.draw.line(SCREEN_Level2, BLANCO, (0, 650), (1366, 650), 20)

        # FONDO EN MOVIMIENTO
        x_bucle = x % fondo2.get_rect().width
        SCREEN_Level2.blit(fondo2, (x_bucle - fondo2.get_rect().width, 0))
        if x_bucle < Largo_2:
            SCREEN_Level2.blit(fondo2, (x_bucle, 0))
        x -= 1
    while Dios:

        # ________FPS________________________________________________________________________________________________
        RELOJ.tick(100)

        # PUNTAJES

        mx, my = pygame.mouse.get_pos()

        # TEXTOS EN LA PANTALLA
        miTexto = font_game2.render(str(Tiempo_Dos//100), bool(0), BLANCO)
        miTexto2 = font_game2.render("TEMPORIZADOR   :", bool(0), BLANCO)
        miTexto3 = font_game2.render("PUNTAJE   :", bool(0), BLANCO)
        miTexto4 = font_game2.render(str(Tiempo_Dos*3//100), bool(0), BLANCO)
        Life_counter = font_game2.render(str("VIDA DEL JUGADOR  :"), bool(0), BLANCO)
        Player_life = font_game2.render(str(Health_Dos), bool(0), BLANCO)
        El_jugador = font_game2.render(str("NOMBRE DEL JUGADOR : "), bool(0), BLANCO)
        Nombre_jugador = font_game2.render(str(user_name), bool(0), BLANCO)

        # BUCLE EN EL JUEGO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
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

        Enemigo_4.update()
        # ______________________COLISIONES______________________________________________________________________________________

        Colission_1 = pygame.sprite.groupcollide(Enemigo_1, jugador, True, False, pygame.sprite.collide_rect)

        Colission_2 = pygame.sprite.groupcollide(Enemigo_2, jugador, True, False, pygame.sprite.collide_rect)

        Colission_3 = pygame.sprite.groupcollide(Enemigo_3, jugador, True, False, pygame.sprite.collide_rect)

        Colission_4 = pygame.sprite.groupcollide(Enemigo_4, jugador, True, False, pygame.sprite.collide_rect)

        # SI LA BOMBA CHOCA CON LA NAVE SE RESTA LA VIDA
        if Colission_1:
            Health_Dos -= 1

        if Colission_2:
            Health_Dos -= 1

        if Colission_3:
            Health_Dos -= 1

        if Colission_4:
            Health_Dos -= 1

        if Aux_Tiempo_Dos == 61:
            Tiempo_Dos += 1

        if Button_Menu.collidepoint((mx,my)):
            if click:
                Menu_juego()
        # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
        jugador.draw(SCREEN_Level2)
        Enemigo_1.draw(SCREEN_Level2)
        Enemigo_2.draw(SCREEN_Level2)
        Enemigo_3.draw(SCREEN_Level2)
        Enemigo_4.draw(SCREEN_Level2)
        pygame.draw.rect(SCREEN_Level1, (255, 255, 255), Button_Menu)

#NIVEL3
def Nivel_Tres():
    global x
    click = False

    pygame.mixer.music.load('musica/Stregh.ogg')
    pygame.mixer.music.play(0)

    class Pirate_ship(pygame.sprite.Sprite):
        # Sprite del barco
        def __init__(self):
            # Se hereda el init de la clase Sprite de pygame
            super().__init__()
            # La bala/rectangulo
            self.image = pygame.image.load("Imagenes_personajes/Pirate ship.png").convert()
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
                self.acceleracion_inicialX = -20

            # MOVIMIENTO HACIA LA DERECHA
            if teclas[pygame.K_d]:
                self.acceleracion_inicialX = 20

            # MOVIMIENTO HACIA LA ARRIBA
            if teclas[pygame.K_w]:
                self.acceleracion_inicialY = -20

            # MOVIMIENTO HACIA LA ABAJO
            if teclas[pygame.K_s]:
                self.acceleracion_inicialY = 20

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


    class Enemigo4(pygame.sprite.Sprite):

        # Sprite del barco
        def __init__(self):
            # Se hereda el init de la clase Sprite de pygame
            super().__init__()
            # La bala/rectangulo
            self.image = pygame.image.load("imagenes_adicionales/bomba_class4.png").convert()
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


    class Enemigo5(pygame.sprite.Sprite):

        # Sprite del barco
        def __init__(self):
            # Se hereda el init de la clase Sprite de pygame
            super().__init__()
            # La bala/rectangulo
            self.image = pygame.image.load("imagenes_adicionales/bomba_class5.png").convert()
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
    Enemigo_4 = pygame.sprite.Group()
    Enemigo_5 = pygame.sprite.Group()
    # SPRITE ENEMIGOS
    Bullets = Enemigo()
    Enemigo_1.add(Bullets)

    Bullets2 = Enemigo2()
    Enemigo_2.add(Bullets2)

    Bullets3 = Enemigo3()
    Enemigo_3.add(Bullets3)

    Bullets4 = Enemigo4()
    Enemigo_4.add(Bullets4)

    Bullets5 = Enemigo5()
    Enemigo_5.add(Bullets5)

    # SPRITE JUGADOR
    Jugador = Pirate_ship()
    jugador.add(Jugador)

    # VARIABLES PARA EL BUCLE DE LA PANTALLA
    x = 0

    # CENTRO DE FPS
    RELOJ = pygame.time.Clock()

    # FUENTES




    # BUCLE PARA LA VENTANA
    Dios = True

    Tiempo_3 = 0
    Aux_Tiempo_3 = 60
    Health = 3

    # BOTONES
    Button_Menu = pygame.Rect(350, 700, 60, 30)
    def actualizacionPantalla():
        global x

        # COLOR DE FONDO
        SCREEN_Level3.fill(GRIS)

        # UBICACION DE LOS TEXTOS EN LA PANTALLA
        SCREEN_Level3.blit(miTexto2, (50, 680))
        SCREEN_Level3.blit(miTexto, (220, 680))
        SCREEN_Level3.blit(miTexto3, (50, 720))
        SCREEN_Level3.blit(miTexto4, (220, 720))
        SCREEN_Level3.blit(Life_counter, (1000, 700))
        SCREEN_Level3.blit(Player_life, (1200, 700))
        SCREEN_Level3.blit(Nombre_jugador, (800, 700))
        SCREEN_Level3.blit(El_jugador, (550, 700))

        if Health <= 0:
            Gamer_over()
        if Tiempo_3 == 6100:
            Gamer_over()

        Linea_divisora = pygame.draw.line(SCREEN_Level3, BLANCO, (0, 650), (1366, 650), 20)

        # FONDO EN MOVIMIENTO
        x_bucle = x % fondo3.get_rect().width
        SCREEN_Level3.blit(fondo3, (x_bucle - fondo3.get_rect().width, 0))
        if x_bucle < Largo_2:
            SCREEN_Level3.blit(fondo3, (x_bucle, 0))
        x -= 1
    while Dios:

        # ________FPS________________________________________________________________________________________________
        RELOJ.tick(100)

        mx, my = pygame.mouse.get_pos()

        # TEXTOS EN LA PANTALLA
        miTexto = font_game2.render(str(Tiempo_3//100), bool(0), BLANCO)
        miTexto2 = font_game2.render("TEMPORIZADOR   :", bool(0), BLANCO)
        miTexto3 = font_game2.render("PUNTAJE   :", bool(0), BLANCO)
        miTexto4 = font_game2.render(str(Tiempo_3*5//100), bool(0), BLANCO)
        Life_counter = font_game2.render(str("VIDA DEL JUGADOR  :"), bool(0), BLANCO)
        Player_life = font_game2.render(str(Health), bool(0), BLANCO)
        El_jugador = font_game2.render(str("NOMBRE DEL JUGADOR : "), bool(0), BLANCO)
        Nombre_jugador = font_game2.render(str(user_name), bool(0), BLANCO)

        # BUCLE EN EL JUEGO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # ALEATORIOS ARRIBA-ABAJO-DERECHA-IZQUIERDA
        Up_down_direction = random.randint(1, 2)
        Right_left_direction = random.randint(1, 2)
        # VALORES DE LOS EJES X y Y
        Direccion_aleatoria_X = random.randint(5, 7)
        Direccion_aleatoria_Y = random.randint(5, 7)

        # ___________________________________________ZONA DE VENTANA________________________________________________#
        # ACTUALIZACION DE LA VENTANA
        pygame.display.update()

        actualizacionPantalla()

        # Actualizar los sprites
        jugador.update()

        Enemigo_1.update()

        Enemigo_2.update()

        Enemigo_3.update()

        Enemigo_4.update()

        Enemigo_5.update()
        # ______________________COLISIONES______________________________________________________________________________________

        Colission_1 = pygame.sprite.groupcollide(Enemigo_1, jugador, True, False, pygame.sprite.collide_rect)

        Colission_2 = pygame.sprite.groupcollide(Enemigo_2, jugador, True, False, pygame.sprite.collide_rect)

        Colission_3 = pygame.sprite.groupcollide(Enemigo_3, jugador, True, False, pygame.sprite.collide_rect)

        Colission_4 = pygame.sprite.groupcollide(Enemigo_4, jugador, True, False, pygame.sprite.collide_rect)

        Colission_5 = pygame.sprite.groupcollide(Enemigo_5, jugador, True, False, pygame.sprite.collide_rect)

        #Space_ship_collision = pygame.sprite.spritecollide(Jugador, Enemigo_1, True)

        # SI LA BOMBA CHOCA CON LA NAVE SE RESTA LA VIDA
        if Colission_1:
            Health -= 1

        if Colission_2:
            Health -= 1

        if Colission_3:
            Health -= 1

        if Colission_4:
            Health -= 1

        if Colission_5:
            Health -= 1

        if Aux_Tiempo_3 == 60:
            Tiempo_3 += 1

        if Button_Menu.collidepoint((mx,my)):
            if click:
                Menu_juego()
        # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
        jugador.draw(pantalla)
        Enemigo_1.draw(pantalla)
        Enemigo_2.draw(pantalla)
        Enemigo_3.draw(pantalla)
        Enemigo_4.draw(pantalla)
        Enemigo_5.draw(pantalla)
        pygame.draw.rect(SCREEN_Level3, (255, 255, 255), Button_Menu)

#VENTANA DEL GAMER OVER
def Gamer_over():
    running = True

    pygame.mixer.music.load('musica/Arcangel two steps from hell.ogg')
    pygame.mixer.music.play(0)
    while running:
        click_Menu = False
        SCREEN_Gamer_Over.blit(fondo_gamerover,(1,1))
        draw_text("¡GAMER OVER!", font_menu, (255, 255, 255), SCREEN_Menu, 520, 300)
        mx, my = pygame.mouse.get_pos()

        # BOTON
        Button_Menu = pygame.Rect(590, 400, 120, 50)
        #Button_2 = pygame.Rect(50, 400, 50, 50)
        #Button_3 = pygame.Rect(50, 600, 50, 50)
        pygame.draw.rect(SCREEN_Gamer_Over, (Crema), Button_Menu)




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

#VENTANA PUNTAJES
def Mejores_puntajes():
    running = True

    pygame.mixer.music.load('musica/Puntajes.ogg')
    pygame.mixer.music.play(0)
    while running:
        click_Menu = False
        SCREEN_Gamer_Over.blit(fondo_trofeos,(1,1))
        #TEXTO EN PANTALLA
        draw_text("¡MEJORES PUNTAJES!", font_menu, (255, 255, 255), SCREEN_Menu, 480, 50)
        #PRIMERO
        draw_text("PRIMERO -->", font_Input, (255, 255, 255), SCREEN_Menu, 480, 150)
        #SEGUNDO
        draw_text("SEGUNDO -->", font_Input, (255, 255, 255), SCREEN_Menu, 480, 225)
        #TERCERO
        draw_text("TERCERO -->", font_Input, (255, 255, 255), SCREEN_Menu, 480, 300)
        #CUARTO
        draw_text("CUARTO -->", font_Input, (255, 255, 255), SCREEN_Menu, 480, 375)
        #QUINTO
        draw_text("QUINTO -->", font_Input, (255, 255, 255), SCREEN_Menu, 480, 450)
        #SEXTO
        draw_text("SEXTO -->", font_Input, (255, 255, 255), SCREEN_Menu, 480, 525)
        #SEPTIMO
        draw_text("SÉPTIMO -->", font_Input, (255, 255, 255), SCREEN_Menu, 480, 600)





        # BOTON
        mx, my = pygame.mouse.get_pos()
        Button_Menu = pygame.Rect(15, 708, 80, 50)

        pygame.draw.rect(SCREEN_Gamer_Over, (Crema), Button_Menu)


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
                else:
                    click_Menu = False
        if Button_Menu.collidepoint((mx, my)):
            if click_Menu:
                Menu_juego()

        pygame.display.update()
        Clock.tick(60)

def Pantalla_about():
    running = True

    pygame.mixer.music.load('musica/Puntajes.ogg')
    pygame.mixer.music.play(0)
    while running:
        click_Menu = False
        SCREEN_Gamer_Over.blit(fondo_trofeos,(1,1))
    #TEXTO EN PANTALLA
        draw_text("ABOUT", font_menu2, (255, 255, 255), SCREEN_Menu, 480, 20)


        draw_text("Pais de producción :", font_menu2, (255, 255, 255), SCREEN_Menu, 100, 75)
        draw_text("Costa Rica", font_menu3, (255, 255, 255), SCREEN_Menu, 100, 110)

        #PRIMERO
        draw_text("Universidad-Carrera  :", font_menu2, (255, 255, 255), SCREEN_Menu, 100, 150)
        draw_text("Tecnológico de Costa Rica    CE 1102", font_menu3, (255, 255, 255), SCREEN_Menu, 100, 185)

        #SEGUNDO
        draw_text("Asignatura-Año-Grupo  :", font_menu2, (255, 255, 255), SCREEN_Menu, 100, 225)
        draw_text("Taller de programación, 2021, GRUPO 4", font_menu3, (255, 255, 255), SCREEN_Menu, 100, 260)

        #TERCERO
        draw_text("Profesor  :", font_menu2, (255, 255, 255), SCREEN_Menu, 100, 300)
        draw_text("Luis Barboza Artavia", font_menu3, (255, 255, 255), SCREEN_Menu, 100, 335)

        #CUARTO
        draw_text("Versión del programa  :", font_menu2, (255, 255, 255), SCREEN_Menu, 100, 375)
        draw_text("1.0", font_menu3, (255, 255, 255), SCREEN_Menu, 100, 410)

        #QUINTO
        draw_text("Autores  :", font_menu2, (255, 255, 255), SCREEN_Menu, 100, 450)
        draw_text("Josthin Soto Sánchez,  Axel Flores Lara", font_menu3, (255, 255, 255), SCREEN_Menu, 100, 485)

        #SEXTO
        draw_text("Modulos  :", font_menu2, (255, 255, 255), SCREEN_Menu, 100, 525)
        draw_text("https://www.youtube.com/watch?v=5v_Jl6tMU68&list=PLVzwufPir356RMxSsOccc38jmxfxqfBdp", font_menu3, (255, 255, 255), SCREEN_Menu, 100, 560)

        draw_text("https://www.youtube.com/watch?v=Rvcyf4HsWiw&ab_channel=ClearCode", font_menu3, (255, 255, 255), SCREEN_Menu, 100, 585)







        # BOTON
        mx, my = pygame.mouse.get_pos()
        Button_Menu = pygame.Rect(15, 708, 80, 50)

        pygame.draw.rect(SCREEN_Gamer_Over, (Crema), Button_Menu)


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
                else:
                    click_Menu = False
        if Button_Menu.collidepoint((mx, my)):
            if click_Menu:
                Menu_juego()

        pygame.display.update()
        Clock.tick(60)

Welcome_Window()
pygame.display.update()
