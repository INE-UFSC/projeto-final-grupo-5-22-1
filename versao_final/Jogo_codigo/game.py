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
        self.__level = Level(self.__screen).levels[1]

    def start_game(self):
        pygame.init()
        bg = pygame.transform.scale(pygame.image.load("images_overworld/background.png"),(1200,700))
        while self.__running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit() 
                    sys.exit()

            self.__screen.blit(bg, (0, 0))
            #self.__screen.fill((200,200,200))
            self.__level.run() 

            pygame.display.update()
            self.__clock.tick(self.__FPS)

#game = Game()
#game.start_game()
