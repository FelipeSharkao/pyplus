# pyplus
This is a in-development package for all those good things python lacks, like a classic `for`, `async` and `promise` from JS with those sweet sweet anonymous functions.  

### Instalation
Simply put the `pyplus` folder in your project root. Soon it will be avaliable as a package on *PyPI* so you can install with *pip*.

## each
Use the `each` functon to construct a very interactive *for* and *foreach*, giving you full control of the execution stream.

```python
for x in each(3, 7):
	if (x.val == 2):
		x.key += 1
		continue

	print(x.val) # 0 1 4 5 6
```

## More coming soon
