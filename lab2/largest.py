print("Program to determine largest amongst three numbers")
a = int(input('Enter a '))
b = int(input('Enter b '))
c = int(input('Enter c '))

largest = ((a if a > c else c) if a > b else (b if b > c else c))
print("Largest is %d" %(largest))
