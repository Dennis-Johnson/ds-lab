num = int(input("Enter a number to factorize "))

factors = set()

for i in range(2, num):
	if num % i == 0:
		factors.add(i)

print('The factors of {} are {}'.format(num, factors))
