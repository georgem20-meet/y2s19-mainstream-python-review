# Part 2 of the Python Review lab.
def is_prime(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True




def encode(x, y):
	while not is_prime(x):
		x+=1
	while not is_prime(y):
		y+=1
	if 1<y<250 and 500<x<10000:
		return x*y
	else:
	print( "Invalid input: Outside range")
	return None

def decode(coded_message):
	for i in range(2,250):
		print(y)
		x=coded_message/y
		if(is_prime(x) and (is_prime(y)))