def russian(a,b):
	x = a; y = b
	z = 0

	while x >= 1:
		if x % 2 == 1:
			z = z + y
		x = int(x / 2)   #int() rounds to the lowest value
		y = y * 2

	return z

print russian(10,20)

print 5/2