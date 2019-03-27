from Funcs import *
import _thread
import time
import os

def ScreenDisplay():
	dots = '.'
	while True:
		print('Awesomeness Underway' + dots)
		time.sleep(1)
		os.system('cls')
		if dots == '.....': dots = '.'
		else: dots += '.'

def TheActualExecution():
	with open('TheOneWereOnRightNow.txt', 'r') as file:
		TheOneWereOnRightNow = int(file.read())
	while True:
		CalcAndWriteCSV(TheOneWereOnRightNow)
		TheOneWereOnRightNow += 1
		with open('TheOneWereOnRightNow.txt', 'w') as file:
			file.write(str(TheOneWereOnRightNow))


_thread.start_new_thread(ScreenDisplay, ())
_thread.start_new_thread(TheActualExecution, ())




while True:
	pass