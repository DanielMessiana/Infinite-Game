import random as rand
import numpy as np
import pygame, time, sys

rand.seed()

pygame.init()
width, height = 1200, 1000
background_size = 630
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
titleFont = pygame.font.Font(None, 130)
font = pygame.font.Font(None, 50)
main = True

white = (255, 255, 255)
light_grey = (10, 10, 10)
black = (0, 0, 0)

titletext = font.render("The Infinite Game" , True, light_grey)
titletextRect = titletext.get_rect()
titletextRect.center = (width / 2, 100)

turn = 0
turntext = font.render("Turn: Builder", True, black)
turntextRect = turntext.get_rect()
turntextRect.center = (width / 2, 850)

game_surface = pygame.Surface((width, height), pygame.SRCALPHA)

class Game():
	## Game instance

	def __init__(self, size=4):
		self.size = size
		self.squares = np.zeros(size*size)

		self.xcoords = np.arange(300, 150*(size+2), 150)
		self.ycoords = np.arange(200, 150*(size+1), 150)

	def draw_squares(self, game_surface):
		xcoords = self.xcoords
		ycoords = self.ycoords
		col = 0
		row = 0

		for square in self.squares:
			if square == 0:
				pygame.draw.rect(game_surface, white, (xcoords[col], ycoords[row], 148, 148))

			elif square == 1:
				pygame.draw.rect(game_surface, white, (xcoords[col], ycoords[row], 148, 148))
				pygame.draw.rect(game_surface, black, (xcoords[col]+1, ycoords[row]+1, 146, 146))

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
				if (pos[0] > xcoords[col] and pos[0] < xcoords[col]+150) and (pos[1] > ycoords[row] and pos[1] < ycoords[row]+150):
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
				if (pos[0] > xcoords[col] and pos[0] < xcoords[col]+150) and (pos[1] > ycoords[row] and pos[1] < ycoords[row]+150):
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
			if (mouse[0] > 285 and mouse[0] < 285+background_size) and (mouse[1] > 185 and mouse[1] < 185+background_size):
				if turn == 0:
					instance.build(mouse)
				elif turn == 1:
					instance.slash(mouse)

				turn = 1 - turn
				if turn == 0:
					turntext = font.render("Turn: Builder", True, black)
				if turn == 1:
					turntext = font.render("Turn: Slasher", True, black)

	game_surface.fill((0, 0, 0, 0))
	pygame.draw.rect(game_surface, black, (285, 185, background_size, background_size))

	instance.draw_squares(game_surface)
	screen.blit(game_surface, (0, 0))

	screen.blit(titletext, titletextRect)
	screen.blit(turntext, turntextRect)

	pygame.display.flip()

	clock.tick(30)

pygame.quit()
sys.exit()
