def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

lower = int(input("Enter a lower limit "))
upper = int(input("Enter a upper limit "))

for i in range(lower, upper):
    if isPrime(i):
        print(i)

