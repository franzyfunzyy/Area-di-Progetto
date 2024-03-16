import pygame as pg
import pygame_widgets 
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from Bottone import Bottone
window_size = (1000, 667)

FPS = 60

def refresh():
    pg.display.update()
    pg.time.Clock().tick(FPS)


class Impostazioni():
    @staticmethod
    def impostazioni() -> None:
        pg.init()
        screen = pg.display.set_mode(window_size)
        pg.display.set_caption("Impostazioni")
        screen.fill('white')

        sfondo = pg.image.load('C:\\Users\\franzyfrunzyy\\Dropbox\\PC\\Documents\\Flow_Inf\\Python\\AreaDiProgetto\\data\\Images\\settings_prova.jpeg')
        screen.blit(sfondo, (0,0))
        
        #Volume Principale
        sliderP = Slider(screen, 430, 100, 200, 20, min=0, max=99, step=1)
        outputP = TextBox(screen, 508, 140, 50, 50, fontSize=30)
        vp = TextBox(screen, 410, 30, 238, 50, fontSize=30)

        #Volume suoni
        sliderS = Slider(screen, 430, 320, 200, 20, min=0, max=99, step=1)
        outputS = TextBox(screen, 508, 360, 50, 50, fontSize=30)
        vs = TextBox(screen, 410, 250, 238, 50, fontSize=30)

        #Volume effetti
        sliderE = Slider(screen, 430, 550, 200, 20, min=0, max=99, step=1)
        outputE = TextBox(screen, 508, 590, 50, 50, fontSize=30)
        ve = TextBox(screen, 410, 480, 238, 50, fontSize=30)

        
        

        outputP.disable()
        outputS.disable()
        outputE.disable()

        vs.disable()
        ve.disable()
        vp.disable()
        exit = Bottone('C:\\Users\\franzyfrunzyy\\Dropbox\\PC\\Documents\\Flow_Inf\\Python\\AreaDiProgetto\\data\\Images\\EXIT.png', screen, 850, 590)
        running = True
        while running:

            for e in pg.event.get():
                pos = pg.mouse.get_pos()
                if e.type == pg.QUIT:
                    pg.quit()
                    exit()
                if e.type == pg.MOUSEBUTTONDOWN:
                    if exit.rect.collidepoint(pos):
                        running = False
                        return sliderS.getValue(), sliderE.getValue()
                
            vp.setText("Volume Principale")
            vs.setText("   Volume Suoni")
            ve.setText("   Volume Effetti")
            outputP.setText(sliderP.getValue())
            outputS.setText(sliderS.getValue())
            outputE.setText(sliderE.getValue())

            
            pygame_widgets.update(sliderP)
            pygame_widgets.update(sliderS)
            pygame_widgets.update(sliderE)

            refresh()

            

    
    
                    
                