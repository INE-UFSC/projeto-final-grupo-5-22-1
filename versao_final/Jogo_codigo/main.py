from time import sleep
import pygame, sys
from Overworld import Overworld
from OverworldController import OverworldController


class Main:
	def __init__(self):
		self.max_level = 1
		self.screen = pygame.display.set_mode((1200,700))
		self.overworld = OverworldController(0,self.max_level,self.screen,self.create_level)
		self.status = 'overworld'

	def create_level(self,current_level):
		self.level = Overworld(current_level,self.screen,self.create_overworld)
		self.status = 'level'

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
			
		else:
			self.level.run()
			sleep(2)
			self.level.start()

	def start(self):
		pygame.init()
		
		clock = pygame.time.Clock()
		main = Main()
		bg = pygame.transform.scale(pygame.image.load("images_overworld/background.png"),(1200,700))

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.blit(bg, (0, 0))
			main.run()

			pygame.display.update()
			clock.tick(60)

