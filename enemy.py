from hero import Hero
import random
class Enemy(Hero):
	"""docstring for Enemy"""
	def __init__(self, height, width, pos):
		super(Enemy,self).__init__(height,width,pos)
	def getCurrentPosition(self):
		return self.pos
	def setPosition(self,x):
		self.pos=x

