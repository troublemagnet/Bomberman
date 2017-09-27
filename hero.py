class Hero(object):
	"""docstring for Hero"""
	def __init__(self, height , width, pos):
		self.height = height
		self.width = width
		self.pos = pos
	def getCurrentPosition(self):
		return self.pos
	def getHeight(self):
		return self.height
	def getWidth(self):
		return self.width
	def setPosition(self,x):
		self.pos=x
