import pygame

class Colision:
    def __init__(self):
        pass

    def horizontal_ground_colision(self,object_one, object_two):
        for sprite in object_one.sprites():
            if sprite.rect.colliderect(object_two.rect):
                if object_two.direction.x < 0:
                    object_two.rect.left = sprite.rect.right
                elif object_two.direction.x > 0:
                    object_two.rect.right = sprite.rect.left

    def vertical_ground_colision(self,object_one, object_two):
        object_two.gravity_effect()
        for sprite in object_one.sprites():
            if sprite.rect.colliderect(object_two.rect):
                if object_two.direction.y < 0:
                    object_two.rect.top = sprite.rect.bottom
                    object_two.direction.y = 0
                elif object_two.direction.y > 0:
                    object_two.rect.bottom = sprite.rect.top
                    object_two.direction.y = 0

        
    def apply_colission(self,object_one, object_two):
        self.horizontal_ground_colision(object_one, object_two)
        self.vertical_ground_colision(object_one, object_two)