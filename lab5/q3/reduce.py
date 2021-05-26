'''
reduce.py
'''
import fileinput

creditor_count = 0
credit_total = 0

for line in fileinput.input():

    data = line.strip().split("\t")    

    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    creditability, creditAmt = data

    creditor_count += 1
    credit_total += int(creditAmt)

print ("Creditor Count: ", creditor_count, "\t","Credit Total", credit_total)

