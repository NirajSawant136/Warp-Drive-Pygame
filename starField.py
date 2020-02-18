import pygame 
import time
import random
import math

#setup background
pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1200, 750
fps = 30

space = pygame.display.set_mode((WIDTH, HEIGHT))

#define properties of a star
class Star(object):
	"""docstring for star"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dx = self.x - WIDTH//2 + 0.0001
		self.dy = self.y - HEIGHT//2 
		self.m = self.dy/self.dx
		self.z = 0.02*math.sqrt( (self.dx)**2 + (self.dy)**2 )
		self.quadrant = 1
		if self.dx < 0:
			self.quadrant = -1
		self.Color = (150, 150, 150)
		self.r = 0

	def draw(self, space):
		pygame.draw.circle(space, self.Color, (self.x, self.y), int(self.r))

	def move(self):
		self.x += int(self.z)*self.quadrant
		self.y = int((self.dx)*self.m) + HEIGHT//2
		self.dx = self.x - WIDTH//2
		self.dy = self.y - HEIGHT//2
		self.z = 0.02*math.sqrt( (self.dx)**2 + (self.dy)**2 )
		if not(500 < self.x < 700 and 200 < self.y < 500):
			self.r += 0.1
			
		

#run the warp drive!
# star = Star(340, 376)
stars = []
starCount = 500

for i in range(starCount):
	stars.append( Star(random.randint(10,1100), random.randint(10,750)) )
	stars[i].draw(space)

driving = True
while driving:
	clock.tick(fps)
	space.fill((0,0,0))

	for i in range(starCount):
		if (stars[i].x < 0 or stars[i]. x > WIDTH):
			stars.pop(stars.index(stars[i]))
			stars.append( Star(random.randint(10,1100), random.randint(10,750)) )
		stars[i].draw(space)
		stars[i].move()

	pygame.draw.circle(space, (0,0,0),(WIDTH//2, HEIGHT//2),70)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			driving = False
			pygame.quit()
