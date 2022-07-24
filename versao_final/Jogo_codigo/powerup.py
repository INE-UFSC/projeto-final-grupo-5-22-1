from random import randint

from animated_objects import AnimatedObject

class Powerup(AnimatedObject):
    def __init__(self, position, path):
        super().__init__(position, path)
        self.__size = 64
        self.__rect = self.image.get_rect(center = ((position[0] + int(self.__size/2)), (position[1] + int(self.__size/2))))

    @property
    def rect(self):
        return self.__rect
    
    def drop_powerup(self, powerup):
            return powerup