import pygame 
import time
import random
import math

#setup background
pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1200, 750
fps = 60

space = pygame.display.set_mode((WIDTH, HEIGHT))

#define properties of a star
class Star(object):
	"""docstring for star"""
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

	def draw(self, space):
		pygame.draw.circle(space, self.Color, (self.x, self.y), 7)
		pygame.display.update()

	def move(self):
		self.x += int(self.z)*self.quadrant
		self.y = int((self.dx)*self.m) + HEIGHT//2
		pygame.draw.line(space, self.Color, (self.px, self.py), (self.x, self.y), 3)
		pygame.display.update()
		self.dx = self.x - WIDTH//2
		self.dy = self.y - HEIGHT//2
		self.z = 0.02*math.sqrt( (self.dx)**2 + (self.dy)**2 )
		if self.line % 25 == 0:
			self.px = self.x
			self.py = self.y
		self.line += 1		
		

#run the warp drive!
# star = Star(340, 376)
stars = []
for i in range(1000):
	stars.append( Star(random.randint(10,1190), random.randint(10,740)) )
	#stars[i].draw(space)

driving = True
while driving:
	# clock.tick(fps)
	space.fill((0,0,0))

	for i in range(1000):
		if (stars[i].x < 0 or stars[i]. x > 1200):
			stars.pop(stars.index(stars[i]))
			stars.append( Star(random.randint(10,1200), random.randint(10,740)) )
		# stars[i].draw(space)
		stars[i].move()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			driving = False
			pygame.quit()
