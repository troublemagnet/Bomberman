import random
def Explode(x, activeBombs, activeExplosions, playArea, bombs, activeBombCount, bombPower, rows, columns, brokenBoxes):
	
	activeBombs.remove(x)
	activeBombCount -= 1
	playArea[x] = 10
	activeExplosions.append(x)
	
	i = 1 # UP
	while i <= bombPower and (x - i * columns) >= 0 and playArea[x - i * columns] != 1:
		if playArea[x - i * columns] in bombs:
			Explode(x - i * columns, activeBombs, activeExplosions, playArea, bombs, activeBombCount, bombPower, rows, columns, brokenBoxes)
		else:
			breakBox = playArea[x - i * columns] == 2
			playArea[x - i * columns] = 10
			if (x - i * columns) not in activeExplosions:
				activeExplosions.append(x - i * columns)
			if breakBox:
				brokenBoxes.append(x - i * columns)
				break
		i += 1
		
	i = 1 # RIGHT
	while i <= bombPower and (x + i) % columns != 0 and playArea[x + i] != 1:
		if playArea[x + i] in bombs:
			Explode(x + i, activeBombs, activeExplosions, playArea, bombs, activeBombCount, bombPower, rows, columns, brokenBoxes)
		else:
			breakBox = playArea[x + i] == 2
			playArea[x + i] = 10
			if (x + i) not in activeExplosions:
				activeExplosions.append(x + i)
			if breakBox:
				brokenBoxes.append(x + i)
				break
		i += 1
		
	i = 1 # DOWN
	while i <= bombPower and (x + i * columns) <= (rows * columns - 1) and playArea[x + i * columns] != 1:
		if playArea[x + i * columns] in bombs:
			Explode(x + i * columns, activeBombs, activeExplosions, playArea, bombs, activeBombCount, bombPower, rows, columns, brokenBoxes)
		else:
			breakBox = playArea[x + i * columns] == 2
			playArea[x + i * columns] = 10
			if (x + i * columns) not in activeExplosions:
				activeExplosions.append(x + i * columns)
			if breakBox:
				brokenBoxes.append(x + i * columns)
				break
		i += 1
		
	i = 1 # LEFT
	while i <= bombPower and ((x - i + 1) % columns) != 0 and playArea[x - i] != 1:
		if playArea[x - i] in bombs:
			Explode(x - i, activeBombs, activeExplosions, playArea, bombs, activeBombCount, bombPower, rows, columns, brokenBoxes)
		else:
			breakBox = playArea[x - i] == 2
			playArea[x - i] = 10
			if (x - i) not in activeExplosions:
				activeExplosions.append(x - i)
			if breakBox:
				brokenBoxes.append(x - i)
				break
		i += 1
		
def UpdateBombs(playArea,columns,brokenBoxes,score,activeBombCount,activeExplosions,activeBombs,rows,bombPower,bombs):
	for i in activeExplosions:
		playArea[i] += 1
		if playArea[i] >= 16:
			if i in brokenBoxes:
				rand = random.random()
				if rand < 0.1:
					playArea[i] = 5
				elif rand < 0.18:
					playArea[i] = 6
				else:
					playArea[i] = 0
					if(playArea[i+1]==2):
						playArea[i+1]=0
						playArea[i+2]=0
						playArea[i+3]=0
						score[0]+=20
						if(playArea[i+columns]==2):
							playArea[i+columns]=0
							playArea[i+columns+1]=0
							playArea[i+columns+2]=0
							playArea[i+columns+3]=0
						else:
							playArea[i-columns]=0
							playArea[i-columns+1]=0
							playArea[i-columns+2]=0
							playArea[i-columns+3]=0
					else:
						playArea[i-1]=0
						playArea[i-2]=0
						playArea[i-3]=0
						score[0]+=20
						if(playArea[i+columns]==2):
							playArea[i+columns]=0
							playArea[i+columns-1]=0
							playArea[i+columns-2]=0
							playArea[i+columns-3]=0
						else:
							playArea[i-columns]=0
							playArea[i-columns-1]=0
							playArea[i-columns-2]=0
							playArea[i-columns-3]=0
					

				brokenBoxes.remove(i)
			else:
				playArea[i] = 0
			activeExplosions.remove(i)
			
	for i in activeBombs:
		playArea[i] += 2
		if playArea[i] >= 32:
			Explode(i, activeBombs, activeExplosions, playArea, bombs, activeBombCount, bombPower, rows, columns, brokenBoxes)
