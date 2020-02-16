import pygame 
import time
import random
import math

#setup background
pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 900, 550
fps = 30

space = pygame.display.set_mode((WIDTH, HEIGHT))

#define properties of a star
class Star(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.px = self.x
		self.py = self.y
		self.dx = self.x - WIDTH//2 + 0.0001
		self.dy = self.y - HEIGHT//2 
		self.m = self.dy/self.dx
		self.z = 0.02*math.sqrt( (self.dx)**2 + (self.dy)**2 )
		self.quadrant = 1
		if self.dx < 0:
			self.quadrant = -1
		self.Color = (255 - 3*self.z, 255 - 3*self.z, 255 - 3*self.z)
		self.line = 0

	def move(self):
		self.x += int(self.z)*self.quadrant
		self.y = int((self.dx)*self.m) + HEIGHT//2
		pygame.draw.line(space, self.Color, (self.px, self.py), (self.x, self.y), 1)
		pygame.display.update()
		self.dx = self.x - WIDTH//2
		self.dy = self.y - HEIGHT//2
		self.z = 0.02*math.sqrt( (self.dx)**2 + (self.dy)**2 )
		if self.line % 60 == 0:
			self.px = self.x
			self.py = self.y
		self.line += 1		
		

#run the warp drive!
# star = Star(340, 376)
stars = []
starCount = 100
for i in range(starCount):
	stars.append( Star(random.randint(10,WIDTH), random.randint(10,HEIGHT)) )

driving = True
while driving:
	clock.tick(fps)
	space.fill((0,0,0))

	for i in range(starCount):
		if (stars[i].x < 0 or stars[i]. x > WIDTH):
			stars.pop(stars.index(stars[i]))
			stars.append( Star(random.randint(10,WIDTH), random.randint(10,HEIGHT)) )
		stars[i].move()
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			driving = False
			pygame.quit()
