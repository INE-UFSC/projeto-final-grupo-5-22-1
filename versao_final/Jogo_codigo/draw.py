import pygame
pygame.font.init()

class Draw:
    def __init__(self):
        self.__text_font = pygame.font.SysFont('Bauhaus 93', 40)

    def draw(self, object, surface):
        object.draw(surface)

    def write_screen(self, frase, surface, position):
        text = self.__text_font.render(f"{frase}", True, (255,255,255))
        text_rect = text.get_rect(topleft = position)
        surface.blit(text, text_rect)
        
