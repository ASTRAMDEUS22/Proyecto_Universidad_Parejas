import pygame
import random
#TAMAÑO PANTALLA
Largo = 1366
Ancho = 768

#NUMEROS ALEATORIOS
locos = random.randint(1,5)

FPS = 60
#COLORES
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)
Blue_sky = (67,168,219)
Orange = (246,127,23)

class Nave(pygame.sprite.Sprite):
    #Sprite de la nave
    def __init__(self):
        #Se hereda el init de la clase Sprite de pygame
        super().__init__()
        #La nave/rectangulo
        self.image = pygame.image.load("bullet.png").convert()
        self.image.set_colorkey("black")


        #Se obtiene el rectangulo
        self.rect = self.image.get_rect()
        #ACOMODAR EL RECTANGULO/CENTRO
        self.rect.center = (Largo // 2, Ancho // 2)
    def update(self): #el UPDATE esta heredado, si se utiliza otra cosa dejará de funcionar
        #SE ACTUALIZA EL RECTANGULO EN CADA BUCLE
        self.rect.x -= 3
        self.rect.y -= 10
        if self.rect.right < 0:
            self.rect.right = Largo
        if self.rect.top < 0:
            self.rect.top = Ancho

#CREACION DE LA VENTANA
pygame.init()
pantalla = pygame.display.set_mode(((Largo,Ancho)))
pygame.display.set_caption("Simularemos la bala")
clock = pygame.time.Clock()

#SPRITES E INSTACIAR OBJETO/JUGADOR
sprites = pygame.sprite.Group()
nave = Nave()
sprites.add((nave))

Dios = True
#BUCLE PARA LA VENTANA
while Dios:
    #VELOCIDAD BUCLE DEL JUEGO
    clock.tick(FPS)

    #EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Dios = False

    #Actualizar los sprites
    sprites.update()

    #PERSONALIZACION
    pantalla.fill(White)
    sprites.draw(pantalla)

    #REFRESCA LA PANTALLA
    pygame.display.flip()

print(random)
pygame.quit()