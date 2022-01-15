# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 1/13/2021
# Description:
num = int(input("Please enter an amount in cents less than a dollar"
 "\n"))
q = num // 25
num %= 25
d = num // 10
num %= 10
n =  num // 5
num %= 5
c = num % 5
print("Your change will be:")
print("Q" + str(q))
print("D" + str(d))
print("N" + str(n))
print("P" + str(c))

