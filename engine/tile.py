

class Tile:
	def __init__(self, x, y, w, h, _type, image_name):
		self.pos = [x, y]
		self.wh = [w, h]
		self.type = _type
		self.image_name = image_name


