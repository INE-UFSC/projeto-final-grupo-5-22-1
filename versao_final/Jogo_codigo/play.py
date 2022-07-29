# -*- coding: utf-8 -*-
import pygame
from menuCredits import menuCredits
from menuMain import menuMain
from menuScore import menuScore
from main import Main
from game import Game


class Play():
    def __init__(self):
        pygame.init()
        
        self.__game = Main()

        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1200, 700
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'font/8-BIT WONDER.TTF'

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        self.main_menu = menuMain(self)
        self.score = menuScore(self)
        self.credits = menuCredits(self)
        self.curr_menu = self.main_menu

        self.imageMenu = pygame.image.load('images/mainMenu.png')
        self.menu_image = pygame.transform.scale(self.imageMenu, (self.DISPLAY_W ,self.DISPLAY_H ))

        self.imageCreditos = pygame.image.load('images/creditsMenu.png')
        self.creditos_image = pygame.transform.scale(self.imageCreditos, (self.DISPLAY_W ,self.DISPLAY_H ))

        self.imageScore = pygame.image.load('images/scoreMenu.png')
        self.score_image = pygame.transform.scale(self.imageScore, (self.DISPLAY_W ,self.DISPLAY_H ))

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.BACK_KEY:
                self.playing= False

            #JOGO AQUI
            self.__game.start()

            # self.display.fill(self.BLACK)
            # self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            # self.window.blit(self.display, (0,0))

            pygame.display.update()
            self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                    self.__game.running = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

g = Play()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    g.reset_keys()