import os, time, sys, random, math
from termcolor import *
import termios
import atexit
from select import select
from ipscan import *
from board import *
from hero import *
from playermovement import *
from enemymovement import *
from gameover import *
from enemy import *
from bomb import *
random.seed()
pos = [0]*4
brd = Board(54)
rows=brd.getrows()
columns=brd.getcolumns()
playArea= [0]*rows*columns
lives = [0]*2
score = [0]*2
lives[0]=3
player=Hero(2,4,0)
pPos=player.getCurrentPosition()
explosions = range(10,16)
bombs = range(20,33)
bombPower = 2
maxBombs = 10
pos[1]=35*54+56
pos[2]=40*54+51	
pos[0]=4*54
activeBombs = []
activeExplosions = []
brokenBoxes = [] 
activeBombCount = 0
pPos=0
kb=KBHit()
brd.initialprint(pos,playArea,rows,columns)
e1=Enemy(2,2,pos[0])
for plr in (player , e1):
	if(plr.getCurrentPosition()<0 or plr.getCurrentPosition()>(54*54+54)):
		GameOver()
def GameOver():
	time.sleep(0.3)
	
	for i in range(3):
		os.system('clear')
		time.sleep(0.1)
		brd.render(playArea,lives,score)
		time.sleep(0.1)
		
	time.sleep(0.3)

	brd.render(playArea,lives,score)
	
	print ("Your final score is:", score[0])
	time.sleep(3)
	exit()

def main():
	global pPos, activeBombCount, maxBombs, bombPower
	while True: 														
		
		keycode = 0
		os.system('clear')
		brd.render(playArea,lives,score)
		
		
		
		startTime = time.time()
		
		if kb.kbhit():
			c = kb.getch()
			keycode = ord(c)
			if keycode == 119 : # UP
				
				if pPos >= columns:
					if playArea[pPos - columns] in explosions:
						GameOver()
					elif ((playArea[pPos-columns]==8) or ((playArea[pPos+1-columns]==8)) or (playArea[pPos+2-columns]==8) or (playArea[pPos+3-columns]==8)):
						lives[0] -= 1
						if(lives[0]<=0):
							GameOver()
						else:
							for i in range(0,4):
								playArea[pPos+i]=0
								playArea[pPos+54+i]=0
							pPos = 0
							brd.initialprint(pos,playArea,rows,columns)
							main()
							 
					elif ((playArea[pPos - columns] in [0, 5, 6]) and (playArea[pPos+1-columns] in [0,5,6]) and (playArea[pPos+2-columns] in [0,5,6]) and (playArea[pPos+3-columns] in [0,5,6])):
						if playArea[pPos] == 3:
							playArea[pPos] = 20
							playArea[pPos+1] = 0
							playArea[pPos+2] = 0
							playArea[pPos+3] = 0
							playArea[pPos+54] = 0
							playArea[pPos+55] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
							activeBombs.append(pPos)
							#activeBombs.append(pPos+1)
						else:
							playArea[pPos] = 0
							playArea[pPos+1] = 0
							playArea[pPos+2] = 0
							playArea[pPos+3] = 0
							playArea[pPos+54] = 0
							playArea[pPos+55] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
						pPos = pPos - columns
						if playArea[pPos] == 5:
							bombPower += 1
							
						elif playArea[pPos] == 6:
							maxBombs += 1
							
						playArea[pPos] = 4
						playArea[pPos+1] = 35
						playArea[pPos+2] = 36
						playArea[pPos+3] = 37
						playArea[pPos+54] = 38
						playArea[pPos+55] = 39
						playArea[pPos+56] = 40
						playArea[pPos+57] = 41
						

					
			elif keycode == 100: # RIGHT
				
				if (pPos + 4) % columns != 0:
					if playArea[pPos + 4] in explosions:
						GameOver()
					elif ((playArea[pPos+4]==8) or (playArea[pPos+columns+4]==8)):
						lives[0] -= 1
						if(lives[0]<=0):
							GameOver()
						else:
							for i in range(0,4):
								playArea[pPos+i]=0
								playArea[pPos+54+i]=0
							pPos = 0
							brd.initialprint(pos,playArea,rows,columns)
							main()
							
					elif ((playArea[pPos + 4] in [0, 5, 6]) and (playArea[pPos+columns+4] in [0,5,6])):
						if playArea[pPos] == 3:
							playArea[pPos] = 20
							playArea[pPos+1] = 0
							playArea[pPos+2] = 0
							playArea[pPos+3] = 0
							playArea[pPos+54] = 0
							playArea[pPos+55] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
							activeBombs.append(pPos)
							#activeBombs.append(pPos+1)
						else:
							playArea[pPos] = 0
							playArea[pPos+1] = 0
							playArea[pPos+2] = 0
							playArea[pPos+3] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
						pPos = pPos + 1
						if playArea[pPos] == 5:
							bombPower += 1
							
						elif playArea[pPos] == 6:
							maxBombs += 1
							
						playArea[pPos] = 4
						playArea[pPos+1] = 35
						playArea[pPos+2] = 36
						playArea[pPos+3] = 37
						playArea[pPos+54] = 38
						playArea[pPos+55] = 39
						playArea[pPos+56] = 40
						playArea[pPos+57] = 41
						
			elif keycode == 115: # DOWN
			
				if pPos < columns*(rows-2):
					if playArea[pPos + columns] in explosions:
						GameOver()
					elif (playArea[pPos+2*columns]==8 or playArea[pPos+1+2*columns]==8 or playArea[pPos+2+2*columns]==8 or playArea[pPos+3+2*columns]==8):
						lives[0] -= 1
						if(lives[0]<=0):
							GameOver()
						else:
							for i in range(0,4):
								playArea[pPos+i]=0
								playArea[pPos+54+i]=0
							pPos = 0
							brd.initialprint(pos,playArea,rows,columns)
							main()
							 
					elif ((playArea[pPos + 2*columns] in [0, 5, 6]) and (playArea[pPos + 2*columns + 1] in [0, 5, 6]) and (playArea[pPos + 2*columns + 2] in [0, 5, 6]) and (playArea[pPos + 2*columns + 3] in [0, 5, 6])) :
						if playArea[pPos] == 3:
							playArea[pPos] = 20
							playArea[pPos+1] = 0
							playArea[pPos+2] = 0
							playArea[pPos+3] = 0
							playArea[pPos+54] = 0
							playArea[pPos+55] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
							activeBombs.append(pPos)
							#activeBombs.append(pPos+1)
						else:
							playArea[pPos] = 0
							playArea[pPos+1] = 0
							playArea[pPos+2] = 0
							playArea[pPos+3] = 0
							playArea[pPos+54] = 0
							playArea[pPos+55] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
						pPos = pPos + columns
						if playArea[pPos] == 5:
							bombPower += 1
							
						elif playArea[pPos] == 6:
							maxBombs += 1
							
						#print("hi")
						playArea[pPos] = 4
						playArea[pPos+1] = 35
						playArea[pPos+2] = 36
						playArea[pPos+3] = 37
						playArea[pPos+54] = 38
						playArea[pPos+55] = 39
						playArea[pPos+56] = 40
						playArea[pPos+57] = 41
					
			elif keycode == 97: # LEFT
				
				if pPos % columns != 0:
					if playArea[pPos - 1] in explosions:
						GameOver()
					elif (playArea[pPos-1]==8 or playArea[pPos+columns-1]==8):
						lives[0] -= 1
						if(lives[0]<=0):
							GameOver()
						else:
							for i in range(0,4):
								playArea[pPos+i]=0
								playArea[pPos+54+i]=0
							pPos = 0
							brd.initialprint(pos,playArea,rows,columns)
							main()
							 
					elif ((playArea[pPos - 1] in [0, 5, 6]) and (playArea[pPos+columns-1] in [0,5,6])):
						if playArea[pPos] == 3:
							playArea[pPos] = 20
							playArea[pPos+1] = 0
							playArea[pPos+2] = 0
							playArea[pPos+3] = 0
							playArea[pPos+54] = 0
							playArea[pPos+55] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
							activeBombs.append(pPos)
							#activeBombs.append(pPos+1)
						else:
							playArea[pPos] = 0
							playArea[pPos+1] = 0
							playArea[pPos+2] = 0
							playArea[pPos+3] = 0
							playArea[pPos+54] = 0
							playArea[pPos+55] = 0
							playArea[pPos+56] = 0
							playArea[pPos+57] = 0
						pPos = pPos - 1
						if playArea[pPos] == 5:
							bombPower += 1
							
						elif playArea[pPos] == 6:
							maxBombs += 1
							
						playArea[pPos] = 4
						playArea[pPos+1] = 35
						playArea[pPos+2] = 36
						playArea[pPos+3] = 37
						playArea[pPos+54] = 38
						playArea[pPos+55] = 39
						playArea[pPos+56] = 40
						playArea[pPos+57] = 41
						
			elif keycode == 32:
				if activeBombCount < maxBombs:
					playArea[pPos] = 3
					#playArea[pPos+1] = 3

					activeBombCount += 1

			elif keycode == 81:
				sys.exit()
			UpdateBombs(playArea,columns,brokenBoxes,score,activeBombCount,activeExplosions,activeBombs,rows,bombPower,bombs)
			if playArea[pPos] in explosions:
				GameOver()
		else:
			time.sleep(0.5)
			if time.time() - startTime >= 0.5:
				EnemyMovement(pos,playArea,lives,score)
			elif time.time() - startTime >= 0.5:	
				if(activeBomb.size()>=1):
					UpdateBombs(playArea,columns,brokenBoxes,score,activeBombCount,activeExplosions,activeBombs,rows,bombPower,bombs)


			
main()
