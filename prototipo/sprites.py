import pygame

class Sprites:
    def __init__(self):
        self.__ground_sprite = pygame.sprite.Group()
        self.__player_sprite = pygame.sprite.GroupSingle()

    @property
    def ground_sprite(self):
        return self.__ground_sprite

    @property
    def player_sprite(self):
        return self.__player_sprite