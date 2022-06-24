import pygame
from character import Character

class Player(Character):
    def __init__(self, pos):
        super().__init__()
        self.__image = pygame.Surface((32,64))
        self.__image.fill("red")
        self.__rect = self.__image.get_rect(topleft = pos)
        self.__direction = pygame.math.Vector2(0,0)
        self.__speed = 4
        self.__jump_height = 13
        self.__jumpping = False

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
    
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def direction(self):
        return self.__direction
    

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.__direction.x = 1
        elif keys[pygame.K_a]:
            self.__direction.x = -1
        else:
            self.__direction.x = 0

        self.rect.x += self.__direction.x * self.__speed

    def jump(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            if self.__jumpping == False:
                self.direction.y =  -(self.__jump_height)  
                self.__jumpping = True 
                self.on_ground = False

    def status_update(self):
        if self.on_ground == True:
            self.__jumpping = False
        
    def update(self):
        self.move()
        self.jump()
        self.status_update()

        

        
    