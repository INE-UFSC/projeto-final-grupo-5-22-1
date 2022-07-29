import pygame 
from game import Game	
class LevelOverworld:
	def __init__(self,current_level,surface,create_overworld):

		self.__display_surface = surface 
		self.__current_level = current_level
		self.__levels = [
		{'node_pos':(300,450), 'content': 'this is level 1','unlock':1},
		{'node_pos':(600,300), 'content': 'this is level 2','unlock':2},
		{'node_pos':(900,450), 'content': 'this is level 3', 'unlock':2}]
		level_content = self.levels[current_level]['content']
		self.__new_max_level = self.levels[current_level]['unlock']
		self.__create_overworld = create_overworld
		self.__font = pygame.font.Font(None,40)
		self.__text_surf = self.font.render(level_content,True,'White')
		self.__text_rect = self.text_surf.get_rect(center = (1280 / 2, 720 / 2))

	@property
	def display_surface(self):
		return self.__display_surface

	@property
	def current_level(self):
		return self.__current_level
	
	@property
	def levels(self):
		return self.__levels

	@property
	def new_max_level(self):
		return self.__new_max_level

	@property
	def create_overworld(self):
		return self.__display_surface
	
	@property
	def font(self):
		return self.__font
	
	@property
	def text_surf(self):
		return self.__text_surf

	@property
	def text_rect(self):
		return self.__text_rect

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			self.create_overworld(self.current_level,self.new_max_level)
		if keys[pygame.K_ESCAPE]:
			self.create_overworld(self.current_level,1)

	def start(self):
		Game().start_game()

	def run(self):
		self.input()
		self.__display_surface.blit(self.text_surf,self.text_rect)
		pygame.display.flip()

