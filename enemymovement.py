import random
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
def EnemyMovement(pos,playArea,lives,score):
		
		x = random.randint(3,4)
		y = random.randint(1,2)
		z = random.randint(1,2)
		#print x
		if x==1:
			if(pos[0]!=-1 and pos[0]-54>=0 and playArea[(pos[0]-54)]!=1 and playArea[pos[0]-54]!=4 and playArea[pos[0]-54]!=2 and playArea[pos[0]+1-54]!=1 and playArea[pos[0]+1-54]!=2 and playArea[pos[0]+1-54]!=4):
				playArea[pos[0]-54]=8
				playArea[pos[0]-54+1]=8
				playArea[pos[0]+54]=0
				playArea[pos[0]+54+1]=0
				pos[0]-=54

		elif x==2:
			if(pos[0]!=-1 and pos[0]<(51*54) and playArea[pos[0]+54]!=1 and playArea[pos[0]+54]!=4 and playArea[pos[0]+54]!=2 and playArea[pos[0]+54+1]!=1 and playArea[pos[0]+54+1]!=4 and playArea[pos[0]+54+1]!=2):
				playArea[pos[0]+54]=8
				playArea[pos[0]+54+1]=8
				playArea[pos[0]-54]=0
				playArea[pos[0]+1-54]=0
				pos[0]+=54
		elif x==3:
			if(pos[0]!=-1 and pos[0]%54<51 and playArea[pos[0]+2]!=1 and playArea[pos[0]+2]!=4 and playArea[pos[0]+2]!=2 and playArea[pos[0]+54+2]!=1 and playArea[pos[0]+54+2]!=4 and playArea[pos[0]+54+2]!=2):
				playArea[pos[0]+1]=8
				playArea[pos[0]+1+54]=8
				playArea[pos[0]-1+54]=0
				playArea[pos[0]-1]=0
				pos[0]+=1
		elif x==4:
			if(pos[0]!=-1 and pos[0]%54>1 and playArea[pos[0]-1]!=1 and playArea[pos[0]-1]!=4 and playArea[pos[0]-1]!=2 and playArea[pos[0]+54-1]!=1 and playArea[pos[0]+54-1]!=4 and playArea[pos[0]+54-1]!=2):
				playArea[pos[0]-1]=8
				playArea[pos[0]+54-1]=8
				playArea[pos[0]+1]=0
				playArea[pos[0]+54+1]=0
				pos[0]-=1
		
		if y==1:
			if(pos[1]!=-1 and pos[1]-54>=0 and playArea[(pos[1]-54)]!=1 and playArea[pos[1]-54]!=4 and playArea[pos[1]-54]!=2 and playArea[pos[1]+1-54]!=1 and playArea[pos[1]+1-54]!=2 and playArea[pos[1]+1-54]!=4):
				playArea[pos[1]-54]=8
				playArea[pos[1]-54+1]=8
				playArea[pos[1]+54]=0
				playArea[pos[1]+54+1]=0
				pos[1]-=54
		elif y==2:
			if(pos[1]!=-1 and pos[1]<(51*54) and playArea[pos[1]+54]!=1 and playArea[pos[1]+54]!=4 and playArea[pos[1]+54]!=2 and playArea[pos[1]+54+1]!=1 and playArea[pos[1]+54+1]!=4 and playArea[pos[1]+54+1]!=2):
				playArea[pos[1]+54]=8
				playArea[pos[1]+54+1]=8
				playArea[pos[1]-54]=0
				playArea[pos[1]+1-54]=0
				pos[1]+=54
		elif y==3:
			if(pos[1]!=-1 and pos[1]%54<51 and playArea[pos[1]+2]!=1 and playArea[pos[1]+2]!=4 and playArea[pos[1]+2]!=2 and playArea[pos[1]+54+2]!=1 and playArea[pos[1]+54+2]!=4 and playArea[pos[1]+54+2]!=2):
				playArea[pos[1]+1]=8
				playArea[pos[1]+1+54]=8
				playArea[pos[1]-1+54]=0
				playArea[pos[1]-1]=0
				pos[1]+=1
		elif y==4:
			if(pos[1]!=-1 and pos[1]%54>1 and playArea[pos[1]-1]!=1 and playArea[pos[1]-1]!=4 and playArea[pos[1]-1]!=2 and playArea[pos[1]+54-1]!=1 and playArea[pos[1]+54-1]!=4 and playArea[pos[1]+54-1]!=2):
				playArea[pos[1]-1]=8
				playArea[pos[1]+54-1]=8
				playArea[pos[1]+1]=0
				playArea[pos[1]+54+1]=0
				pos[1]-=1
		if z==1:
			if(pos[2]!=-1 and pos[2]-54>=0 and playArea[(pos[2]-54)]!=1 and playArea[pos[2]-54]!=4 and playArea[pos[2]-54]!=2 and playArea[pos[2]+1-54]!=1 and playArea[pos[2]+1-54]!=2 and playArea[pos[2]+1-54]!=4):
				playArea[pos[2]-54]=8
				playArea[pos[2]-54+1]=8
				playArea[pos[2]+54]=0
				playArea[pos[2]+54+1]=0
				pos[2]-=54
		elif z==2:
			if(pos[2]!=-1 and pos[2]<(51*54) and playArea[pos[2]+54]!=1 and playArea[pos[2]+54]!=4 and playArea[pos[2]+54]!=2 and playArea[pos[2]+54+1]!=1 and playArea[pos[2]+54+1]!=4 and playArea[pos[2]+54+1]!=2):
				playArea[pos[2]+54]=8
				playArea[pos[2]+54+1]=8
				playArea[pos[2]-54]=0
				playArea[pos[2]+1-54]=0
				pos[2]+=54
		elif z==3:
			if(pos[2]!=-1 and pos[2]%54<51 and playArea[pos[2]+2]!=1 and playArea[pos[2]+2]!=4 and playArea[pos[2]+2]!=2 and playArea[pos[2]+54+2]!=1 and playArea[pos[2]+54+2]!=4 and playArea[pos[2]+54+2]!=2):
				playArea[pos[2]+1]=8
				playArea[pos[2]+1+54]=8
				playArea[pos[2]-1+54]=0
				playArea[pos[2]-1]=0
				pos[2]+=1
		elif z==4:
			if(pos[2]!=-1 and pos[1]%54>1 and playArea[pos[2]-1]!=1 and playArea[pos[2]-1]!=4 and playArea[pos[2]-1]!=2 and playArea[pos[2]+54-1]!=1 and playArea[pos[2]+54-1]!=4 and playArea[pos[2]+54-1]!=2):
				playArea[pos[2]-1]=8
				playArea[pos[2]+54-1]=8
				playArea[pos[2]+1]=0
				playArea[pos[2]+54+1]=0
				pos[2]-=1
		if((playArea[pos[0]]==4 or playArea[pos[0]] in [35,41]) or (playArea[pos[1]]==4 or playArea[pos[1]] in [35,41]) or (playArea[pos[2]]==4 or playArea[pos[2]] in [35,41])):
			lives[0]-=1
			if(lives[0]==0):
				GameOver()
		if((playArea[pos[0]]>=10 and playArea[pos[0]]<=15) or (playArea[pos[0]+1]>=10 and playArea[pos[0]+1]<=15) or (playArea[pos[0]+54]>=10 and playArea[pos[0]+54]<=15) or (playArea[pos[0]+54+1]>=10 and playArea[pos[0]+54+1]<=15)):
					
					score[0]+=100
					playArea[pos[0]]=0
					playArea[pos[0]+1]=0
					playArea[pos[0]+54]=0
					playArea[pos[0]+55]=0
					pos[0]=-1
		if((playArea[pos[1]]>=10 and playArea[pos[1]]<=15) or (playArea[pos[1]+1]>=10 and playArea[pos[1]+1]<=15) or (playArea[pos[1]+54]>=10 and playArea[pos[1]+54]<=15) or (playArea[pos[1]+54+1]>=10 and playArea[pos[1]+54+1]<=15)):
					
					score[0]+=100
					playArea[pos[1]]=0
					playArea[pos[1]+1]=0
					playArea[pos[1]+54]=0
					playArea[pos[1]+55]=0
					pos[1]=-1
		if((playArea[pos[2]]>=10 and playArea[pos[2]]<=15) or (playArea[pos[2]+1]>=10 and playArea[pos[2]+1]<=15) or (playArea[pos[2]+54]>=10 and playArea[pos[2]+54]<=15) or (playArea[pos[2]+54+1]>=10 and playArea[pos[2]+54+1]<=15)):
					
					score[0]+=100
					playArea[pos[2]]=0
					playArea[pos[2]+1]=0
					playArea[pos[2]+54]=0
					playArea[pos[2]+55]=0
					pos[2]=-1