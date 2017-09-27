import random
from termcolor import *
class Board(object):
	"""docstring for Board"""
	
	def __init__(self, x):
		self.columns = x
		self.rows = x
	def getrows(self):
		return self.rows
	def getcolumns(self):
		return self.columns
	def initialprint(self,pos,playArea,rows,columns):
		
		
		rows=54
		columns=54
		
		for i in range(rows):
			for j in range(columns):
				if ((i == 0 and j == 0)):
					playArea[i * columns + j] = 4
				elif i%4==0 or i%4==1:
					playArea[i * columns + j] = 0
				elif ((j%8==4 or j%8==5 or j%8==6 or j%8==7) and j!=52 and j!=53 and j!=54):
					playArea[i * columns + j] = 1
		playArea[1]=35
		playArea[2]=36
		playArea[3]=37
		playArea[54]=38
		playArea[55]=39
		playArea[56]=40
		playArea[57]=41
		for i in range(15):
			x=random.randint(10,40)
			print x
			x=x+4-x%4
			print x
			y=random.randint(10,40)
			y=y+8-y%8-4
			playArea[x*54+y]=2
			playArea[x*54+y+1]=2
			playArea[x*54+y+2]=2
			playArea[x*54+y+3]=2
			playArea[x*54+y+54]=2
			playArea[x*54+y+55]=2
			playArea[x*54+y+56]=2
			playArea[x*54+y+57]=2
		playArea[0]=4			
		playArea[pos[0]]=8
		playArea[pos[0]+1]=8
		playArea[pos[0]+columns]=8
		playArea[pos[0]+columns+1]=8
		playArea[pos[1]]=8
		playArea[pos[1]+1]=8
		playArea[pos[1]+columns]=8
		playArea[pos[1]+columns+1]=8
		playArea[pos[2]]=8
		playArea[pos[2]+1]=8
		playArea[pos[2]+1+columns]=8
		playArea[pos[2]+columns]=8
	def render(self, playArea,lives,score):
		rows=54
		columns=54
		print(colored('X','red')),
		for column in range(columns):
			print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red'))
		print(colored('X','red')),
		for column in range(columns):
			print(colored('X','red')),
		
		print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red'))
		
		for line in range(rows):
		
			print(colored("XXXX",'red')),
			
			for column in range(columns):
			

				if playArea[(line * columns) + column] == 0: 			# AIR
					print(" "),
				elif playArea[(line * columns) + column] == 1: 		# BLOCK
					print(colored('X','red')),
				elif playArea[(line * columns) + column] == 2:			# DESTRUCTIBLE_BLOCK
					print(colored("%","white")),
				elif playArea[(line * columns) + column] == 3:			# PLAYER_BOMB
					print("p"),
				elif playArea[(line * columns) + column] == 4:			# PLAYER
					print(colored("[","green")),
				elif playArea[(line * columns) + column] == 35:			# PLAYER
					print(colored("^","green")),
				elif playArea[(line * columns) + column] == 36:			# PLAYER
					print(colored("^","green")),
				elif playArea[(line * columns) + column] == 37:			# PLAYER
					print(colored("]","green")),
				elif playArea[(line * columns) + column] == 38:			# PLAYER
					print(colored(" ","green")),
				elif playArea[(line * columns) + column] == 39:			# PLAYER
					print(colored("[","green")),
				elif playArea[(line * columns) + column] == 40:			# PLAYER
					print(colored("]","green")),
				elif playArea[(line * columns) + column] == 41:			# PLAYER
					print(colored(" ","green")),
				elif playArea[(line * columns) + column] == 5:			# POWERUP_BOMB_POWER
					print("S"),
				elif playArea[(line * columns) + column] == 6:			# POWERUP_BOMB_AMOUNT
					print("0"),
				elif playArea[(line * columns) + column] == 10:		# EXPLOSION
					print("0"),
				elif playArea[(line * columns) + column] == 11:		# EXPLOSION
					print("0"),
				elif playArea[(line * columns) + column] == 12:		# EXPLOSION
					print("0"),
				elif playArea[(line * columns) + column] == 13:		# EXPLOSION
					print("0"),
				elif playArea[(line * columns) + column] == 14:		# EXPLOSION
					print("0"),
				elif playArea[(line * columns) + column] == 15:		# EXPLOSION
					print("0"),
				elif playArea[(line * columns) + column] == 20:			# BOMB
					print("2"),
				elif playArea[(line * columns) + column] == 21:			# BOMB
					print("2"),
				elif playArea[(line * columns) + column] == 22:			# BOMB
					print("2"),
				elif playArea[(line * columns) + column] == 23:			# BOMB
					print("2"),
				elif playArea[(line * columns) + column] == 24:			# BOMB
					print("1"),
				elif playArea[(line * columns) + column] == 25:			# BOMB
					print("1"),
				elif playArea[(line * columns) + column] == 26:			# BOMB
					print("1"),
				elif playArea[(line * columns) + column] == 27:			# BOMB
					print("1"),
				elif playArea[(line * columns) + column] == 28:			# BOMB
					print("1"),
				elif playArea[(line * columns) + column] == 29:			# BOMB
					print("1"),
				elif playArea[(line * columns) + column] == 30:			# BOMB
					print("1"),
				elif playArea[(line * columns) + column] == 31:			# BOMB
					print("1"),
				elif playArea[(line * columns) + column] == 32:			# BOMB
					print("1"),
				elif playArea[(line*columns)+column] == 8:
					print("E"),
				else:
					print(" "),
					
			print(colored('XXXX',"red"))
			
		print(colored('X','red')),
		for column in range(columns):
			print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red'))
		print(colored('X','red')),
		for column in range(columns):
			print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red')),
		print(colored('X','red'))
		print("Lives Remaining:", lives[0])
		print("Current score:",score[0])
		

			