import pygame

class Sprites:
    def __init__(self):
        self.__ground_sprite = pygame.sprite.Group()
        self.__player_sprite = pygame.sprite.GroupSingle()
        self.__enemy_sprite = pygame.sprite.Group()
        self.__limiter = pygame.sprite.Group()
        self.__coin_sprite = pygame.sprite.Group()

    @property
    def ground_sprite(self):
        return self.__ground_sprite

    @property
    def player_sprite(self):
        return self.__player_sprite

    @property
    def enemy_sprite(self):
        return self.__enemy_sprite

    @property
    def limiter(self):
        return self.__limiter

    @property
    def coin_sprite(self):
        return self.__coin_sprite
    
