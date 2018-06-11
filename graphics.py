import pygame
from animation import animation
from animation import animation_rw


def load_animations(dir):
	return_dict = animation_rw.load_animations_in_dir(dir)

	"""

	return_dict["GO_TEST"] = animation.Animation([animation.Frame("test_graphics.jpg", 0, 0, 70, 85), animation.Frame("test_graphics.jpg", 70, 0, 70, 85)])
	return_dict["IDLE_TEST"] = animation.Animation([animation.Frame("test_graphics.jpg", 0, 0, 70, 85), animation.Frame("test_graphics.jpg", 10, 0, 70, 85)])
	return_dict["IDLE_MAIN"] = animation.Animation([animation.Frame("generalMainSmall.jpg", 42, 42, 99, 126)])
	return_dict["JUMP_MAIN"] = animation.Animation([animation.Frame("generalMainSmall.jpg", 57, 423, 67, 134)])
	return_dict["WALK_MAIN"] = animation.Animation([animation.Frame("generalMainSmall.jpg", 45, 226, 114, 109, offset_x = -15),
		animation.Frame("generalMainSmall.jpg", 262,230, 42, 120, offset_x = 35),
		animation.Frame("generalMainSmall.jpg", 460, 230, 64, 123, offset_x = 13)], 2)

	"""

	return return_dict

def load_images():
	return_dict = {}

	return_dict["BLOCK_1"] = animation.Image("generalTiles.jpg", 0, 0, 49, 49)

	return return_dict


class GraphicHandler:
	def __init__(self, screen, dir, size):
		self.screen = screen
		self.size = size
		self.sheets = {}
		self.animations = load_animations(dir)
		self.images = load_images()
		self.font = pygame.font.SysFont("Comic Sans MS", 20)

	def check_if_on_screen(self, o, camera):
		r = (camera.pos[0]-self.size[0]/2-100, camera.pos[1]-self.size[1]/2-100, self.size[0]/2 + 200, self.size[1]/2 + 200)
		if o.pos[0] + o.wh[0] < r[0] or o.pos[0] > r[0] + r[2] or o.pos[1] > r[0] + r[2] or o.pos[1] > r[1] + r[3]:
			return False
		else:
			return True


		print("ble =",n, true)

	def draw_image(self, pos, image, camera):

		self.screen.blit(self.sheets[image.sheet], 
			(pos[0]+ image.offset_x - camera[0], pos[1] + image.offset_y - camera[1]), 
			pygame.Rect(image.sheet_x, image.sheet_y, image.sheet_w, image.sheet_h))

	def draw_animation(self, pos, animation_tracker, camera, right = False):
		f = animation_tracker.animation.get_frame(animation_tracker.current_index)
		if right:
			self.screen.blit(pygame.transform.flip(self.sheets[f.sheet].subsurface(f.sheet_x, f.sheet_y, f.sheet_w, f.sheet_h), True, False), (pos[0]+ f.offset_x - camera[0], pos[1] + f.offset_y - camera[1])) #, pygame.Rect(f.sheet_x, f.sheet_y, f.sheet_w, f.sheet_h))
		else:
			self.screen.blit(self.sheets[f.sheet], (pos[0]+ f.offset_x - camera[0], pos[1] + f.offset_y - camera[1]), pygame.Rect(f.sheet_x, f.sheet_y, f.sheet_w, f.sheet_h))
	def draw_background(self):
		self.screen.fill((10,10,50))

	def draw(self, data):

		camera = (data.game_objects[0].pos[0] + data.game_objects[0].wh[0]- self.size[0]/2 , data.game_objects[0].pos[1] + data.game_objects[0].wh[1]- self.size[1]/2 )
		
		self.draw_background()

		for tile in data.tiles:
			self.draw_image( tile.pos, self.images[tile.image_name], camera)

		for game_object in data.game_objects:
			self.draw_animation( game_object.pos, game_object.animations[game_object.current_animation] , camera, game_object.right)
			game_object.animations[game_object.current_animation].iterate()


		pygame.display.flip()



	def draw_menu(self, menu_data):
		self.screen.fill((12,12,30))
		for i, s in enumerate(menu_data.get_selections()):
			if i == menu_data.pointer_i:
				self.draw_image((self.size[0]/2 - 70, 350+i*30), self.images["BLOCK_1"], (0, 0))
			t = self.font.render(s, 1, (255, 255, 255))
			self.screen.blit(t , (self.size[0]/2, 350+i*30))


	def load_graphics(self, file_list):
		for path in file_list:
			key = path.split("/")[-1]
			self.sheets[key] = pygame.image.load(path).convert()
			transColor = self.sheets[key].get_at((20,20))
			self.sheets[key].set_colorkey( transColor)

	def associate_animations(self, obj_list):
		for obj in obj_list:
			obj.animations = {}
			for animation_name in obj.animation_names:
				obj.animations[animation_name] = self.animations[animation_name].get_animation_tracker()


			


