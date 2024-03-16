import pygame as pg
from pygame import Surface

class Bottone():
    def __init__(self, percorso : str, screen : Surface, x : int, y : int) -> None:
        self.surface = pg.image.load(percorso)
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)
        screen.blit(self.surface, (x, y))
        
    
