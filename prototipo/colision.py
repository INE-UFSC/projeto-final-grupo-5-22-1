import pygame
from enemy import Enemy
from ground import Ground
from limiter import Limiter
from coin import Coin

class Colision:
    def __init__(self):
        pass

    def player_horizontal_colison(self, collidable_obj, player):
        for sprite in collidable_obj:
            if not isinstance(sprite, Limiter):
                if sprite.rect.colliderect(player.rect):
                    if isinstance(sprite, Coin):
                        sprite.collected = True
                        collidable_obj.remove(sprite)
                    else:
                        if not isinstance(sprite, Enemy):
                            if player.direction.x < 0:
                                player.rect.left = sprite.rect.right
                            elif player.direction.x > 0:
                                player.rect.right = sprite.rect.left

                            
    def player_vertical_colison(self, collidable_obj, player):
        player.gravity_effect()
        for sprite in collidable_obj:
            if not isinstance (sprite, Limiter):
                if sprite.rect.colliderect(player.rect):
                    if isinstance(sprite, Coin):
                        sprite.collected = True
                        collidable_obj.remove(sprite)
                    else:
                        if player.direction.y < 0:
                            if not isinstance(sprite, Enemy):
                                player.rect.top = sprite.rect.bottom
                                player.direction.y = 0
                        elif player.direction.y > 0.5:
                            if not isinstance(sprite, Enemy):
                                player.rect.bottom = sprite.rect.top
                                player.direction.y = 0
                                player.on_ground = True
                            if isinstance(sprite, Enemy):
                                sprite.dead = True
                                collidable_obj.remove(sprite)

                elif player.jumpping == False:
                    player.on_ground = False
                            

    def enemy_colision(self, collidable_obj, enemy):
        for spriteG in collidable_obj:
            for spriteE in enemy:
                if (isinstance(spriteG, Ground)) or (isinstance)(spriteG, Limiter):
                    if spriteE.rect.colliderect(spriteG.rect):
                        spriteE.reverse()


    def apply_colission(self,collidable_obj, player):
        self.player_horizontal_colison(collidable_obj, player)
        self.player_vertical_colison(collidable_obj, player)
    
    def apply_enemy_colision(self, collidable_obj, enemy):
        self.enemy_colision(collidable_obj, enemy)

