import pygame, sys
from pygame.locals import *
from screen import Screen
from level import Level



class Game:
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__FPS = 60
        self.__running = True
        self.__name = pygame.display.set_caption('Mario')
        self.__level = Level().level1

    def start_game(self):
        pygame.init()
        self.__level.setup_leve()
  
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit() 
                    sys.exit()

            Screen().screen.fill("black")
            self.__level.run()

            pygame.display.update()
            self.__clock.tick(self.__FPS)
            

game = Game()
game.start_game()
