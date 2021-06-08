'''
map.py
input: expects countries.csv
'''
import fileinput

for i, line in enumerate(fileinput.input()):
    if i == 0: 
        continue #skip the row of column names
    
    # Get a single row from csv file
    data = line.strip().split(",")
    
    # Data row should have atleast 6 columns, skip this line otherwise.
    # More than 6 rows can occur when country name has a comma. For example "Korea, Dem."
    if len(data) < 6:
        print("Ignoring line {}".format(i))
        continue
    
    # Country name is usually just one column
    # Because of names with more than one word, we add the second condition
    country = data[0: (len(data) - 6 +1)]
    country = "".join(country)

    #Population is the second to last row
    population = data[-2]
    print ("{}\t{}".format(country, population))
