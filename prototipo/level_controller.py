import pygame
from ground import Ground
from player import Player
from sprites import Sprites
from draw import Draw
from map import Map
from colision import Colision

class LevelController:
    def __init__(self, current_level, surface):
        self.__display_surface = surface
        self.__level_shift = 0
        self.__ground = Sprites().ground_sprite
        self.__player = Sprites().player_sprite
        self.__level = current_level
 
    def setup_leve(self):
        for line_index, line in enumerate (self.__level):
            for colum_index, colum in enumerate(line):
                x = colum_index * Map().ground_size
                y = line_index * Map().ground_size

                if colum == "X":
                    ground = Ground((x,y), Map().ground_size)
                    self.__ground.add(ground)
                if colum == "P":
                    player = Player((x,y))
                    self.__player.add(player)
    
    def map_scroll(self):
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

    def colision_control(self):
        colision = Colision().apply_colission
        colision(self.__ground, self.__player.sprite)
              
    def draw_control(self):
        draw = Draw().draw
        draw(self.__ground, self.__display_surface)
        draw(self.__player, self.__display_surface)

    def update(self):
        self.__ground.update(self.__level_shift)
        self.__player.update()

    def run(self):
        self.draw_control()
        self.update()
        self.map_scroll() 
        self.colision_control()





    