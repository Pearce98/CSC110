#
# Pearce Phanawong
# wheres_the_money.py
# Description: Program that helps user keep track of
#              how much money they earn and spend.
#
from os import _exit as exit

#title
print('-----------------------------')
print('----- WHERE\'S THE MONEY -----')
print('-----------------------------')

#Inputting variables and checking if they are int
salary = input('What is your annual salary?\n')
if salary.isnumeric() == False:
    print('Must enter positive integer for salary.')
    exit(0)
salary = int(salary)

rent = input('How much is your monthly mortgage or rent?\n')
if rent.isnumeric() == False:
    print('Must enter positive integer for mortgage or rent.')
    exit(0)
rent = int(rent)

bills = input('What do you spend on bills monthly?\n')
if bills.isnumeric() == False:
    print('Must enter positive integer for bills.')
    exit(0)
bills = int(bills)

food = input('What are your weekly grocery/food expenses?\n')
if food.isnumeric() == False:
    print('Must enter positive integer for food.')
    exit(0)
food = int(food)

travel = input('How much do you spend on travel annually?\n')
if travel.isnumeric() == False:
    print('Must enter positive integer for travel.')
    exit(0)
travel = int(travel)

#calculating tax range
if salary <= 15000:
    tax = int(salary) * 0.1
    ctax = 10
elif salary <= 75000:
    tax = int(salary) * 0.2
    ctax = 20
elif salary <= 200000:
    tax = salary * 0.25
    ctax = 25
else:
    tax = salary * 0.3
    ctax = 30
if tax >= 50000:
    tax = 50000
tax = int(tax)

#finding total, extra, and percentages
total = rent * 12 + bills * 12 + food * 52 + travel + tax
extra = int(salary - total)
prent = (rent / salary) * 1200
pbills = (bills / salary) * 1200
pfood = (food / salary) * 5200
ptravel = (travel / salary) * 100
ptax = (tax / salary) * 100
pextra = 100 - ptax - ptravel - pfood - pbills - prent

#number of dashes based on graph size
dashes = int(max(prent, pbills, pfood, ptravel, ptax, pextra))

#displaying the chart
print()
print('------------------------------------------' + '-' * dashes)
print('See the financial breakdown below, based on a salary of $' + str(salary))
print('------------------------------------------' + '-' * dashes)

print('| mortgage/rent | $ ' + str(format((rent * 12), '10,.2f')) + ' | '
+ str(format(prent, '5,.1f')) + '% | ' + '#' * int(prent))

print('|         bills | $ ' + str(format((bills * 12), '10,.2f')) + ' | '
+ str(format(pbills, '5,.1f')) + '% | ' + '#' * int(pbills))

print('|          food | $ ' + str(format((food * 52), '10,.2f')) + ' | '
+ str(format(pfood, '5,.1f')) + '% | ' + '#' * int(pfood))

print('|        travel | $ ' + str(format(travel, '10,.2f')) + ' | '
+ str(format(ptravel, '5,.1f')) + '% | ' + '#' * int(ptravel))

print('|           tax | $ ' + str(format(tax, '10,.2f')) + ' | '
+ str(format(ctax, '5,.1f')) + '% | ' + '#' * int(ctax))

print('|         extra | $ ' + str(format(extra, '10,.2f')) + ' | '
+ str(format(pextra, '5,.1f'))  + '% | ' + '#' * int(pextra))

print('------------------------------------------' + '-' * dashes)

#if costs are greater than salary, prints deficit
if extra < 0:
    print('>>> WARNING: DEFICIT <<<')

#prints this if the tax limit is reached
if tax == 50000:
    print('>>> TAX LIMIT REACHED <<<')

