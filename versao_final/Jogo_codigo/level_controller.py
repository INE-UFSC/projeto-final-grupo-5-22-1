from score import Score
from sprites import Sprites
from draw import Draw
from colision import Colision
from health import Health


class LevelController:
    def __init__(self, current_level, surface):
        self.__draw = Draw()
        self.__sprite = Sprites()
        self.__score = Score()
        self.__colision = Colision()
        self.__health = Health(surface)
        self.__display_surface = surface
        self.__level_shift = 0
        self.__level = current_level
        self.__ground = self.__sprite.setup_sprite(self.__level, 'ground')
        self.__coins = self.__sprite.setup_sprite(self.__level, 'coins')
        self.__enemys = self.__sprite.setup_sprite(self.__level, 'enemys')
        self.__limiter = self.__sprite.setup_sprite(self.__level, 'limiter')
        self.__player = self.__sprite.setup_sprite(self.__level, 'player')
        

    def mapa_limiter(self):
        player = self.__player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < 300 and direction_x < 0:
            self.__level_shift = 4
            player.speed = 0
        elif player_x > 600 and direction_x > 0:
            self.__level_shift = -4
            player.speed = 0
        else:
            self.__level_shift = 0
            player.speed = 4

        for sprite in self.__enemys.sprites():
            enemy_x = sprite.rect.x
            if self.__enemys.sprites() != []:
                if enemy_x == 10  :
                    sprite.reverse_side()

    def colision_control(self):
        collidable_sprites = self.__enemys.sprites() + self.__coins.sprites() + self.__ground.sprites() \
        + self.__limiter.sprites()
        self.__colision.apply_colission(collidable_sprites, self.__player.sprite)
        self.__colision.apply_enemy_colision(collidable_sprites, self.__enemys.sprites())
                    
    def draw_control(self):
        self.__draw.draw(self.__ground, self.__display_surface)
        self.__draw.draw(self.__player, self.__display_surface)
        self.__draw.draw(self.__enemys, self.__display_surface)
        self.__draw.draw(self.__coins, self.__display_surface)
        self.__draw.write_screen(f"Score: {self.__score.score}", self.__display_surface, (30, 30))

        #self.__draw.draw(self.__health, self.__display_surface)
        self.__health.show_health(self.__player.sprite.cur_health, self.__player.sprite.max_health)

    def update(self):
        self.__ground.update(self.__level_shift)
        self.__coins.update(self.__level_shift)
        self.__enemys.update(self.__level_shift)
        self.__limiter.update(self.__level_shift)
        self.__player.update()

    def check_alive(self):
        for sprite in self.__enemys.sprites():
            if sprite.dead == True:
                self.__enemys.remove(sprite)

        for sprite in self.__coins.sprites():
            if sprite.collected == True:
                self.__coins.remove(sprite)

    def score(self):
        for sprite in self.__coins.sprites():
            if sprite.collected == True:
                self.__score.update()

    def run(self):
        self.draw_control()
        self.update()
        self.mapa_limiter() 
        self.colision_control()
        self.score()
        self.check_alive()
