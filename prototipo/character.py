import pygame
from abc import ABC, abstractmethod
from map import Map
from random import randint

class Character(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, pos):
        super().__init__()
        self.__image = pygame.Surface((32,64))
        self.__color = self.__image.fill("blue")
        self.__rect = self.__image.get_rect(topleft = pos)
        self.__direction = pygame.math.Vector2(0,1)
        self.__speed = randint(1,3)
        self.__on_ground = True
        self.__dead = False

    @property
    def on_ground(self):
        return self.__on_ground

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def image(self):
        return self.__image

    @property
    def direction(self):
        return self.__direction

    @on_ground.setter
    def on_ground(self, value):
        self.__on_ground = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def dead(self):
        return self.__dead

    @dead.setter
    def dead(self, dead):
        self.__dead = dead
    
    def move(self):
        self.__rect.x -= self.__speed

    def update(self,x_shift):
        self.rect.x += x_shift
        self.move()

    def gravity_effect(self):
        gravity = Map().gravity
        self.direction.y += gravity
        self.rect.y += self.direction.y