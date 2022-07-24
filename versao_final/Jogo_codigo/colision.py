from player import Player
from powerup import Powerup


class Colision:
    def __init__(self):
        pass

    def player_ground_horizontal_colison(self, ground, player):
        for ground_sprite in ground:
            if player.rect.colliderect(ground_sprite.rect):
                if player.direction.x < 0:
                    player.rect.left = ground_sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = ground_sprite.rect.left
                else:
                    player.change_health(-10)
                        
    def player_ground_vertical_colison(self, ground, player):
        player.gravity_effect()
        for ground_sprite in ground:
                if player.rect.colliderect(ground_sprite.rect):
                    if player.direction.y < 0:
                        player.rect.top = ground_sprite.rect.bottom
                        player.direction.y = 0
                    elif player.direction.y > 0.5:
                            player.rect.bottom = ground_sprite.rect.top
                            player.direction.y = 0
                            player.on_ground = True
                            player.jumping = False

    def player_enemy_colision(self, enemy, player):
        for enemy_sprite in enemy:
            if player.rect.colliderect(enemy_sprite.rect):
                if enemy_sprite.rect.top < player.rect.bottom < enemy_sprite.rect.centery and player.status == "fall":
                    player.direction.y = -player.jump_height
                    enemy_sprite.dead = True
                else:
                    player.change_health(enemy_sprite.power)

    def enemy_limiter_colision(self, limiter, enemy):
        for limiter_sprite in limiter:
            for enemy_sprite in enemy:
                if enemy_sprite.rect.colliderect(limiter_sprite.rect):
                    enemy_sprite.reverse_side()

    def player_coin_colision(self, coin, player):
        for coin_sprite in coin:
            if player.rect.colliderect(coin_sprite.rect):
                coin_sprite.collected = True
    
    def player_powerup_colision(self, powerup, player):
        for powerup_sprite in powerup:
            if player.rect.colliderect(powerup_sprite.rect):
                powerup_sprite.effect(player)
                print(player.speed, player.jump_height, player.cur_health)
                powerup_sprite.kill()
                
