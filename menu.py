import pygame as pg
from Impostazioni import Impostazioni
from Bottone import Bottone
from game import Game


window_size = (900, 600)

class Menu:
    def __init__(self) -> None:
        pg.init()
        screen = pg.display.set_mode((window_size))

        # Creo il bottone per una nuova partita
        
        # NuovaPartita = Bottone('AreaDiProgetto\\Immage\\AnuovaPartita.png', screen, 150, 200)

        pg.display.set_caption("Menu")

        # Carichiamo l'immagine dello sfondo
        sfondo = pg.image.load('C:\\Users\\franzyfrunzyy\\Dropbox\\PC\\Documents\\Flow_Inf\\Python\\AreaDiProgetto\\data\\Images\\Sfondo (1).png')

        # Disegniamo l'immagine sulla superficie
        screen.blit(sfondo, (0,0))

        # Creiamo un bottone per avviare una nuova partita
        NuovaPartita = Bottone('C:\\Users\\franzyfrunzyy\\Dropbox\\PC\\Documents\\Flow_Inf\\Python\\AreaDiProgetto\\data\\Images\\Nuova Partita_NonR (2) (1).png', screen, 75, 150)
        CaricaPartita = Bottone('C:\\Users\\franzyfrunzyy\\Dropbox\\PC\\Documents\\Flow_Inf\\Python\\AreaDiProgetto\\data\\Images\\Carica Partita_NonR (1) (1).png', screen, 75, 220)
        bImpostazioni = Bottone('C:\\Users\\franzyfrunzyy\\Dropbox\\PC\\Documents\\Flow_Inf\\Python\\AreaDiProgetto\\data\\Images\\Impostazioni_NonR (1) (1).png', screen, 75, 290)
        Esci = Bottone('C:\\Users\\franzyfrunzyy\\Dropbox\\PC\\Documents\\Flow_Inf\\Python\AreaDiProgetto\\data\\Images\\Esci_NonR (1) (1).png', screen, 75, 360)

        # Utilizziamo il metodo get_rect() per verificare le collisioni con l'immagine
        pos = pg.mouse.get_pos()
        
        while True:
            for e in pg.event.get():
                pos = pg.mouse.get_pos()
                if e.type == pg.QUIT:
                    pg.quit()
                    exit()
                if e.type == pg.MOUSEBUTTONDOWN:
                    if NuovaPartita.rect.collidepoint(pos):
                        Game().run()
                    elif CaricaPartita.rect.collidepoint(pos):
                        print('Carica Partita')
                    elif bImpostazioni.rect.collidepoint(pos):
                        Impostazioni.impostazioni()
                        Menu()
                    elif Esci.rect.collidepoint(pos):
                        pg.quit()
                        exit()
            
            pg.display.flip()

menu = Menu()


        