import glob
import os
import pygame

import input_handling
import gamelogic
import graphics
from engine import data_containers
from sound import sound


def run_intro():
	pass

def run_outro():
	pass

def run_game(screen, input_data, run_data, graphic_handler, clock):

	#stage_data = fileIO.load_stage(run_data.__current_level)
	stage_data = data_containers.StageData(0)
	stage_data.randomize()
	graphic_handler.associate_animations(stage_data.game_objects)
	updateFreq = 60
	deltaTime = 1/updateFreq

	if stage_data:
		run = True
	else:
		run = False

	sounds = glob.glob(os.path.normpath("audio/effects/*"))

	#sounds = glob.glob(os.path.normpath("res/anim/*"))

	print(sounds)

	sound_handler = sound.SoundHandler(sounds, stage_data.music)

	sound_handler.play_music()
	

	while run :

		# INPUT
		input_data.get_input()
		# GAME LOGIC
		gamelogic.iterate_one_time(stage_data, input_data, deltaTime, sound_handler)

		# DRAW
		graphic_handler.draw(stage_data)

		pygame.display.flip()

		# Tick
		clock.tick(updateFreq)

		if input_data.quit:
			sound_handler.exit()
			return True

def run_menu(screen, input_data, run_data, graphic_handler, clock):

	run = True

	#menu_data = rw.load_menu()

	menu_data = data_containers.MenuData(run_data)

	while (run):
		# INPUT
		input_data.get_input()
		# MENU LOGIC
		if input_data.up:
			menu_data.increment()
		elif input_data.down:
			menu_data.decrement()
		elif input_data.enter:
			menu_data.select()

		# DRAW
		graphic_handler.draw_menu(menu_data)
		pygame.display.flip()

		# Tick 
		clock.tick(60)

		if input_data.quit or menu_data.exit:
			return True

		if menu_data.run_game:
			return False


# START OF GAME LOOP

pygame.init()

pygame.font.init()

pygame.mixer.init()

screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size )# , pygame.FULLSCREEN)

g = graphics.GraphicHandler(screen, "res/anim", screen_size)
g.load_graphics( ["res/sprites/test_graphics.jpg", "res/sprites/generalTiles.jpg", "res/sprites/generalMainSmall.jpg"])

clock = pygame.time.Clock()

input_data = input_handling.Input_Data()
run_data = data_containers.RunData(10)

run_intro()

exit = False

while not exit:
	exit = run_menu(screen, input_data, run_data, g, clock)
	if exit:
		break
	exit = run_game(screen, input_data, run_data, g, clock)
	if exit:
		break

run_outro()

pygame.mixer.stop()

pygame.quit()