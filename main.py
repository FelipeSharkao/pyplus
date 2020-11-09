from pyplus import each

for x in each(3, 7):
	if (x.val == 2):
		x.key += 1
		continue

	print(x.val)

print()

for x in each(('a', 'b', 'c', 'd', 'e')):
	if (x.key == 1):
		x.key += 1
		continue

	print(x.val)

	if (x.key == 2):
		x.key += 1
		continue
	elif (x.key == 3):
		x.key -= 2
		continue
