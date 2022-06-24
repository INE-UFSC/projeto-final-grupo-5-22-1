from level_controller import LevelController
from map import Map
from screen import Screen

class Level:
    def __init__(self):
        self.__level1 = LevelController(Map().map1, Screen().screen)

    @property
    def level1(self):
        return self.__level1

        
