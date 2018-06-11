import animation

class GameObject:
	def __init__(self, x, y, mass = 1):
		self.pos = [x, y]
		self.wh = [70, 85]
		self.velocity = [0, 0]
		self.acc = [0, 0]
		self.walk_speed = 1
		self.jump_power = 10
		self.mass = mass
		self.right = False
		self._type = "GENERAL"
		self.animation_names = ["GO_TEST", "IDLE_TEST"]
		self.animation_dict = {"WALK": "GO_TEST", "IDLE": "IDLE_TEST"}
		self.current_animation = "IDLE_TEST"
		self.states = ["WALK", "IDLE"]
		self.current_state = "IDLE"
		self.grounded = False
		self.destroy = False
	def add_force(self, force):
		self.acc = [self.acc[0] + force[0]/self.mass, self.acc[1] + force[1]/self.mass]
	def update_pos(self):
		self.velocity = [self.velocity[0] + self.acc[0], self.velocity[1] + self.acc[1]]
		self.pos = [self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1]]
		self.acc = [0, 0]
	def set_state(self, s):
		if s in self.states:
			self.current_state = s
			self.current_animation = self.animation_dict.get(s)