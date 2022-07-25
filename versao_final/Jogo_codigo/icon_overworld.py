import pygame


class Icon(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.pos = pos
		self.image = pygame.transform.scale(pygame.image.load('images_overworld/luigii.png'),(50,50))
		self.rect = self.image.get_rect(center = pos)


	def update(self):
		self.rect.center = self.pos


