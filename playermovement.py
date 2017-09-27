
def playermovement(keycode,pPos,rows,columns,activeBombs,maxBombs,bombPower,explosions,playArea,activeBombCount,lives):

			if keycode == 119 : # UP
				
				if pPos >= columns:
					if playArea[pPos - columns] in explosions:
						GameOver()
					elif ((playArea[pPos-columns]==8) or ((playArea[pPos+1-columns]==8)) or (playArea[pPos+2-columns]==8) or (playArea[pPos+3-columns]==8)):
						lives[0] -= 1
						if(lives[0]<=0):
							GameOver()
						else:
							playArea[pPos]=0
							for i in range(0,4):
								playArea[pPos+i]=0
								playArea[pPos+54+i]=0

							pPos = 0

							Initialize()
							 
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
							Initialize()
							
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

							Initialize()
							 
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
							Initialize()
							 
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
