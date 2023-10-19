# Write code for algorithm 5 below
#Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.
def is_Palindrome(str):
    if len(str) == 1 or len(str) == 0 :
        return True
    else:
        return (str[0] == str[-1]) and is_Palindrome(str[1:-1])
    #is_Palindrome(str[1:-1]) gets rid of the first letter in the string and the last one after the compare then comapres the next two
    # for example s = "Hello World"
    #s = s[1:-1]
    # Result is s = "ello Worl"

print(is_Palindrome('apple'))
print(is_Palindrome('tacocat'))
print(is_Palindrome('radar'))