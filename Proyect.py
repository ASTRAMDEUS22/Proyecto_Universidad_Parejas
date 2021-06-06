from tkinter import *

class Principal_Window:
    def __init__(self, algo):

        self.frameInit = Canvas(Home_window, width=1366, height=768, bg="yellow")
        self.frameInit.place(x=-10, y=-10)

        self.Button_menu = Button(Home_window,text="EMPEZAR",font=("Arial",13), fg="blue",bg="White", command=self.Principal_screen)
        self.Button_menu.place(x=200,y=300)

        self.Wallpaper_image = PhotoImage(file="Imagen Principal.png")
        self.Wallpaper_image_ubication = self.frameInit.create_image(693,390, image=self.Wallpaper_image)

        self.Game_name = Label(text="ADVENTURES IN THE SEA", font=("Bradley Hand ITC",32), width=22,height=-7)
        self.Game_name.place(x=400,y=100)

        self.Creaneo_uno = PhotoImage(file="Pirata craneo.png")
        self.Creaneo_uno_ubication = self.frameInit.create_image(300, 150, image=self.Creaneo_uno)

        self.Creaneo_dos = PhotoImage(file="Pirata craneo.png")
        self.Creaneo_dos_ubication = self.frameInit.create_image(1080, 150, image=self.Creaneo_dos)
    def Principal_screen(self):
        #CANVAS DE JUEGO
        self.principal_screen = Canvas(Home_window, width=1700, height=780, bg="red")
        self.principal_screen.place(x=-10, y=-2)
        #IMAGEN DEL OCEANO
        self.Ocean_image = PhotoImage(file="ocean-mist-horizon-24875-1366x768.png")
        self.Ocean_image_place = self.principal_screen.create_image(693, 386, image=self.Ocean_image)
        #CANVAS DE LA INFORMACION
        self.Information_zone = Canvas(Home_window, width=1366, height=100, bg="red")
        self.Information_zone.place(x=-2,y=666)
        #IMAGEN DONDE VA LA INFORMACION
        self.Player_information = PhotoImage(file="Texture_Wood_planks_550067_1366x768.png")
        self.Player_information_place = self.Information_zone.create_image(685, 386, image=self.Player_information)


# game window

Home_window = Tk()
principal_window = Principal_Window(Home_window)
Home_window.title("¡SPACE INVADERS!")
Home_window.config(bg="gray11")
Home_window.geometry("1366x768")
Home_window.resizable(False, False)
Home_window.mainloop()

#It's going to be a repeat semester
