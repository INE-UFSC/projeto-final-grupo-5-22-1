from time import sleep
import pygame, sys
from LevelOverworld import LevelOverworld
from Overworld import Overworld


class Main:
	def __init__(self):
		self.max_level = 2
		self.screen = pygame.display.set_mode((1200,700))
		self.overworld = Overworld(0,self.max_level,self.screen,self.create_level)
		self.status = 'overworld'
		self.BACK_KEY = False
		self.running = True

	def create_level(self,current_level):
		self.level = LevelOverworld(current_level,self.screen,self.create_overworld)
		self.status = 'level'

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = LevelOverworld(current_level,self.screen,self.create_level)
		self.status = 'overworld'

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			sleep(2)
			self.level.start()
			self.level.game_over()
			sleep(3)
			self.status = 'overworld'

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					self.BACK_KEY = True
                

	def start(self):
		pygame.init()
		
		clock = pygame.time.Clock()
		bg = pygame.transform.scale(pygame.image.load("images_overworld/background.png"),(1200,700))

		while self.running:
			self.check_events()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				

			self.screen.blit(bg, (0, 0))
			self.run()

			pygame.display.update()
			clock.tick(60)
			if self.BACK_KEY:
				self.running = False
			self.BACK_KEY = False