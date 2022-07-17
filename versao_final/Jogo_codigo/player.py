import pygame
from animated_objects import AnimatedObject

class Player(AnimatedObject):
    def __init__(self, size, position, path):
        super().__init__(size, position, path)
        self.__animations = {'idle' : [], 'run' : [], 'jump' : []}
        self.__direction = pygame.math.Vector2(0,1)
        self.__speed = 4
        self.__jump_height = 15
        self.__jumpping = False
        self.__on_ground = True
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def jumpping(self):
        return self.__jumpping

    @jumpping.setter
    def jumping(self, jumpping):
        self.__jumpping = jumpping

    @property
    def on_ground(self):
        return self.__on_ground

    @on_ground.setter
    def on_ground(self,on_ground):
        self.__on_ground = on_ground

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, direction):
        self.__direction = direction


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        self.rect.x += self.__direction.x * self.__speed

    def jump(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            if self.__jumpping == False and self.__on_ground == True:
                self.direction.y =  -(self.__jump_height)  
                self.__jumpping = True
                self.on_ground = False

            

    def status_update(self):
        if self.__on_ground == True:
            self.__jumpping = False
        elif self.__jumpping == True:
            self.__on_ground = False
            

    def character_assets(self, sprite_path):
        character_path = sprite_path

        for animation in self.__animations.keys():
            animation_path = character_path + animation
            self.__animations[animation] = self.frames = self.list_images(animation_path)

    def gravity_effect(self):
        self.direction.y += 0.7
        self.rect.y += self.direction.y
        
    def update(self):
        self.move()
        self.jump()
        self.status_update()

    

        

        
    