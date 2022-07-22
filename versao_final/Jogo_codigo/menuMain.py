from menu import Menu

class menuMain(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 20
        self.scorex, self.scorey = self.mid_w, self.mid_h + 60
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            #self.game.display.fill(self.game.WHITE)
            self.game.display.blit(self.game.menu_image, (0, 0))
            self.game.draw_text("Start Game", 35, self.startx, self.starty -65)
            self.game.draw_text("Score", 35, self.scorex, self.scorey -65)
            self.game.draw_text("Credits", 35, self.creditsx, self.creditsy -65)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.scorex + self.offset, self.scorey)
                self.state = 'Score'
            elif self.state == 'Score':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Score':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.scorex + self.offset, self.scorey)
                self.state = 'Score'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Score':
                self.game.curr_menu = self.game.score
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False