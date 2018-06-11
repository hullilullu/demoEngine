import game_objects
from engine import tile
import random


class MenuData:
	def __init__(self, run_data):
		self.__run_data = run_data
		self.pointer_i = 0
		self.exit = False
		self.run_game = False
		self.current_menu = "MAIN"
		self.menus = {"MAIN": ["GO_PLAY_PLAY", "P_QUIT_QUIT"], "PLAY": ["P_RANDOMIZE_RANDOM STAGE", "GO_MAIN_BACK"]}
	def select(self):
		print (self.menus)
		print(self.current_menu)
		print(self.pointer_i)
		l = self.menus[self.current_menu][self.pointer_i]
		parsed = l.split("_")
		if parsed[0] == "GO":
			self.current_menu = parsed[1]
			print(self.current_menu)
			self.pointer_i = 0
		elif parsed[0] == "P":
			if parsed[1] == "QUIT":
				self.exit = True
			elif parsed[1] == "RANDOMIZE":
				self.run_game = True
				self.__run_data.randomize_level = True
	def increment(self):
		self.pointer_i =  ( self.pointer_i + 1 ) % len(self.menus[self.current_menu])
	def decrement(self):
		self.pointer_i =  ( self.pointer_i - 1 ) % len(self.menus[self.current_menu])
	def get_selections(self):
		l = []
		for s in self.menus[self.current_menu]:
			l.append(s.split("_")[-1])
		return l







class StageData:
	def __init__(self, stage_index):
		self.stage_index = stage_index
		self.game_objects = []
		self.tiles = []
		self.size = []
		self.music = None
	def randomize(self):
		self.music = "swinger.ogg"
		self.game_objects.append(game_objects.MainCh(100, 100))
		
		#self.game_objects.append(game_objects.PowerUp(1000, 100))

		#self.game_objects.append(game_objects.Trampoline(2000, 100))
		"""self.tiles.append(game_objects.GameObject(290, 164))
		self.tiles.append(game_objects.GameObject(150, 250))
		self.tiles.append(game_objects.GameObject(220, 250))
		self.tiles.append(game_objects.GameObject(290, 250))
		self.tiles.append(game_objects.GameObject(360, 250))
		self.tiles.append(game_objects.GameObject(430, 250))
		self.tiles.append(game_objects.GameObject(500, 250))
		self.tiles.append(game_objects.GameObject(640, 250))
		self.tiles.append(game_objects.GameObject(710, 250))
		self.tiles.append(game_objects.GameObject(0, 1000))
		self.tiles.append(game_objects.GameObject(-70, 1000))"""
		class Hole:
			def __init__(self, x, w, ticker):
				self.x = x
				self.w = w
				self.ticker = ticker

		for i in range(500):
			self.tiles.append(tile.Tile(i*50, 350, 50, 50, "standard", "BLOCK_1"))
			self.tiles.append(tile.Tile(0, 300 - i * 50, 50, 50, "standard", "BLOCK_1"))
		xCount = 0
		yCount = 0
		trampoline = 5
		holes = []
		for y in range(100):
			xCount = 0
			for h in holes:
				h.ticker -= 1
				if h.ticker < 1:
					holes.remove(h)
			for x in range(100):
				hole = False
				for h in holes:
					if x*50 > h.x and x*50 < h.x + h.w:
						hole = True
						print("HOLE", x*50, 250-y*50)
				if hole == False and (-50*y < -200 or 50*x > 300 ):
					seed = random.randint(0, 9)
					seed2 = random.randint(0, 20)
					if  (y%4 == 3 and seed + xCount > 8 ):
						self.tiles.append(tile.Tile(x*50, 250-y*50, 50, 50, "standard", "BLOCK_1"))
						xCount += 1
						if xCount > 7:
							xCount = 0
					elif seed2 == 5 or (xCount < 4 and xCount > 0 and seed2 > 10):
						self.tiles.append(tile.Tile(x*50, 250-y*50, 50, 50, "standard", "BLOCK_1"))
						xCount += 1
						if xCount > 7:
							xCount = 0
					elif xCount > 0:
						xCount = 0
					elif xCount == 0 and seed == 2 and seed2 == 2:
						if trampoline:
							trampoline -= 1
							self.game_objects.append(game_objects.Trampoline(x*50, 150-y*50))
							print("tramp", x, y)
						holes.append(Hole(x*50 - 300, 600, 10))



		"""
		self.tiles.append(tile.Tile(450, 300, 50, 50, "standard", "BLOCK_1"))
		self.tiles.append(tile.Tile(250, 100, 50, 50, "standard", "BLOCK_1"))
		self.tiles.append(tile.Tile(200, 100, 50, 50, "standard", "BLOCK_1"))
		self.tiles.append(tile.Tile(500, 250, 50, 50, "standard", "BLOCK_1"))
		"""

		


class RunData:
	def __init__(self, MAX_LEVEL):
		self.__current_level = 0
		self.MAX_LEVEL = MAX_LEVEL
		self.randomize_level = False
	def increment_level(self):
		self.__current_level = (self.__current_level + 1) % self.MAX_LEVEL
	def set_current_level(self, level):
		self.__current_level = level % self.MAX_LEVEL

