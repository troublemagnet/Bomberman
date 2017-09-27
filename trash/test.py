import threading
from threading import Thread

class Func(threading.Thread):

	def run(self):
		for i in range(10):
			print(threading.currentThread().getName())

Gunnu = Func(name="Chin")
Neal = Func(name="Chan")

Gunnu.start()
Neal.start()