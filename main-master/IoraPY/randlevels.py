#import pygame
import random

import pygame
import os
import background
import sprites
import projectiles
import player
import level
import titleScreen
import time

# Returns a randomly generated 2d array
def genlevel():
	level = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-','-','-','!']]
	choices = ['-', '-','X','#', '-','-']
	temp = []
	enemy_count = 0
	box_count = 0
	enemy_row = 0
	box_row = 0
	#print("L2: ", L2)
	for x in range(0,7):
		temp.clear()
		for y in range(0,12):
			tile = choices[random.randint(0,5)]
			if tile == 'X':
				enemy_row += 1
				if enemy_row > 2 or enemy_count > 12 or x == 0 or y == 0:
					tile = '-'
			elif tile == '#':
				box_row += 1
				print("Box count: ", box_count)
				if box_row > 1 or box_count > 8 or x == 0 or y == 0:
					tile = '-'
			temp.append(tile)
		level.append(temp)
		#print(L2)
		#temp.clear()
		print(box_count)
		print(enemy_count)
		box_row = 0
		enemy_row = 0
		box_count += box_row
		enemy_count += enemy_row
	return level
