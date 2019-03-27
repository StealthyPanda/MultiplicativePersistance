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
	CalcAndWriteCSV()


_thread.start_new_thread(ScreenDisplay, ())
_thread.start_new_thread(TheActualExecution, ())




while True:
	pass