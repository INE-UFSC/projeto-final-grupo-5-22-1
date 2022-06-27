import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.__image = pygame.Surface((size, size))
        self.__rect = self.image.get_rect(topleft = position)

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    def update(self, x_shift):
        self.rect.x += x_shift