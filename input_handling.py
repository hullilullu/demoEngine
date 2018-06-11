import pygame

class Input_Data:
	def __init__(self):
		self.quit = False
		self.up = False
		self.down = False
		self.right = False
		self.left = False
		self.command = False
		self.enter = False
		self.mouse_pos = (0,0)
		self.mouse_down = False
		self.mouse_click = False
	def get_input(self):
		self.mouse_pos = pygame.mouse.get_pos()
		self.mouse_click = False
		self.enter = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit = True
				break
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.mouse_down = True
			elif event.type == pygame.MOUSEBUTTONUP:
				self.mouse_down = False
				self.mouse_click = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.up = True
				if event.key == pygame.K_DOWN:
					self.down = True
				if event.key == pygame.K_RIGHT:
					self.right = True
				if event.key == pygame.K_LEFT:
					self.left = True
				if event.key == 310:  #cmd
					self.command = True
				if event.key == 113 and self.command:  #113 == Q
					self.quit = True
				if event.key == 13:  #ENTER
					self.enter = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.up = False
				if event.key == pygame.K_DOWN:
					self.down = False
				if event.key == pygame.K_RIGHT:
					self.right = False
				if event.key == pygame.K_LEFT:
					self.left = False
				if event.key == 310:
					self.command = False