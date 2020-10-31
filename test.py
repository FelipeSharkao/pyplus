from pyplus import foreach

@foreach(3, 7)
def anonym(iter):
	if (iter.val == 2):
		return iter.skipone()

	print(iter.val)

print()

@foreach(['a', 'b', 'c', 'd', 'e'])
def anonym(iter):
	if (iter.key == 1):
		return iter.skipone()

	print(iter.val)

	if (iter.key == 2):
		return iter.skipone()
	elif (iter.key == 3):
		return iter.prev()
