import pygame


class Icon(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.__pos = pos
		self.__image = pygame.transform.scale(pygame.image.load('images_overworld/luigii.png'),(50,50))
		self.__rect = self.image.get_rect(center = pos)

	@property
	def pos(self):
		return self.__pos

	@property
	def image(self):
		return self.__image

	@property
	def rect(self):
		return self.__rect

	def update(self):
		self.rect.center = self.pos


