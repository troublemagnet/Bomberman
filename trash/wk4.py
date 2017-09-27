#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import msvcrt
import os, time, sys, random, math
from termcolor import *
import kbhit
random.seed()

columns = 54		#\
									# adjustable, odd numbers only
lines = 54			#/  


pPos = 0				#top left corner starting position

explosions = range(10,16)
bombs = range(20,33)

spf = 0.1			#seconds per frame
bombPower = 2
maxBombs = 3
activeBombs = []
activeExplosions = []
brokenBoxes = [] 
activeBombCount = 0
percentBoxes = 0.1			# percent of screen filled with destructible boxes
atime = time.time()
lives = [0]*2
score = [0]*2
# 0 = AIR, 1 = BLOCK, 2 = DESTRUCTIBLE_BLOCK, 3 = PLAYER_BOMB, 4 = PLAYER,
# 5 = POWERUP_BOMB_STRENGTH, 6 = POWERUP_BOMB_AMOUNT, 10-15 = EXPLOSION, 20-32 = BOMB
# 8 = ENEMY
class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch



getch = _Getch()

def InitArray():
	global gameArray, pos
	
	
	pos = [0]*4
	pos[1]=35*54+56
	pos[2]=40*54+51	
	pos[0]=4*54
	
	gameArray = [0] * (lines*columns)
	
	for i in range(lines):
		for j in range(columns):
			if ((i == 0 and j == 0)):
				gameArray[i * columns + j] = 4
			elif i%4==0 or i%4==1:
				gameArray[i * columns + j] = 0
			elif ((j%8==4 or j%8==5 or j%8==6 or j%8==7) and j!=52 and j!=53 and j!=54):
				gameArray[i * columns + j] = 1
	gameArray[1]=35
	gameArray[2]=36
	gameArray[3]=37
	gameArray[54]=38
	gameArray[55]=39
	gameArray[56]=40
	gameArray[57]=41
	for i in range(15):
		x=random.randint(10,40)
		print x
		x=x+4-x%4
		print x
		y=random.randint(10,40)
		y=y+8-y%8-4
		gameArray[x*54+y]=2
		gameArray[x*54+y+1]=2
		gameArray[x*54+y+2]=2
		gameArray[x*54+y+3]=2
		gameArray[x*54+y+54]=2
		gameArray[x*54+y+55]=2
		gameArray[x*54+y+56]=2
		gameArray[x*54+y+57]=2
	gameArray[0]=4			
	gameArray[pos[0]]=8
	gameArray[pos[0]+1]=8
	gameArray[pos[0]+columns]=8
	gameArray[pos[0]+columns+1]=8
	gameArray[pos[1]]=8
	gameArray[pos[1]+1]=8
	gameArray[pos[1]+columns]=8
	gameArray[pos[1]+columns+1]=8
	gameArray[pos[2]]=8
	gameArray[pos[2]+1]=8
	gameArray[pos[2]+1+columns]=8
	gameArray[pos[2]+columns]=8
	
	

def EnemyMovement():
		
		x = random.randint(3,4)
		y = random.randint(1,2)
		z = random.randint(1,2)
		#print x
		if x==1:
			if(pos[0]!=-1 and pos[0]-54>=0 and gameArray[(pos[0]-54)]!=1 and gameArray[pos[0]-54]!=4 and gameArray[pos[0]-54]!=2 and gameArray[pos[0]+1-54]!=1 and gameArray[pos[0]+1-54]!=2 and gameArray[pos[0]+1-54]!=4):
				gameArray[pos[0]-54]=8
				gameArray[pos[0]-54+1]=8
				gameArray[pos[0]+54]=0
				gameArray[pos[0]+54+1]=0
				pos[0]-=54

		elif x==2:
			if(pos[0]!=-1 and pos[0]<(53*54) and gameArray[pos[0]+54]!=1 and gameArray[pos[0]+54]!=4 and gameArray[pos[0]+54]!=2 and gameArray[pos[0]+54+1]!=1 and gameArray[pos[0]+54+1]!=4 and gameArray[pos[0]+54+1]!=2):
				gameArray[pos[0]+54]=8
				gameArray[pos[0]+54+1]=8
				gameArray[pos[0]-54]=0
				gameArray[pos[0]+1-54]=0
				pos[0]+=54
		elif x==3:
			if(pos[0]!=-1 and pos[0]%54<52 and gameArray[pos[0]+2]!=1 and gameArray[pos[0]+2]!=4 and gameArray[pos[0]+2]!=2 and gameArray[pos[0]+columns+2]!=1 and gameArray[pos[0]+columns+2]!=4 and gameArray[pos[0]+columns+2]!=2):
				gameArray[pos[0]+1]=8
				gameArray[pos[0]+1+columns]=8
				gameArray[pos[0]-1+columns]=0
				gameArray[pos[0]-1]=0
				pos[0]+=1
		elif x==4:
			if(pos[0]!=-1 and pos[0]%54>1 and gameArray[pos[0]-1]!=1 and gameArray[pos[0]-1]!=4 and gameArray[pos[0]-1]!=2 and gameArray[pos[0]+columns-1]!=1 and gameArray[pos[0]+columns-1]!=4 and gameArray[pos[0]+columns-1]!=2):
				gameArray[pos[0]-1]=8
				gameArray[pos[0]+columns-1]=8
				gameArray[pos[0]+1]=0
				gameArray[pos[0]+columns+1]=0
				pos[0]-=1
		
		if y==1:
			if(pos[1]!=-1 and pos[1]-54>=0 and gameArray[(pos[1]-54)]!=1 and gameArray[pos[1]-54]!=4 and gameArray[pos[1]-54]!=2 and gameArray[pos[1]+1-54]!=1 and gameArray[pos[1]+1-54]!=2 and gameArray[pos[1]+1-54]!=4):
				gameArray[pos[1]-54]=8
				gameArray[pos[1]-54+1]=8
				gameArray[pos[1]+54]=0
				gameArray[pos[1]+54+1]=0
				pos[1]-=54
		elif y==2:
			if(pos[1]!=-1 and pos[1]<(53*54) and gameArray[pos[1]+54]!=1 and gameArray[pos[1]+54]!=4 and gameArray[pos[1]+54]!=2 and gameArray[pos[1]+54+1]!=1 and gameArray[pos[1]+54+1]!=4 and gameArray[pos[1]+54+1]!=2):
				gameArray[pos[1]+54]=8
				gameArray[pos[1]+54+1]=8
				gameArray[pos[1]-54]=0
				gameArray[pos[1]+1-54]=0
				pos[1]+=54
		elif y==3:
			if(pos[1]!=-1 and pos[1]%54<52 and gameArray[pos[1]+2]!=1 and gameArray[pos[1]+2]!=4 and gameArray[pos[1]+2]!=2 and gameArray[pos[1]+columns+2]!=1 and gameArray[pos[1]+columns+2]!=4 and gameArray[pos[1]+columns+2]!=2):
				gameArray[pos[1]+1]=8
				gameArray[pos[1]+1+columns]=8
				gameArray[pos[1]-1+columns]=0
				gameArray[pos[1]-1]=0
				pos[1]+=1
		elif y==4:
			if(pos[1]!=-1 and pos[1]%54>1 and gameArray[pos[1]-1]!=1 and gameArray[pos[1]-1]!=4 and gameArray[pos[1]-1]!=2 and gameArray[pos[1]+columns-1]!=1 and gameArray[pos[1]+columns-1]!=4 and gameArray[pos[1]+columns-1]!=2):
				gameArray[pos[1]-1]=8
				gameArray[pos[1]+columns-1]=8
				gameArray[pos[1]+1]=0
				gameArray[pos[1]+columns+1]=0
				pos[1]-=1
		if z==1:
			if(pos[2]!=-1 and pos[2]-54>=0 and gameArray[(pos[2]-54)]!=1 and gameArray[pos[2]-54]!=4 and gameArray[pos[2]-54]!=2 and gameArray[pos[2]+1-54]!=1 and gameArray[pos[2]+1-54]!=2 and gameArray[pos[2]+1-54]!=4):
				gameArray[pos[2]-54]=8
				gameArray[pos[2]-54+1]=8
				gameArray[pos[2]+54]=0
				gameArray[pos[2]+54+1]=0
				pos[2]-=54
		elif z==2:
			if(pos[2]!=-1 and pos[2]<(52*54) and gameArray[pos[2]+54]!=1 and gameArray[pos[2]+54]!=4 and gameArray[pos[2]+54]!=2 and gameArray[pos[2]+54+1]!=1 and gameArray[pos[2]+54+1]!=4 and gameArray[pos[2]+54+1]!=2):
				gameArray[pos[2]+54]=8
				gameArray[pos[2]+54+1]=8
				gameArray[pos[2]-54]=0
				gameArray[pos[2]+1-54]=0
				pos[2]+=54
		elif z==3:
			if(pos[2]!=-1 and pos[2]%54<52 and gameArray[pos[2]+2]!=1 and gameArray[pos[2]+2]!=4 and gameArray[pos[2]+2]!=2 and gameArray[pos[2]+columns+2]!=1 and gameArray[pos[2]+columns+2]!=4 and gameArray[pos[2]+columns+2]!=2):
				gameArray[pos[2]+1]=8
				gameArray[pos[2]+1+columns]=8
				gameArray[pos[2]-1+columns]=0
				gameArray[pos[2]-1]=0
				pos[2]+=1
		elif z==4:
			if(pos[2]!=-1 and pos[1]%54>1 and gameArray[pos[2]-1]!=1 and gameArray[pos[2]-1]!=4 and gameArray[pos[2]-1]!=2 and gameArray[pos[2]+columns-1]!=1 and gameArray[pos[2]+columns-1]!=4 and gameArray[pos[2]+columns-1]!=2):
				gameArray[pos[2]-1]=8
				gameArray[pos[2]+columns-1]=8
				gameArray[pos[2]+1]=0
				gameArray[pos[2]+columns+1]=0
				pos[2]-=1
		if((gameArray[pos[0]]==4 or gameArray[pos[0]] in [35,41]) or (gameArray[pos[1]]==4 or gameArray[pos[1]] in [35,41]) or (gameArray[pos[2]]==4 or gameArray[pos[2]] in [35,41])):
			lives[0]-=1
			if(lives[0]==0):
				GameOver()
		if((gameArray[pos[0]]>=10 and gameArray[pos[0]]<=15) or (gameArray[pos[0]+1]>=10 and gameArray[pos[0]+1]<=15) or (gameArray[pos[0]+columns]>=10 and gameArray[pos[0]+columns]<=15) or (gameArray[pos[0]+columns+1]>=10 and gameArray[pos[0]+columns+1]<=15)):
					
					score+=100
					pos[0]=-1
		if((gameArray[pos[1]]>=10 and gameArray[pos[1]]<=15) or (gameArray[pos[1]+1]>=10 and gameArray[pos[1]+1]<=15) or (gameArray[pos[1]+columns]>=10 and gameArray[pos[1]+columns]<=15) or (gameArray[pos[1]+columns+1]>=10 and gameArray[pos[1]+columns+1]<=15)):
					
					score+=100
					pos[1]=-1
		if((gameArray[pos[2]]>=10 and gameArray[pos[2]]<=15) or (gameArray[pos[2]+1]>=10 and gameArray[pos[2]+1]<=15) or (gameArray[pos[2]+columns]>=10 and gameArray[pos[2]+columns]<=15) or (gameArray[pos[2]+columns+1]>=10 and gameArray[pos[2]+columns+1]<=15)):
					
					score+=100
					pos[2]=-1
def Render():
	os.system('clear')
	
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
	
	for line in range(lines):
	
		print(colored("XXXX",'red')),
		
		for column in range(columns):
		

			if gameArray[(line * columns) + column] == 0: 			# AIR
				print(" "),
			elif gameArray[(line * columns) + column] == 1: 		# BLOCK
				print(colored('X','red')),
			elif gameArray[(line * columns) + column] == 2:			# DESTRUCTIBLE_BLOCK
				print(colored("%","white")),
			elif gameArray[(line * columns) + column] == 3:			# PLAYER_BOMB
				print("p"),
			elif gameArray[(line * columns) + column] == 4:			# PLAYER
				print(colored("[","green")),
			elif gameArray[(line * columns) + column] == 35:			# PLAYER
				print(colored("^","green")),
			elif gameArray[(line * columns) + column] == 36:			# PLAYER
				print(colored("^","green")),
			elif gameArray[(line * columns) + column] == 37:			# PLAYER
				print(colored("]","green")),
			elif gameArray[(line * columns) + column] == 38:			# PLAYER
				print(colored(" ","green")),
			elif gameArray[(line * columns) + column] == 39:			# PLAYER
				print(colored("[","green")),
			elif gameArray[(line * columns) + column] == 40:			# PLAYER
				print(colored("]","green")),
			elif gameArray[(line * columns) + column] == 41:			# PLAYER
				print(colored(" ","green")),
			elif gameArray[(line * columns) + column] == 5:			# POWERUP_BOMB_POWER
				print("S"),
			elif gameArray[(line * columns) + column] == 6:			# POWERUP_BOMB_AMOUNT
				print("0"),
			elif gameArray[(line * columns) + column] == 10:		# EXPLOSION
				print("0"),
			elif gameArray[(line * columns) + column] == 11:		# EXPLOSION
				print("0"),
			elif gameArray[(line * columns) + column] == 12:		# EXPLOSION
				print("0"),
			elif gameArray[(line * columns) + column] == 13:		# EXPLOSION
				print("0"),
			elif gameArray[(line * columns) + column] == 14:		# EXPLOSION
				print("0"),
			elif gameArray[(line * columns) + column] == 15:		# EXPLOSION
				print("0"),
			elif gameArray[(line * columns) + column] == 20:			# BOMB
				print("2"),
			elif gameArray[(line * columns) + column] == 21:			# BOMB
				print("2"),
			elif gameArray[(line * columns) + column] == 22:			# BOMB
				print("2"),
			elif gameArray[(line * columns) + column] == 23:			# BOMB
				print("2"),
			elif gameArray[(line * columns) + column] == 24:			# BOMB
				print("1"),
			elif gameArray[(line * columns) + column] == 25:			# BOMB
				print("1"),
			elif gameArray[(line * columns) + column] == 26:			# BOMB
				print("1"),
			elif gameArray[(line * columns) + column] == 27:			# BOMB
				print("1"),
			elif gameArray[(line * columns) + column] == 28:			# BOMB
				print("1"),
			elif gameArray[(line * columns) + column] == 29:			# BOMB
				print("1"),
			elif gameArray[(line * columns) + column] == 30:			# BOMB
				print("1"),
			elif gameArray[(line * columns) + column] == 31:			# BOMB
				print("1"),
			elif gameArray[(line * columns) + column] == 32:			# BOMB
				print("1"),
			elif gameArray[(line*columns)+column] == 8:
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
	#print( "Bomb power:", bombPower)
	#print( time.time() - atime)

def GameOver():
	time.sleep(0.3)
	
	for i in range(3):
		os.system('clear')
		time.sleep(0.1)
		Render()
		time.sleep(0.1)
		
	time.sleep(0.3)

	Render()
	
	print ("Oops, you died. Your final score is:", score[0])
	time.sleep(3)
	exit()
	
def Explode(x):
	global activeBombCount
	activeBombs.remove(x)
	activeBombCount -= 1
	gameArray[x] = 10
	activeExplosions.append(x)
	
	i = 1 # UP
	while i <= bombPower and (x - i * columns) >= 0 and gameArray[x - i * columns] != 1:
		if gameArray[x - i * columns] in bombs:
			Explode(x - i * columns)
		else:
			breakBox = gameArray[x - i * columns] == 2
			gameArray[x - i * columns] = 10
			if (x - i * columns) not in activeExplosions:
				activeExplosions.append(x - i * columns)
			if breakBox:
				brokenBoxes.append(x - i * columns)
				break
		i += 1
		
	i = 1 # RIGHT
	while i <= bombPower and (x + i) % columns != 0 and gameArray[x + i] != 1:
		if gameArray[x + i] in bombs:
			Explode(x + i)
		else:
			breakBox = gameArray[x + i] == 2
			gameArray[x + i] = 10
			if (x + i) not in activeExplosions:
				activeExplosions.append(x + i)
			if breakBox:
				brokenBoxes.append(x + i)
				break
		i += 1
		
	i = 1 # DOWN
	while i <= bombPower and (x + i * columns) <= (lines * columns - 1) and gameArray[x + i * columns] != 1:
		if gameArray[x + i * columns] in bombs:
			Explode(x + i * columns)
		else:
			breakBox = gameArray[x + i * columns] == 2
			gameArray[x + i * columns] = 10
			if (x + i * columns) not in activeExplosions:
				activeExplosions.append(x + i * columns)
			if breakBox:
				brokenBoxes.append(x + i * columns)
				break
		i += 1
		
	i = 1 # LEFT
	while i <= bombPower and ((x - i + 1) % columns) != 0 and gameArray[x - i] != 1:
		if gameArray[x - i] in bombs:
			Explode(x - i)
		else:
			breakBox = gameArray[x - i] == 2
			gameArray[x - i] = 10
			if (x - i) not in activeExplosions:
				activeExplosions.append(x - i)
			if breakBox:
				brokenBoxes.append(x - i)
				break
		i += 1
		
def UpdateBombs():
	for i in activeExplosions:
		gameArray[i] += 1
		if gameArray[i] >= 16:
			if i in brokenBoxes:
				rand = random.random()
				if rand < 0.1:
					gameArray[i] = 5
				elif rand < 0.18:
					gameArray[i] = 6
				else:
					gameArray[i] = 0
					if(gameArray[i+1]==2):
						gameArray[i+1]=0
						gameArray[i+2]=0
						gameArray[i+3]=0
						score[0]+=20
						if(gameArray[i+columns]==2):
							gameArray[i+columns]=0
							gameArray[i+columns+1]=0
							gameArray[i+columns+2]=0
							gameArray[i+columns+3]=0
						else:
							gameArray[i-columns]=0
							gameArray[i-columns+1]=0
							gameArray[i-columns+2]=0
							gameArray[i-columns+3]=0
					else:
						gameArray[i-1]=0
						gameArray[i-2]=0
						gameArray[i-3]=0
						score[0]+=20
						if(gameArray[i+columns]==2):
							gameArray[i+columns]=0
							gameArray[i+columns-1]=0
							gameArray[i+columns-2]=0
							gameArray[i+columns-3]=0
						else:
							gameArray[i-columns]=0
							gameArray[i-columns-1]=0
							gameArray[i-columns-2]=0
							gameArray[i-columns-3]=0
					

				brokenBoxes.remove(i)
			else:
				gameArray[i] = 0
			activeExplosions.remove(i)
			
	for i in activeBombs:
		gameArray[i] += 1
		if gameArray[i] >= 32:
			Explode(i)
def Main():
	global snakeHead, snakeTail, pPos, bombPower, maxBombs, activeBombCount, cnt 
	cnt=0
	
	while True: 													# Game; W=119, A=97, S=115, D=100	
		cnt+=1
		keycode = 0
		Render()
		EnemyMovement()
		
		
		startTime = time.time()
		
		while True:													# wait for input, keep frame length stable
			
			key = getch()
			print( "key:" + key)
			if key != "":
				keycode = ord(key)
				#time.sleep(spf - (time.time() - startTime))			# Wait for frame
				break
			elif time.time() - startTime > spf:
				break

				"""if msvcrt.kbhit():
				keycode = ord(msvcrt.getch())
				time.sleep(spf - (time.time() - startTime))			# Wait for frame
				break
				elif time.time() - startTime > spf:
				break"""
		
		if keycode == 119 : # UP
			
			if pPos >= columns:
				if gameArray[pPos - columns] in explosions:
					GameOver()
				elif ((gameArray[pPos-columns]==8) or ((gameArray[pPos+1-columns]==8)) or (gameArray[pPos+2-columns]==8) or (gameArray[pPos+3-columns]==8)):
					lives[0] -= 1
					if(lives[0]<=0):
						GameOver()
					else:
						pPos = 0
						InitArray()
						Main() 
				elif ((gameArray[pPos - columns] in [0, 5, 6]) and (gameArray[pPos+1-columns] in [0,5,6]) and (gameArray[pPos+2-columns] in [0,5,6]) and (gameArray[pPos+3-columns] in [0,5,6])):
					if gameArray[pPos] == 3:
						gameArray[pPos] = 20
						gameArray[pPos+1] = 0
						gameArray[pPos+2] = 0
						gameArray[pPos+3] = 0
						gameArray[pPos+54] = 0
						gameArray[pPos+55] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
						activeBombs.append(pPos)
						#activeBombs.append(pPos+1)
					else:
						gameArray[pPos] = 0
						gameArray[pPos+1] = 0
						gameArray[pPos+2] = 0
						gameArray[pPos+3] = 0
						gameArray[pPos+54] = 0
						gameArray[pPos+55] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
					pPos = pPos - columns
					if gameArray[pPos] == 5:
						bombPower += 1
						score += 1
					elif gameArray[pPos] == 6:
						maxBombs += 1
						score += 1
					gameArray[pPos] = 4
					gameArray[pPos+1] = 35
					gameArray[pPos+2] = 36
					gameArray[pPos+3] = 37
					gameArray[pPos+54] = 38
					gameArray[pPos+55] = 39
					gameArray[pPos+56] = 40
					gameArray[pPos+57] = 41
					

				
		elif keycode == 100: # RIGHT
			
			if (pPos + 4) % columns != 0:
				if gameArray[pPos + 4] in explosions:
					GameOver()
				elif ((gameArray[pPos+4]==8) or (gameArray[pPos+columns+4]==8)):
					lives[0] -= 1
					if(lives[0]<=0):
						GameOver()
					else:
						pPos = 0
						InitArray()
						Main()
				elif ((gameArray[pPos + 4] in [0, 5, 6]) and (gameArray[pPos+columns+4] in [0,5,6])):
					if gameArray[pPos] == 3:
						gameArray[pPos] = 20
						gameArray[pPos+1] = 0
						gameArray[pPos+2] = 0
						gameArray[pPos+3] = 0
						gameArray[pPos+54] = 0
						gameArray[pPos+55] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
						activeBombs.append(pPos)
						#activeBombs.append(pPos+1)
					else:
						gameArray[pPos] = 0
						gameArray[pPos+1] = 0
						gameArray[pPos+2] = 0
						gameArray[pPos+3] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
					pPos = pPos + 1
					if gameArray[pPos] == 5:
						bombPower += 1
						score += 1
					elif gameArray[pPos] == 6:
						maxBombs += 1
						score += 1
					gameArray[pPos] = 4
					gameArray[pPos+1] = 35
					gameArray[pPos+2] = 36
					gameArray[pPos+3] = 37
					gameArray[pPos+54] = 38
					gameArray[pPos+55] = 39
					gameArray[pPos+56] = 40
					gameArray[pPos+57] = 41
					
		elif keycode == 115: # DOWN
		
			if pPos < columns*(lines-2):
				if gameArray[pPos + columns] in explosions:
					GameOver()
				elif (gameArray[pPos+2*columns]==8 or gameArray[pPos+1+2*columns]==8 or gameArray[pPos+2+2*columns]==8 or gameArray[pPos+3+2*columns]==8):
					lives[0] -= 1
					if(lives[0]<=0):
						GameOver()
					else:
						pPos = 0
						InitArray()
						Main() 
				elif ((gameArray[pPos + 2*columns] in [0, 5, 6]) and (gameArray[pPos + 2*columns + 1] in [0, 5, 6]) and (gameArray[pPos + 2*columns + 2] in [0, 5, 6]) and (gameArray[pPos + 2*columns + 3] in [0, 5, 6])) :
					if gameArray[pPos] == 3:
						gameArray[pPos] = 20
						gameArray[pPos+1] = 0
						gameArray[pPos+2] = 0
						gameArray[pPos+3] = 0
						gameArray[pPos+54] = 0
						gameArray[pPos+55] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
						activeBombs.append(pPos)
						#activeBombs.append(pPos+1)
					else:
						gameArray[pPos] = 0
						gameArray[pPos+1] = 0
						gameArray[pPos+2] = 0
						gameArray[pPos+3] = 0
						gameArray[pPos+54] = 0
						gameArray[pPos+55] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
					pPos = pPos + columns
					if gameArray[pPos] == 5:
						bombPower += 1
						score += 1
					elif gameArray[pPos] == 6:
						maxBombs += 1
						score += 1
					#print("hi")
					gameArray[pPos] = 4
					gameArray[pPos+1] = 35
					gameArray[pPos+2] = 36
					gameArray[pPos+3] = 37
					gameArray[pPos+54] = 38
					gameArray[pPos+55] = 39
					gameArray[pPos+56] = 40
					gameArray[pPos+57] = 41
				
		elif keycode == 97: # LEFT
			
			if pPos % columns != 0:
				if gameArray[pPos - 1] in explosions:
					GameOver()
				elif (gameArray[pPos-1]==8 or gameArray[pPos+columns-1]==8):
					lives[0] -= 1
					if(lives[0]<=0):
						GameOver()
					else:
						pPos = 0
						InitArray()
						Main() 
				elif ((gameArray[pPos - 1] in [0, 5, 6]) and (gameArray[pPos+columns-1] in [0,5,6])):
					if gameArray[pPos] == 3:
						gameArray[pPos] = 20
						gameArray[pPos+1] = 0
						gameArray[pPos+2] = 0
						gameArray[pPos+3] = 0
						gameArray[pPos+54] = 0
						gameArray[pPos+55] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
						activeBombs.append(pPos)
						#activeBombs.append(pPos+1)
					else:
						gameArray[pPos] = 0
						gameArray[pPos+1] = 0
						gameArray[pPos+2] = 0
						gameArray[pPos+3] = 0
						gameArray[pPos+54] = 0
						gameArray[pPos+55] = 0
						gameArray[pPos+56] = 0
						gameArray[pPos+57] = 0
					pPos = pPos - 1
					if gameArray[pPos] == 5:
						bombPower += 1
						score += 1
					elif gameArray[pPos] == 6:
						maxBombs += 1
						score += 1
					gameArray[pPos] = 4
					gameArray[pPos+1] = 35
					gameArray[pPos+2] = 36
					gameArray[pPos+3] = 37
					gameArray[pPos+54] = 38
					gameArray[pPos+55] = 39
					gameArray[pPos+56] = 40
					gameArray[pPos+57] = 41
					
		elif keycode == 32:
			if activeBombCount < maxBombs:
				gameArray[pPos] = 3
				#gameArray[pPos+1] = 3

				activeBombCount += 1

		elif keycode == 81:
			sys.exit()
		 
		UpdateBombs()
		if gameArray[pPos] in explosions:
			GameOver()


	
InitArray()
lives[0] = 3
Main()