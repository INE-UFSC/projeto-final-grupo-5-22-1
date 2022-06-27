import pygame
from tiles import Tile

class Ground(Tile):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.image.fill("green")
