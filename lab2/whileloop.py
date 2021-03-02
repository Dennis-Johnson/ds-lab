counter = 4

while True:
    if counter >= 0:
        print("Still in the loop, counter = %d" % (counter))
        counter -= 1
    else: 
        print("Exit condition reached in else stmt")
        break

