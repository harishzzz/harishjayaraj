# 1.1 Implement a recursive function to celculate the factorial of a given number

"""
1! = 1 × 1
2! = 2 × 1! --->2
3! = 3× 2! --->3 × 2 × 1
.
.
10! = 10 × 9!¡ --->10 × 9 × 8 ×...×1

Formula - no × (n-1 )!
"""


def fact_rec(n):
 if n==0 or n==1:
   return 1
 else:
    return n*fact_rec(n-1)
                     
number = int(input("Enter a value :"))
res = fact_rec(number)
       
print("The factorial of {} is {}".format(number,res))



# importing the module
import calendar

# input the year 
year=int(input('Enter the value of year: '))
leap_year=calendar.isleap(year)

# checking leap year
if leap_year: # to check condition
    print('The given year is a leap year.')
else:
    print('The given year is a non-leap year.')