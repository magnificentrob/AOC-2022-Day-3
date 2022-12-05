woohoo = []
with open('input.txt') as file:
	for row in file:
		row = row.strip()
		woohoo.append(row)
alpha = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
total = 0

for i in range(0, len(woohoo), 3):
	a = (set(woohoo[i]) & set(woohoo[i+1]) & set(woohoo[i+2]))
	a = list(a)
	total+= alpha.index(a[0])+1
print(total)