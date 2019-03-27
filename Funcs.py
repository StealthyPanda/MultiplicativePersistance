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


def CalcAndWriteCSV():
	with open('Table.csv', 'r') as file:
		contents = file.read().split('\n')
		lastentry = int(contents[-2].split(',')[0]) + 1

	with open('Table.csv', 'a') as file:
		while True:
			file.write(str(lastentry) + ',' + str(GetPers(lastentry)) + '\n')
			lastentry += 1

			