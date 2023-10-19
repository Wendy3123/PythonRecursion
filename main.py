# Write code for algorithm 1 below
#Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def num(x):
    if x == 0:
        return 0
    else:
        print(x)
        return num(x-1) 
print(num(6))

# Write code for algorithm 2 below
#Write a function that prints the natural numbers from 1 to n.
def natural_numbers(x,i=1):
	#your code here
    if i > x:
        return
    else: 
        print(i)
        natural_numbers(x,i+1)
natural_numbers(3)
#output: 1 2 3



# Write code for algorithm 4 below
# Write a function that calculates the value of 'a' to the power of 'b'.
# For example if a=2 and b=4, then power(2,4) would be calculating 2^4=2*2*2*2 so the result would be 16.

def square(a,b):
    if b < 1: 
        print('invalid input')
    elif b == 1:
        return a
    else:
        return a * square(a,b-1)
print(square(2,3))




