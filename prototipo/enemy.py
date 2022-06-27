import pygame
from character import Character

class Enemy(Character):
    def __init__(self, pos):
        super().__init__(pos)

    def reverse(self):
        self.speed *= -1

