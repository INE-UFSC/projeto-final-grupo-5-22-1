from menu import Menu

class menuScore(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()    
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.blit(self.game.score_image, (0, 0))
            #self.game.display.fill((0, 0, 0))
            self.game.draw_text('Score', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.blit_screen()
