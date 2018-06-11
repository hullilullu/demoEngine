import pygame

def rectCollobt(r1, r2):
	pr1 = pygame.Rect(r1.pos[0]+r1.velocity[0], r1.pos[1]+r1.velocity[1], r1.wh[0], r1.wh[1])
	pr2 = pygame.Rect(r2.pos[0], r2.pos[1], r2.wh[0], r2.wh[1])
	if pr1.colliderect(pr2):
		offset = 0.1

		side = None

		x1 = r1.pos[0]
		y1 = r1.pos[1]
		w1 = r1.wh[0]
		h1 = r1.wh[1]
		x2 = r2.pos[0]
		y2 = r2.pos[1]
		w2 = r2.wh[0]
		h2 = r2.wh[1]
		vx = r1.velocity[0]
		vy = r1.velocity[1]

		#left side
		if x1 + w1 <= x2:
			if y1 + h1 >= y2 and y1 <= y2 + h2:
				#left
				x1 = x2 - w1 - offset
				vx = 0
				side = "l"
			elif vx == 0 or x2 - x1 - w1 == 0:
				y1 = y2 - h1 -offset
				vy = 0
				side = "t"
			elif vx == vy:
				y1 = y2 - h1 -offset
				vy = 0
				x1 = x2 - w1 - offset
				vx = 0
				side = "tl"
			elif vx == -vy:
				x1 = x2 - w1 - offset
				vx = 0
				y1 = y2 + h2 +offset
				vy = 0
				side = "bl"
			elif y1 + h1 < y2 + 1:
				if abs(vy/vx) > ( y2 - y1 - h1 ) / (x2 - x1 - w1):
					#left
					x1 = x2 - w1 -offset
					vx = 0
					side = "l"
				else:
					#top
					y1 = y2 - h1 -offset
					vy = 0
					side = "t"
			elif y1 + h1 < y2:
				if abs(vy/vx) > ( y1 - y2 - h2 ) / (x2 - x1 - w1):
					#left
					x1 = x2 - w1 -offset
					vx = 0
					side = "l"
				else:
					#bottom
					y1 = y2 + h2 +offset
					vy = 0
					side = "b"
		#right side
		elif x1 >= x2 + w2:
			if y1 + h1 >= y2 and y1 <= y2 + h2:
				x1 = x2 + w2 + offset
				vx = 0
				side = "r"
			elif vx == 0 or x1 - x2 - w2 == 0:
				y1 = y2 - h1 -offset
				vy = 0
				side = "t"
			elif vx == vy:
				y1 = y2 - h1 -offset
				vy = 0
				x1 = x2 + w2 + offset
				vx = 0
				side = "tl"
			elif vx == -vy:
				x1 = x2 + w2 + offset
				vx = 0
				y1 = y2 + h2 +offset
				vy = 0
				side = "bl"
			elif y1 + h1 < y2:
				if abs(vy/vx) > ( y2 + h2 - y1) / (x1- x2 - w2):
					#right
					x1 = x2 + w2 + offset
					vx = 0
					side = "r"
				else:
					#bottom
					y1 = y2 + h2 + offset
					vy = 0
					side = "b"
			elif y1 + h1 < y2:
				if abs(vy/vx) > ( y2 - y1 - h1) / (x1- x2 - w2):
					#right
					x1 = x2 + w2 + offset
					vx = 0
					side = "r"
				else:
					#top
					y1 = y2 - h1 -offset
					vy = 0
					side = "t"
		#middle
		elif y1 + h1 <= y2 + 1:
			#top
			y1 = y2 - h1 -offset
			vy = 0
			side = "t"
		elif y1 >= y2 + h2 - 1:
			#bottom
			y1 = y2 + h2 + offset
			vy = 0
			side = "b"
		else:
			#top
			
			"""
			y1 = y2 - h1 -offset
			vy = 0
			side = "top"
			"""

		#print (x1, y1, "h1 = ",y2 - h1 -offset, vx, vy, x2, y2, side)
		return (x1, y1, vx, vy, side)

	else: 
		return None


def handle_collisions(game_objects, tiles):
	for go in game_objects:
		cl = [1]
		n = 0
		while n < 10:
			cl = []
			for t in tiles:
				c = rectCollobt(go, t)
				if c: 
					cl.append(c)

			if cl != []:
				n += 1
				d2 = 9999
				indeces = []
				for i, c in enumerate(cl):
					d = (go.pos[0]-c[0])**2 + (go.pos[1]-c[1])**2
					if d < d2:
						indeces = [i]
						d2 = d
					elif d == d2:
						indeces.append(i)
				for index in indeces:
					go.pos = [cl[index][0], cl[index][1]]
					if cl[index][4] == "t":
						go.velocity = [go.velocity[0], cl[index][3]]
						go.grounded = True
					elif cl[index][4] == "b":
						go.velocity = [go.velocity[0], cl[index][3]]
					elif cl[index][4] == "l" or cl[index][4] == "r":
						go.velocity = [cl[index][2], go.velocity[1]]


			else: break

def handle_damage(game_objects):
	mainCh = game_objects[0]
	m_rect = pygame.Rect(mainCh.pos, mainCh.wh)
	for o in game_objects:
		if o.destroy:
			game_objects.remove(o)
	for i in range(len(game_objects) - 1):
		if m_rect.colliderect(pygame.Rect(game_objects[i+1].pos, game_objects[i+1].wh)):
			game_objects[i+1].on_collision(mainCh)