import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.__image = pygame.Surface((30, 30))
        self.__image.fill("yellow")
        self.__rect = self.image.get_rect(topleft = position)
        self.__collected = False
   
    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
        
    @property
    def collected(self):
        return self.__collected

    @collected.setter
    def collected(self, collected):
        self.__collected = collected

    def update(self, x_shift):
        self.rect.x += x_shift

    