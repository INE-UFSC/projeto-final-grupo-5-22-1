import pygame
from animated_objects import AnimatedObject

class Player(AnimatedObject):
    def __init__(self, size, position, path):
        super().__init__(size, position, path)
        self.__animations = {'idle' : [], 'run' : [], 'jump' : [], 'fall' : []}
        self.__direction = pygame.math.Vector2(0,1)
        self.__speed = 4
        self.__jump_height = 13
        self.__jumping = False
        self.__on_ground = True
        self.__on_right = True
        self.__status = 'idle'

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def jumping(self):
        return self.__jumping

    @property
    def direction(self):
        return self.__direction

    @property
    def on_ground(self):
        return self.__on_ground

    @on_ground.setter
    def on_ground(self, on_ground):
        self.__on_ground = on_ground

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @jumping.setter
    def jumping(self, jumping):
        self.__jumping = jumping

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.__on_right = True
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.__on_right = False
        else:
            self.direction.x = 0

        self.rect.x += self.__direction.x * self.__speed

    def jump(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            if self.__jumping == False:
                self.direction.y =  -(self.__jump_height)  
                self.__jumping = True 
                self.on_ground = False
   
    def status_update(self):
        if self.__on_ground == True:
            self.__jumping = False
        elif self.__jumping == True:
            self.__on_ground = False
        if self.__direction.y < 0 :
            self.__status = 'jump'
        elif self.__direction.y > 1 :
            self.__status = 'fall'
        else:
            if self.__direction.x != 0:
                self.__status = 'run'
            else:
                self.__status = 'idle'

    def character_assets(self):
        character_path = '../Jogo_sprites/Player/'

        for animation in self.__animations.keys():
            animation_path = character_path + animation
            self.__animations[animation] = self.frames = self.import_folder(animation_path)

    def gravity_effect(self):
        self.direction.y += 0.5
        self.rect.y += self.direction.y

    def animate(self):
        animation = self.__animations[self.__status]

        self.frame_index += 0.15
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = self.image = animation[int(self.frame_index)]
        if self.__on_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)
        
    def update(self):
        self.animate()
        self.move()
        self.jump()
        self.status_update()

    

        

        
    