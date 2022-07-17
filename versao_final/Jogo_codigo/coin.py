from animated_objects import AnimatedObject

class Coin(AnimatedObject):
    def __init__(self, size, position, path):
        super().__init__(size, position, path)
        self.__rect = self.image.get_rect(center = ((position[0] + int(size/2)), (position[1] + int(size/2))))
        self.__collected = False
        
    @property
    def rect(self):
        return self.__rect
        
    @property
    def collected(self):
        return self.__collected

    @collected.setter
    def collected(self, collected):
        self.__collected = collected

    