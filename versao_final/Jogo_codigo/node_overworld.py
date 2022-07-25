import pygame

class Node(pygame.sprite.Sprite):
	def __init__(self,pos,status,icon_speed):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load('images_overworld/ilha2.png'),(400,300))
		self.rect = self.image.get_rect(center = pos)
		self.detection_zone = pygame.Rect(self.rect.centerx-(icon_speed/2),self.rect.centery-(icon_speed/2),icon_speed,icon_speed)
