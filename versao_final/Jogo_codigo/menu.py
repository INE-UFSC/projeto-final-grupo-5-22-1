import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x -100, self.cursor_rect.y -60) 

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

# class MainMenu(Menu):
#     def __init__(self, game):
#         Menu.__init__(self, game)
#         self.state = "Start"
#         self.startx, self.starty = self.mid_w, self.mid_h + 20
#         self.scorex, self.scorey = self.mid_w, self.mid_h + 60
#         self.creditsx, self.creditsy = self.mid_w, self.mid_h + 100
#         self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

#     def display_menu(self):
#         self.run_display = True
#         while self.run_display:
#             self.game.check_events()
#             self.check_input()
#             #self.game.display.fill(self.game.WHITE)
#             self.game.display.blit(self.game.menu_image, (0, 0))
#             self.game.draw_text("Start Game", 35, self.startx, self.starty -65)
#             self.game.draw_text("Score", 35, self.scorex, self.scorey -65)
#             self.game.draw_text("Credits", 35, self.creditsx, self.creditsy -65)
#             self.draw_cursor()
#             self.blit_screen()


#     def move_cursor(self):
#         if self.game.DOWN_KEY:
#             if self.state == 'Start':
#                 self.cursor_rect.midtop = (self.scorex + self.offset, self.scorey)
#                 self.state = 'Score'
#             elif self.state == 'Score':
#                 self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
#                 self.state = 'Credits'
#             elif self.state == 'Credits':
#                 self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
#                 self.state = 'Start'
#         elif self.game.UP_KEY:
#             if self.state == 'Start':
#                 self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
#                 self.state = 'Credits'
#             elif self.state == 'Score':
#                 self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
#                 self.state = 'Start'
#             elif self.state == 'Credits':
#                 self.cursor_rect.midtop = (self.scorex + self.offset, self.scorey)
#                 self.state = 'Score'

#     def check_input(self):
#         self.move_cursor()
#         if self.game.START_KEY:
#             if self.state == 'Start':
#                 self.game.playing = True
#             elif self.state == 'Score':
#                 self.game.curr_menu = self.game.score
#             elif self.state == 'Credits':
#                 self.game.curr_menu = self.game.credits
#             self.run_display = False

# #SCORE MENU
# class ScoreMenu(Menu):
#     def __init__(self, game):
#         Menu.__init__(self, game)

#     def display_menu(self):
#         self.run_display = True
#         while self.run_display:
#             self.game.check_events()    
#             if self.game.START_KEY or self.game.BACK_KEY:
#                 self.game.curr_menu = self.game.main_menu
#                 self.run_display = False
#             self.game.display.blit(self.game.score_image, (0, 0))
#             #self.game.display.fill((0, 0, 0))
#             self.game.draw_text('Score', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
#             self.blit_screen()


# class CreditsMenu(Menu):
#     def __init__(self, game):
#         Menu.__init__(self, game)

#     def display_menu(self):
#         self.run_display = True
#         while self.run_display:
#             self.game.check_events()
#             if self.game.START_KEY or self.game.BACK_KEY:
#                 self.game.curr_menu = self.game.main_menu
#                 self.run_display = False

#             self.game.display.blit(self.game.creditos_image, (0, 0))
#             #self.game.display.fill(self.game.BLACK)
#             self.game.draw_text('Credits', 45, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 90)
#             self.game.draw_text('Game made by', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -30)
#             self.game.draw_text('Eduardo', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
#             self.game.draw_text('Fillipi', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
#             self.game.draw_text('Livia', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 110)
#             self.game.draw_text('Lucas', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 150)
#             self.blit_screen()

