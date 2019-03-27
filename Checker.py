while True:
	entries = 0
	highestpers = 0
	highestnum = 0

	contents = ''
	with open('Table' + str(input('Enter file no.: ')) + '.csv', 'r') as file:
		contents = file.read().split('\n')[0:-1]


	for each in contents:
		entries += 1
		pers = int(each.split(',')[1])

		if pers > highestpers: 
			highestpers = pers
			highestnum = int(each.split(',')[0])

	print()
	print('Out of the ' + str(entries) + ' numbers checked in current Table, ' + str(highestpers) + ' is the highest persistance, of the number ' + str(highestnum) + '.')
	print()
	input('Enter to exit\n')