#BIBLIOTECAS A USAR
import pygame, sys
from pygame.locals import *
import random
import pygame
import pygame_menu

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
font_titulos = pygame.font.SysFont ("Wide Latin", 20)
font_menu = pygame.font.SysFont("Amasis MT Pro Black",60)
font_game = pygame.font.Font(None,12)

#MUSICA/EFECTOS
Metalic_sound = pygame.mixer.Sound('musica/Sonido colision (mp3cut.net).ogg')

# COLORES
BLANCO = (255, 255, 255)
MORADO_LINDO = (39, 22, 56)



#FONDO DEL JUEGO
fondo = pygame.image.load("Fondo_juego/fondo experimental.png").convert()
fondo_Menu = pygame.image.load("Fondo_juego/Sky_ship2.jpg").convert()
#FUENTE DE TEXTO Y TAMAÑO DE LETRA
Fuente_texto = pygame.font.Font(None, 19)

Health = 3





def draw_text(text, font, color, surface,x,y):
    textobjet = font.render(text, 1, color)
    textrect = textobjet.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobjet, textrect)

#X XD
x = 0

#VARIABLES GLOBALES
Dios = True
Cronos = True

menu = pygame_menu.Menu(
            height=400,
            theme=pygame_menu.themes.THEME_SOLARIZED,
            title='¡BIENVENIDO!',
            width=500
        )




#VARIABLE PARA ACTIVAR EL BOTON
click = False
click_menu = False
Menu = False
def Welcome_Window():
    click_menu = False
    while True:

        # VENTANA
        SCREEN_Welcome.fill((54,45,45))
        draw_text("WELCOME TO PIRATES IN THE SKY", font_titulos, (0, 0, 0), SCREEN_Welcome, 520, 70)
        draw_text("Nivel 1", font_menu, (0, 0, 0), SCREEN_Welcome, 110, 200)
        # Detectar el click del mouse
        mx, my = pygame.mouse.get_pos()

        # BOTON
        Button_Welcome = pygame.Rect(50, 200, 50, 50)

        if Button_Welcome.collidepoint((mx, my)):
            if click_menu:
                Menu_juego()

        pygame.draw.rect(SCREEN_Welcome, (0, 255, 0), Button_Welcome)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_menu = True
        pygame.display.update()

def Menu_juego():
    global Dios
    global Cronos
    global menu
    pygame.mixer.music.load('musica/Imposible TSH remix.ogg')
    pygame.mixer.music.play(0)

    click = False
    Dios = True
    user_name = menu.add.text_input('Nombre: ', default='', maxchar=10)
    print('{0}, AQUI VA EL JUEGO'.format(user_name.get_value()))
    while Dios:


        #VENTANA
        SCREEN_Menu.blit(fondo_Menu,(1,1))
        #SCREEN_Menu.blit(fondo, (0, 0))
        draw_text("THE PIRATES IN THE SKY", font_titulos,(255,255,255), SCREEN_Menu,520,70)
        draw_text("Nivel 1", font_menu, (0, 0, 0), SCREEN_Menu, 110, 200)
        #Detectar el click del mouse
        mx,my = pygame.mouse.get_pos()

        #SCREEN_Menu.blit(user_name, (50, 680))

        #BOTON
        Button_1 = pygame.Rect(50,200,50,50)
        Button_2 = pygame.Rect(50,400,50,50)
        Button_3 = pygame.Rect(50, 600, 50, 50)

        if Button_1.collidepoint((mx,my)):
            if click:
                Dios = True
                Nivel_Uno()

        elif Button_2.collidepoint((mx,my)):
            if click:
                Nivel_Dos()
        elif Button_3.collidepoint((mx,my)):
            if click:
                Nivel_Tres()
        pygame.draw.rect(SCREEN_Menu,(0,255,0),Button_1)
        pygame.draw.rect(SCREEN_Menu, (255, 0, 0), Button_2)
        pygame.draw.rect(SCREEN_Menu, (0, 0, 255), Button_3)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    Contador_tiempo = True
        pygame.display.update()
        Clock.tick(60)

def Nivel_Uno():
    #Music
    pygame.mixer.music.load('musica/Remix Four brave champions.ogg')
    pygame.mixer.music.play(0)
    #FLAGS
    Dios = True
    while Dios:




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

        # FUENTES
        Fuente_texto = pygame.font.Font(None, 19)

        #BOTONES
        Button_Menu = pygame.Rect(100,630,60,20)

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

            if Health == 0:
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



            # TEXTOS EN LA PANTALLA
            miTexto = Fuente_texto.render(str(Tiempo//100), bool(0), BLANCO)
            miTexto2 = Fuente_texto.render("TEMPORIZADOR   :", bool(0), BLANCO)

            miTexto3 = Fuente_texto.render("PUNTAJE   :", bool(0), BLANCO)
            miTexto4 = Fuente_texto.render(str(Tiempo//100), bool(0), BLANCO)

            Life_counter = Fuente_texto.render(str("VIDA DEL JUGADOR  :"), bool(0), BLANCO)
            Player_life = Fuente_texto.render(str(Health), bool(0), BLANCO)



            # BUCLE EN EL JUEGO
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
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

            # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
            jugador.draw(SCREEN_Level1)
            Enemigo_1.draw(SCREEN_Level1)
            Enemigo_2.draw(SCREEN_Level1)
            Enemigo_3.draw(SCREEN_Level1)
            pygame.draw.rect(SCREEN_Level1,(255,255,255),Button_Menu)




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

        clock = pygame.time.Clock()

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

        def actualizacionPantalla():
            global x

            # COLOR DE FONDO
            SCREEN_Level1.fill(MORADO_LINDO)

            # UBICACION DE LOS TEXTOS EN LA PANTALLA
            SCREEN_Level2.blit(miTexto2, (50, 680))
            SCREEN_Level2.blit(miTexto, (220, 680))
            SCREEN_Level2.blit(miTexto3, (50, 720))
            SCREEN_Level2.blit(miTexto4, (220, 720))
            SCREEN_Level2.blit(Life_counter, (1000, 700))
            SCREEN_Level2.blit(Player_life, (1200, 700))

            if Health_Dos == 0:
                Gamer_over()
            if Tiempo_Dos == 6100:
                Gamer_over()

            Linea_divisora = pygame.draw.line(SCREEN_Level2, BLANCO, (0, 650), (1366, 650), 20)

            # FONDO EN MOVIMIENTO
            x_bucle = x % fondo.get_rect().width
            SCREEN_Level2.blit(fondo, (x_bucle - fondo.get_rect().width, 0))
            if x_bucle < Largo_2:
                SCREEN_Level2.blit(fondo, (x_bucle, 0))
            x -= 1
        while Dios:

            # ________FPS________________________________________________________________________________________________
            RELOJ.tick(100)

            # PUNTAJES


            # TEXTOS EN LA PANTALLA
            miTexto = Fuente_texto.render(str(Tiempo_Dos//100), bool(0), BLANCO)
            miTexto2 = Fuente_texto.render("TEMPORIZADOR   :", bool(0), BLANCO)
            miTexto3 = Fuente_texto.render("PUNTAJE   :", bool(0), BLANCO)
            miTexto4 = Fuente_texto.render(str(Tiempo_Dos*3//100), bool(0), BLANCO)
            Life_counter = Fuente_texto.render(str("VIDA DEL JUGADOR  :"), bool(0), BLANCO)
            Player_life = Fuente_texto.render(str(Health_Dos), bool(0), BLANCO)
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
            # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
            jugador.draw(SCREEN_Level2)
            Enemigo_1.draw(SCREEN_Level2)
            Enemigo_2.draw(SCREEN_Level2)
            Enemigo_3.draw(SCREEN_Level2)
            Enemigo_4.draw(SCREEN_Level2)


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
        Fuente_texto = pygame.font.Font(None, 19)



        # BUCLE PARA LA VENTANA
        Dios = True

        Tiempo_3 = 0
        Aux_Tiempo_3 = 60
        Health = 7
        def actualizacionPantalla():
            global x

            # COLOR DE FONDO
            SCREEN_Level1.fill(MORADO_LINDO)

            # UBICACION DE LOS TEXTOS EN LA PANTALLA
            SCREEN_Level3.blit(miTexto2, (50, 680))
            SCREEN_Level3.blit(miTexto, (220, 680))
            SCREEN_Level3.blit(miTexto3, (50, 720))
            SCREEN_Level3.blit(miTexto4, (220, 720))
            SCREEN_Level3.blit(Life_counter, (1000, 700))
            SCREEN_Level3.blit(Player_life, (1200, 700))

            if Health == 0:
                Gamer_over()
            if Tiempo_3 == 6100:
                Gamer_over()

            Linea_divisora = pygame.draw.line(SCREEN_Level3, BLANCO, (0, 650), (1366, 650), 20)

            # FONDO EN MOVIMIENTO
            x_bucle = x % fondo.get_rect().width
            SCREEN_Level3.blit(fondo, (x_bucle - fondo.get_rect().width, 0))
            if x_bucle < Largo_2:
                SCREEN_Level3.blit(fondo, (x_bucle, 0))
            x -= 1
        while Dios:

            # ________FPS________________________________________________________________________________________________
            RELOJ.tick(100)


            # TEXTOS EN LA PANTALLA
            miTexto = Fuente_texto.render(str(Tiempo_3//100), bool(0), BLANCO)
            miTexto2 = Fuente_texto.render("TEMPORIZADOR   :", bool(0), BLANCO)
            miTexto3 = Fuente_texto.render("PUNTAJE   :", bool(0), BLANCO)
            miTexto4 = Fuente_texto.render(str(Tiempo_3*5//100), bool(0), BLANCO)
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
            # MOSTRAR AL JUGADOR Y ENEMIGOS EN LA PANTALLA
            jugador.draw(pantalla)
            Enemigo_1.draw(pantalla)
            Enemigo_2.draw(pantalla)
            Enemigo_3.draw(pantalla)
            Enemigo_4.draw(pantalla)
            Enemigo_5.draw(pantalla)

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
pygame.display.update()
