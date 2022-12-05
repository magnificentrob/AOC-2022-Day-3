woohoo = []
with open('input.txt') as file:
	for row in file:
		row = row.strip()
		half = round(len(row)/2)
		rucksack1 = row[:half]
		rucksack2 = row[half:]
		for i in rucksack1:
			if i in rucksack2:
				woohoo.append(i)
				break
alpha = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
total = 0
for i in woohoo:
	total+= alpha.index(i)+1
print(total)