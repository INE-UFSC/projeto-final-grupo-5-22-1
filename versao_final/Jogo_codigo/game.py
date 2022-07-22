import pygame, sys
from pygame.locals import *
from screen import Screen
from level import Level

class Game:
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__FPS = 60
        self.__running = True
        self.__screen = Screen().screen
        self.__name = pygame.display.set_caption('Not Mario')
        self.__level = Level(self.__screen).level1

    def start_game(self):
        pygame.init()
  
        while self.__running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit() 
                    sys.exit()
       
            self.__screen.fill("grey")
            self.__level.run()

            pygame.display.update()
            self.__clock.tick(self.__FPS)

# game = Game()
# game.start_game()
