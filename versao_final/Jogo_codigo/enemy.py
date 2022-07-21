import pygame
from animated_objects import AnimatedObject
from random import randint

class Enemy(AnimatedObject):
    def __init__(self,position, path):
        super().__init__(position, path)
        self.__speed = randint(2, 4)
        self.__dead = False
        self.__power = 10

    @property
    def dead(self):
        return self.__dead
    
    @dead.setter
    def dead(self, dead):
        self.__dead = dead

    @property
    def power(self):
        return self.__power

    def reverse_side(self):
        self.__speed *= -1
        
    def reverse_image(self):
        if self.__speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def move(self):
        self.rect.x -= self.__speed

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate()
        self.move()
        self.reverse_image()
        
