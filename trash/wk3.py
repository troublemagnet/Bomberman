def EnemyMovement():
		x = random.randint(1,4)
		y = random.randint(1,4)
		z = random.randint(1,4)
		print x
		if x==1:
			#if(pos[0]>=54 and ((gameArray[pos[0]-54]>=10 and gameArray[pos[0]-54]<=15) or (gameArray[pos[0]]>=10 and gameArray[pos[0]]<=15))):
			#	pos[0]=-1
			if(pos[0]!=-1 and pos[0]>=54 and gameArray[(pos[0]-54)]!=1 and gameArray[pos[0]-54+1]!=1 and gameArray[pos[0]-54]!=4 and gameArray[pos[0]-54+1]!=4 and gameArray[pos[0]-54+1]!=2 and gameArray[pos[0]-54]!=2):
				
				gameArray[pos[0]-54]=8
				gameArray[pos[0]-54+1]=8
				gameArray[pos[0]+54]=0
				gameArray[pos[0]+55]=0
				pos[0]-=54

		elif x==2:
			#if((gameArray[pos[0]+56]==10 or gameArray[pos[0]]==10 or gameArray[pos[0]]==12 or gameArray[pos[0]]==14 or gameArray[pos[0]+56]==12 or gameArray[pos[0]+56]==14)):
			#	gameArray[pos[0]]=0
			#	pos[0]=-1
			if(pos[0]!=-1 and pos[0]+54<(54*54+54) and gameArray[pos[0]+54]!=1 and gameArray[pos[0]+54]!=4 and gameArray[pos[0]+54]!=2 and gameArray[pos[0]+54+1]!=1 and gameArray[pos[0]+54+1]!=4 and gameArray[pos[0]+54+1]!=2):
				gameArray[pos[0]+54]=8
				gameArray[pos[0]+55]=8
				gameArray[pos[0]-54]=0
				gameArray[pos[0]-53]=0
				gameArray[pos[0]]=0
				pos[0]+=54
		elif x==3:
			#if((gameArray[pos[0]+1]==10 or gameArray[pos[0]]==10 or gameArray[pos[0]]==12 or gameArray[pos[0]]==14 or gameArray[pos[0]+1]==12 or gameArray[pos[0]+1]==14)):
			#	gameArray[pos[0]]=0
			#	pos[0]=-1
			if(pos[0]!=-1 and pos[0]%54<52 and gameArray[pos[0]+2]!=1 and gameArray[pos[0]+2]!=4 and gameArray[pos[0]+2]!=2 and gameArray[pos[0]+2+columns]!=1 and gameArray[pos[0]+2+columns]!=4 and gameArray[pos[0]+2+columns]!=2):
				gameArray[pos[0]+1]=8
				gameArray[pos[0]+1+columns]=8
				gameArray[pos[0]]=0
				gameArray[pos[0]+columns]=0
				pos[0]+=1
		elif x==4:
			#if((gameArray[pos[0]-1]==10 or gameArray[pos[0]]==10 or gameArray[pos[0]]==12 or gameArray[pos[0]]==14 or gameArray[pos[0]-1]==12 or gameArray[pos[0]-1]==14)):
			#	gameArray[pos[0]]=0
			#	pos[0]=-1
			if(pos[0]!=-1 and pos[0]%54>0 and gameArray[pos[0]-1]!=1 and gameArray[pos[0]-1]!=4 and gameArray[pos[0]-1]!=2 and pos[0]%54!=0):
				gameArray[pos[0]-1]=8
				gameArray[pos[0]-1+columns]=8
				gameArray[pos[0]+1]=0
				gameArray[pos[0]+1+columns]=0

				pos[0]-=1
		
		if y==1:
			#if((gameArray[pos[1]-54]==10 or gameArray[pos[1]]==10 or gameArray[pos[1]]==12 or gameArray[pos[1]]==14 or gameArray[pos[1]-54]==12 or gameArray[pos[1]-54]==14)):
			#	gameArray[pos[1]]=0
			#	pos[1]=-1
			if(pos[1]-54>=0 and gameArray[pos[1]-54]!=1 and pos[1]-54>=0 and gameArray[pos[1]-54]!=4 and gameArray[pos[1]-54]!=2 ):
				gameArray[pos[1]-54]=8
				gameArray[pos[1]]=0
				pos[1]-=54
		elif y==2:
			#if((gameArray[pos[1]+56]==10 or gameArray[pos[1]]==10 or gameArray[pos[1]]==12 or gameArray[pos[1]]==14 or gameArray[pos[1]+56]==12 or gameArray[pos[1]+56]==14)):
			#	gameArray[pos[1]]=0
			#	pos[1]=-1
			if(pos[1]+54<(54*54+54) and gameArray[pos[1]+54]!=1 and pos[1]+54<(54*54+54) and gameArray[pos[1]+54]!=4 and gameArray[pos[1]+54]!=2):
				gameArray[pos[1]+54]=8
				gameArray[pos[1]]=0
				pos[1]+=54
		elif y==3:
			#if((gameArray[pos[1]+1]==10 or gameArray[pos[1]]==10 or gameArray[pos[1]]==12 or gameArray[pos[1]]==14 or gameArray[pos[1]+1]==12 or gameArray[pos[1]+1]==14)):
			#	gameArray[pos[1]]=0
			#	pos[1]=-1
			if(pos[1]%54!=53 and gameArray[pos[1]+1]!=1 and pos[1]%54!=44 and gameArray[pos[1]+1]!=4 and gameArray[pos[1]+1]!=2 and pos[1]%54!=44):
				gameArray[pos[1]+1]=8
				gameArray[pos[1]]=0
				pos[1]+=1
		elif y==4:
			#if((gameArray[pos[1]-1]==10 or gameArray[pos[1]]==10 or gameArray[pos[1]]==12 or gameArray[pos[1]]==14 or gameArray[pos[1]-1]==12 or gameArray[pos[1]-1]==14)):
			#	gameArray[pos[1]]=0
			#	pos[1]=-1
			if(pos[1]%54!=0 and gameArray[pos[1]-1]!=1 and pos[1]%54!=0 and gameArray[pos[1]-1]!=4 and gameArray[pos[1]-1]!=2 and pos[1]%54!=0):
				gameArray[pos[1]-1]=8
				gameArray[pos[1]]=0
				pos[1]-=1
		if z==1:
			#if((gameArray[pos[2]-54]==10 or gameArray[pos[2]]==10 or gameArray[pos[2]]==12 or gameArray[pos[2]]==14 or gameArray[pos[2]-54]==12 or gameArray[pos[2]-54]==14)):
			#	gameArray[pos[2]]=0
			#	pos[2]=-1
			if(pos[2]-54>=0 and gameArray[pos[2]-54]!=1 and pos[2]-54>=0 and gameArray[pos[2]-54]!=4 and gameArray[pos[2]-54]!=2 and pos[2]-54>=0):
				gameArray[pos[2]-54]=8
				gameArray[pos[2]]=0
				pos[2]-=54
		elif z==2:
			#if((gameArray[pos[2]+56]==10 or gameArray[pos[2]]==10 or gameArray[pos[2]]==12 or gameArray[pos[2]]==14 or gameArray[pos[2]+56]==12 or gameArray[pos[2]+56]==14)):
			#	gameArray[pos[2]]=0
			#	pos[2]=-1
			if(pos[2]<(54*54-1) and gameArray[pos[2]+54]!=1 and pos[2]+54<(54*54+54) and gameArray[pos[2]+54]!=4 and gameArray[pos[2]+54]!=2 and pos[2]+54<(54*54+54)):
				gameArray[pos[2]+54]=8
				gameArray[pos[2]]=0
				pos[2]+=54
		elif z==3:
			#if((gameArray[pos[2]+1]==10 or gameArray[pos[2]]==10 or gameArray[pos[2]]==12 or gameArray[pos[2]]==14 or gameArray[pos[2]+1]==12 or gameArray[pos[2]+1]==14)):
			#	gameArray[pos[2]]=0
			#	pos[2]=-1
			if(pos[2]%54!=53 and gameArray[pos[2]+1]!=1 and pos[2]%54!=44 and gameArray[pos[2]+1]!=4 and gameArray[pos[2]+1]!=2 and pos[2]%54!=44):
				gameArray[pos[2]+1]=8
				gameArray[pos[2]]=0
				pos[2]+=1
		elif z==4:
			#if((gameArray[pos[2]-1]==10 or gameArray[pos[2]]==10 or gameArray[pos[2]]==12 or gameArray[pos[2]]==14 or gameArray[pos[2]-1]==12 or gameArray[pos[2]-1]==14)):
			#	gameArray[pos[2]]=0
			#	pos[2]=-1
			if(pos[2]%54!=0 and gameArray[pos[2]-1]!=1 and pos[2]%54!=0 and gameArray[pos[2]-1]!=4 and gameArray[pos[2]-1]!=2 and pos[2]%54!=0):
				gameArray[pos[2]-1]=8
				gameArray[pos[2]]=0
				pos[2]-=1
		if((gameArray[pos[0]]==4 or gameArray[pos[0]] in [35,41]) or (gameArray[pos[1]]==4 or gameArray[pos[1]] in [35,41]) or (gameArray[pos[2]]==4 or gameArray[pos[2]] in [35,41])):
			lives[0]-=1
			if(lives[0]==0):
				GameOver()

