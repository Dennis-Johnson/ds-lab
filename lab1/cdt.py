#List operations
first  = [1,2,'Joe']
second = [3, 4, 'Jane']

print(first[0])
print(second * 2)
print(zip(first, second))

first.append('Doe')
print(first)

del second[2]
print(len(second))



#Tuples
tup = (1, 2, 'Dennis')

#Loops and Conditionals
#num = float(input('Enter a number'))
num = 12
if num>0:
	print('pos number')
elif num==0:
	print('zero')
else:
	print('Neg number')

x=5
print('Before 5')
if x==5:
	print ('this is 5')
	print('still 5')
	
print('After 5')
print('Before 6')
if x==6:
	print('this is 6')
print ('After 6')




#Ternary
age = 15
b = ('kid' if age < 18 else 'adult')
print(b)



#Loops
print("\n\nLoops")
print('Ex 1')
for i in range(4):
	print(i)

print('\nEx 2')
for item in ['one', 'two', 'three']:
	print(item) 

print('\nEx 3')
i = 2
while(i):
	print('Still running while loop')
	i-= 1

print('\nEx 4: Factors')
x= int(input('Enter a number: '))
for i in range(1,x+1):
	if x%i ==0:
		print(i)

print('\nEx 5: Largest in list')
x = [1,2,3,4]
largest = -1000
for i in x:
	if i > largest:
		largest = i
print('Largest is %d' % (largest))

print('\nEx 6: Smallest in list')
x = [1,2,3,4]
smallest = 1000
for i in x:
	if i < smallest:
		smallest = i
print('Smallest is %d' % (smallest))


print('\nEx 7: Count, Sum Average')
x = [1,2,3,4,5]
count, sum_, avg = 0,0,0
for i in x:
	sum_ += i
	count += 1
avg = sum_ / count
print("Count %d, Sum %d, Avg: %d" % (count, sum_, avg))

print('\nEx 8: Filtering')
x = [10,20,30,40,50]
for i in x:
	if i >= 30:
		print(i)

print('\nEx9: store result in another list')
res = []
for i in x: 
	if i > 20:
		res.append(i)
print(res)

print('\nEx 10: Replace')
y = np.zeros(len(x))
for i in range(len(x)):
	if x[i]>20:
	y[i]=x[i]
print(y)