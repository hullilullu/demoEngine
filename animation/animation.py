#import error_handling

class Rect:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h= h

class Image:
	def __init__(self, sheet, x, y, w, h, offset_x = 0, offset_y = 0):
		self.sheet = sheet
		self.sheet_x = x
		self.sheet_y = y
		self.sheet_w = w
		self.sheet_h = h
		self.offset_x = offset_x
		self.offset_y = offset_y

class Frame:
	def __init__(self, sheet, x, y, w, h, t = 12, offset_x = 0, offset_y = 0):
		self.sheet = sheet
		self.sheet_x = x
		self.sheet_y = y
		self.sheet_w = w
		self.sheet_h = h
		self.t = t
		self.offset_x = offset_x
		self.offset_y = offset_y
	def get_rect(self):
		return Rect(self.sheet_x, self.sheet_y, self.sheet_w, self.sheet_h)

class AnimationTracker:
	def __init__(self, animation):
		self.animation = animation
		self.right = False
		self.current_index = 0
		self.ticker = animation.get_frame(0).t
		self.speed = animation.speed
	def iterate(self):
		if self.ticker <= 0:
			self.current_index = (self.current_index + 1) % self.animation.len
			self.ticker = self.animation.get_frame(self.current_index).t / self.speed
		else:
			self.ticker -= 1


class Animation:
	def __init__(self, frames = [], speed = 1):
		#self.name = name
		self.__frames = frames
		self.len = len(self.__frames)
		self.current_index = 0
		self.speed = speed
		if self.__frames != []:
			self.ticker = self.__frames[self.current_index].t

	def add_frame(self, frame, index = -1):
		if index == -1:
			index = self.len
		self.__frames.insert(index, frame)
		self.len += 1
	def get_frame(self, index):
		return self.__frames[index]
	def get_animation_tracker(self):
		return AnimationTracker(self)




