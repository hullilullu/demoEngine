from engine.game_object_prefab import GameObject





class MainCh(GameObject):
	def __init__(self, x, y):
		GameObject.__init__(self, x, y)
		self._type = "MAIN"
		self.walk_speed = 7
		self.jump_power = 12
		self.wh = [65, 110]
		self.gravity = True
		self.animation_names = ["WALK_MAIN", "IDLE_MAIN", "JUMP_MAIN"]
		self.animation_dict = {"WALK": "WALK_MAIN", "IDLE": "IDLE_MAIN", "JUMP": "JUMP_MAIN"}
		self.current_animation = "IDLE_MAIN"
		self.states = ["WALK", "IDLE", "JUMP"]


class PowerUp(GameObject):
	def __init__(self, x, y):
		GameObject.__init__(self, x, y)
		self.gravity = False
	def on_collision(self, go):
		if go._type == "MAIN":
			go.jump_power += 13
			self.destroy = True

class Trampoline(GameObject):
	def __init__(self, x, y):
		GameObject.__init__(self, x, y)
		self.gravity = False
		self.w = 40
		self.h = 40
	def on_collision(self, go):
		if go._type == "MAIN":
			go.velocity[1] -= 5








