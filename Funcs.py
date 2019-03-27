def GetPers(number):
	persistance = 0

	while True:
		if len(str(number)) == 1: 
			break
		else:
			persistance += 1
			product = 1
			for each in str(number):
				product *= int(each)
			#print(product)
			number = product

	return persistance


numofcheckednums = 0


def CalcAndWriteCSV(index):
	global numofcheckednums
	with open('Table' + str(index) + '.csv', 'r') as file:
		contents = file.read().split('\n')
		lastentry = int(contents[-2].split(',')[0]) + 1

	with open('Table' + str(index) + '.csv', 'a') as file:
		while numofcheckednums <= 1000000:

			#contents = file.read().split('\n')

			ok = True

			if '0' in str(lastentry): ok = False

			if '5' in str(lastentry):
				if '2' in str(lastentry) or '4' in str(lastentry) or '6' in str(lastentry) or '8' in str(lastentry): ok = False

			if ok: 
				file.write(str(lastentry) + ',' + str(GetPers(lastentry)) + '\n')
				numofcheckednums += 1

			lastentry += 1
	numofcheckednums = 0
	with open('Table' + str(index + 1) + '.csv', 'a') as file:
		file.write(str(lastentry) + ',' + str(GetPers(lastentry)) + '\n')

			