
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any
surface = create_example_window('PRUEBA DE INTERFAZ', (500, 400))
a = 50
def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the levels to play.
    
    """
    print('Seleccionar dificultad {} ({})'.format(selected[0], value))


def start_the_game() -> None:
    """
    Function that starts a game.
    """
    global user_name
    print('{0}, AQUI VA EL JUEGO'.format(user_name.get_value()))


menu = pygame_menu.Menu(
    height=400,
    theme=pygame_menu.themes.THEME_SOLARIZED,
    title='¡BIENVENIDO!',
    width=500
)

user_name = menu.add.text_input('Nombre: ', default="", maxchar=10)
menu.add.selector('Nivel: ', [('Primero', 1), ('Segundo', 2),('Tercero', 3)], onchange=set_difficulty)
menu.add.button('Jugar', start_the_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)

if start_the_game() ==True:
    from Juego_pygame import*