import pygame

class SoundHandler:
	def __init__(self, sounds, music):
		self.music = False
		self.sounds = {}
		self.default_sound = None
		try:
			self.default_sound = pygame.mixer.Sound("audio/effects/default.ogg")
			self.music = True
		except:
			pass
		try:
		    pygame.mixer.music.load("audio/" + music)
		except:
			print("music not loaded" + music)
		for s in sounds:
			try:
				s_nopath = s.split("/")[-1]
				key = s_nopath.split(".")[0]
				self.sounds[key] = pygame.mixer.Sound(s)
				print("key = %s" , key)
			except:
				pass

	def play_music(self):
		if self.music:
			pygame.mixer.music.play(loops = -1)
	def play_sound(self, s):
		self.sounds[s].play(loops = 0) #get(s, default = self.default_sound)
	def exit(self):
		pygame.mixer.music.stop()