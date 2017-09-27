import time
def GameOver():
	time.sleep(0.3)
	
	for i in range(3):
		os.system('clear')
		time.sleep(0.1)
		brd.Render(playArea,lives,score)
		time.sleep(0.1)
		
	time.sleep(0.3)

	brd.Render(playArea,lives,score)
	
	print ("Oops, you died. Your final score is:", score[0])
	time.sleep(3)
	exit()