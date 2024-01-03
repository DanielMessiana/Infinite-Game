import random as rand
import numpy as np
import pygame, time, sys

rand.seed()

class Game():
	## Game instance

	def __init__(self, size=5):
		self.size = size
		self.squares = np.zeros(size*size)

		self.xcoords = np.arange(100, 100*(size+1), 100)
		self.ycoords = np.arange(100, 100*(size+1), 100)

	def draw_squares(self):
		xcoords = self.xcoords
		ycoords = self.ycoords
		col = 1
		row = 1

		for square in self.squares:
			if square == 0:
				pygame.draw.rect(game_surface, white, (xcoords[col-1], ycoords[row-1], 98, 98))

			else:
				pygame.draw.rect(game_surface, black, (xcoords[col-1], ycoords[row-1], 96, 96))

			col += 1
			if col == self.size+1:
				row += 1
				col = 1

instance = Game()

pygame.init()
width, height = 1400, 960
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
main = True

white = (255, 255, 255)
black = (0, 0, 0)

game_surface = pygame.Surface((width, height), pygame.SRCALPHA)

font = pygame.font.Font(None, 40)

while main:
	screen.fill(white)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			main = False

	game_surface.fill((0, 0, 0, 0))
	pygame.draw.rect(game_surface, black, (50, 50, 700, 700))

	instance.draw_squares()
	screen.blit(game_surface, (0, 0))

	mouse = pygame.mouse.get_pos()

	if mouse 

	pygame.display.flip()

pygame.quit()
sys.exit()
