import random as rand
import numpy as np
import pygame, time, sys

rand.seed()

class Game():

	def __init__(self, size=4):
		self.size = size

		self.squares = np.zeros(size*size)

	def draw_squares(self):
		col = 1
		x, y = 102, 102
		for i, square in enumerate(self.squares):
			if square == 0:
				pygame.draw.rect(game_surface, white, (x*col, y, 98, 98))

			else:
				pygame.draw.rect(game_surface, black, (x*col, y, 96, 96))

			col += 1
			if col == self.size+1:
				col = 1
				y += 102

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
	pygame.draw.rect(game_surface, black, (50, 50, 500, 500))

	instance.draw_squares()
	

	screen.blit(game_surface, (0, 0))

	pygame.display.flip()

pygame.quit()
sys.exit()
