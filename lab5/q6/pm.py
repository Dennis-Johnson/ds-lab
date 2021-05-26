from operator import itemgetter
import sys

current_year = None
year_tot = []
year_male = []
year_fem = []
month_tot = []
month_male = []
month_fem = []

specyear = 2001

for i in range(40):
	year_tot.append(0)
	year_male.append(0)
	year_fem.append(0)

for i in range(12):
	month_tot.append(0)
	month_male.append(0)
	month_fem.append(0)

for line in sys.stdin:
    sex, month, year = line.strip().split(' ')
    try: 
        sex = int(sex)
        month = int(month)
        year = int(year)
    except ValueError:
        print("Not a number, skipping line")
        continue

    year_tot[year - 1980] += 1

    if sex == 0:
    	year_male[year - 1980] += 1
    else:
    	year_fem[year - 1980] += 1
    
    if year == specyear:
    	month_tot[month - 1] += 1
    	if sex == 0:
    		month_male[month - 1] += 1
    	else:
    		month_fem[month - 1] += 1

for i in range(40):
    if year_tot[i] == 0:
        continue

    print('Year %d Total: %d' %(i+1980, year_tot[i]))
    print('Males: %d' %(year_male[i]))
    print('Females: %d' %(year_fem[i]))
    print('\n')

print('Year %d'% (specyear))

for i in range(12):
    if month_tot[i] == 0:
        continue
    print('Month %d Total: %d' %(i+1, month_tot[i]))
    print('Males: %d' %(month_male[i]))
    print('Females: %d' %(month_fem[i]))
    print('\n')
