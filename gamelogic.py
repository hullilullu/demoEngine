import pygame
from engine import collisions


def update_gameobject_positions(game_objects):
	for obj in game_objects:
		obj.update_pos()


def iterate_one_time(stage_data, input_data, delta_time, sound_handler):

	go = stage_data.game_objects
	tiles = stage_data.tiles



	if input_data.up and go[0].grounded:
		sound_handler.play_sound("Explosion")
		go[0].velocity[1] = -go[0].jump_power
	if input_data.right:
		go[0].right = True
		if go[0].grounded:
			go[0].set_state("WALK")
		go[0].velocity[0] = go[0].walk_speed
	if input_data.left:
		go[0].right = False
		if go[0].grounded:
			go[0].set_state("WALK")
		go[0].velocity[0] = -go[0].walk_speed
	if not (input_data.left or input_data.right):
		go[0].set_state("IDLE")
		go[0].velocity[0] = 0
	if not go[0].grounded:
		go[0].set_state("JUMP")

	for o in go:
		o.grounded = False
		if o.gravity:
			o.velocity[1] += 0.3



	collisions.handle_collisions(go, tiles)

	collisions.handle_damage(go)

	update_gameobject_positions(go)


