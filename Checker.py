entries = 0
highest = 0

contents = ''
with open('Table.csv', 'r') as file:
	contents = file.read().split('\n')

for each in contents:
	entries += 1
	pers = int(each.split(',')[1])

	if pers > highest: highest = pers

print('Out of the ' + str(entries) + ' numbers checked in current Table.csv, ' + str(highest) + ' is the highest persistance.')
