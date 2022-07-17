from level_controller import LevelController
from map import Map
from screen import Screen

class Level:
    def __init__(self, screen):
        self.__map = Map()
        self.__level1 = LevelController(self.__map.map1, screen)

    @property
    def level1(self):
        return self.__level1