import pygame
from abc import ABC, abstractmethod
from map import Map

class Character(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.__on_ground = True

    @property
    def on_ground(self):
        return self.__on_ground

    @on_ground.setter
    def on_ground(self, value):
        self.__on_ground = value

    @abstractmethod
    def move():
        pass

    def update():
        pass

    def gravity_effect(self):
        gravity = Map().gravity
        self.direction.y += gravity
        self.rect.y += self.direction.y