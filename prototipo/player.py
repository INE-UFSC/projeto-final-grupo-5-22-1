import pygame
from character import Character

class Player(Character):
    def __init__(self, pos):
        super().__init__(pos)
        self.color = self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)
        self.__speed = 4
        self.__jump_height = 13
        self.__jumpping = False

    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def jumpping(self):
        return self.__jumpping

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        self.rect.x += self.direction.x * self.__speed

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
        else:
            self.__jumpping = True
        
    def update(self):
        self.move()
        self.jump()
        self.status_update()

    

        

        
    