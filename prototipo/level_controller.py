from ground import Ground
from player import Player
from enemy import Enemy
from limiter import Limiter
from score import Score
from sprites import Sprites
from draw import Draw
from map import Map
from colision import Colision
from coin import Coin


class LevelController:
    def __init__(self, current_level, surface):
        self.__draw = Draw()
        self.__sprite = Sprites()
        self.__display_surface = surface
        self.__level_shift = 0
        self.__ground = self.__sprite.ground_sprite
        self.__player = self.__sprite.player_sprite
        self.__enemy = self.__sprite.enemy_sprite
        self.__limiter = self.__sprite.limiter
        self.__coin = self.__sprite.coin_sprite
        self.__collidable_sprites = None
        self.__level = current_level
        self.__score = Score()
        self.__colision = Colision()

    def setup_leve(self):
        for line_index, line in enumerate (self.__level):
            for colum_index, colum in enumerate(line):
                ground_size = Map().ground_size
                x = colum_index * ground_size
                y = line_index * ground_size

                if colum == "X":
                    ground = Ground((x,y), ground_size)
                    self.__ground.add(ground)
                if colum == "P":
                    player = Player((x,y))
                    self.__player.add(player)
                if colum == "E":
                    enemy = Enemy((x,y))
                    self.__enemy.add(enemy)
                if colum == "L":
                    limiter = Limiter((x,y), ground_size)
                    self.__limiter.add(limiter)
                if colum == "C":
                    coin = Coin((x,y))
                    self.__coin.add(coin)

        self.__collidable_sprites = self.__ground.sprites() + self.__enemy.sprites() + self.__limiter.sprites() + self.__coin.sprites()
        
    def mapa_limiter(self):
        player = self.__player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < 30 and direction_x < 0:
            player.speed = 0
        elif player_x > 1000 and direction_x > 0:
            self.__level_shift = -4
            player.speed = 0
        else:
            self.__level_shift = 0
            player.speed = 4

        for sprite in self.__enemy.sprites():
            enemy_x = sprite.rect.x
            if self.__enemy.sprites() != []:
                if enemy_x == 10  :
                    sprite.reverse()

    def colision_control(self):
        self.__colision.apply_colission(self.__collidable_sprites, self.__player.sprite)
        self.__colision.apply_enemy_colision(self.__collidable_sprites, self.__enemy.sprites())
       
              
    def draw_control(self):
        #draw = self.__draw.draw
        #write = self.__draw.write_screen
        self.__draw.draw(self.__ground, self.__display_surface)
        self.__draw.draw(self.__player, self.__display_surface)
        self.__draw.draw(self.__enemy, self.__display_surface)
        self.__draw.draw(self.__coin, self.__display_surface)
        self.__draw.write_screen(f"Score: {self.__score.score}", self.__display_surface, (30, 30))

    def update(self):
        self.__ground.update(self.__level_shift)
        self.__player.update()
        self.__enemy.update(self.__level_shift)
        self.__limiter.update(self.__level_shift)
        self.__coin.update(self.__level_shift)

    def check_alive(self):
        for sprite in self.__enemy.sprites():
            if sprite.dead == True:
                self.__enemy.remove(sprite)

        for sprite in self.__coin.sprites():
            if sprite.collected == True:
                self.__coin.remove(sprite)

    def score(self):
        for sprite in self.__coin.sprites():
            if sprite.collected == True:
                self.__score.update()

    def run(self):
        self.draw_control()
        self.update()
        self.mapa_limiter() 
        self.colision_control()
        self.score()
        self.check_alive()
  





    