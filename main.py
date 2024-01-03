import random as rand
import numpy as np
import pygame, time, sys

rand.seed()

pygame.init()
width, height = 1400, 960
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
main = True

white = (255, 255, 255)
black = (0, 0, 0)

turn = 0
turntext = font.render("Turn: " + str(turn), True, black)
turntextRect = turntext.get_rect()
turntextRect.center = (width / 2, 850)

game_surface = pygame.Surface((width, height), pygame.SRCALPHA)

class Game():
	## Game instance

	def __init__(self, size=4):
		self.size = size
		self.squares = np.zeros(size*size)

		self.xcoords = np.arange(100, 100*(size+1), 100)
		self.ycoords = np.arange(100, 100*(size+1), 100)

	def draw_squares(self, game_surface):
		xcoords = self.xcoords
		ycoords = self.ycoords
		col = 0
		row = 0

		for square in self.squares:
			if square == 0:
				pygame.draw.rect(game_surface, white, (xcoords[col], ycoords[row], 98, 98))

			elif square == 1:
				pygame.draw.rect(game_surface, black, (xcoords[col], ycoords[row], 96, 96))

			col += 1
			if col == self.size:
				row += 1
				col = 0

	def build(self, pos):
		xcoords = self.xcoords
		ycoords = self.ycoords
		col = 0
		row = 0

		for i, square in enumerate(self.squares):
			if square == 0:
				if (pos[0] > xcoords[col] and pos[0] < xcoords[col]+100) and (pos[1] > ycoords[row] and pos[1] < ycoords[row]+100):
					self.squares[i] = 1
					break

			col += 1
			if col == self.size:
				row += 1
				col = 0

	def slash(self, pos):
		xcoords = self.xcoords
		ycoords = self.ycoords
		col = 0
		row = 0

		for i, square in enumerate(self.squares):
			if square == 1:
				if (pos[0] > xcoords[col] and pos[0] < xcoords[col]+100) and (pos[1] > ycoords[row] and pos[1] < ycoords[row]+100):
					self.squares[i] = 0
					break
			
			col += 1
			if col == self.size:
				row += 1
				col = 0

instance = Game()

while main:
	screen.fill(white)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			main = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			if turn == 0:
				instance.build(mouse)
			elif turn == 1:
				instance.slash(mouse)
			turn = 1 - turn
			turntext = font.render("Turn: " + str(turn), True, black)

	game_surface.fill((0, 0, 0, 0))
	pygame.draw.rect(game_surface, black, (50, 50, 700, 700))

	instance.draw_squares(game_surface)
	screen.blit(game_surface, (0, 0))

	screen.blit(turntext, turntextRect)

	pygame.display.flip()

	clock.tick(30)

pygame.quit()
sys.exit()
