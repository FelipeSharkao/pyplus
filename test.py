from pyplus import foreach

@foreach(5)
def anonym(iter):
	if (iter.val == 2):
		return iter.next

	print(iter.val)

print()

@foreach(['a', 'b', 'c', 'd', 'e'])
def anonym(iter):
	if (iter.key == 2):
		return iter.next

	print(iter.val)
