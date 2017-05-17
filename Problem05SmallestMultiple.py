'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

#Doesn't include 11 for optimization
#Includes 16 as it's the only non prime that isn't made up of exactly 2 primes from 1-10
DIVISORS = [13, 16, 17, 19]

def find_smallest_multiple():
    '''Returns smallest multiple of all number 1-20'''
    i = 1
    multiple = 0
    while True:
        #will have to be a multiple of 2520 for it to be divisible by 1-10
        multiple = 2520 * i * 11    #multiply by 11 here to reduce run time
        #If divisible, print number and exit
        if check_if_divisible(multiple):
            print multiple
            exit()
        i += 1

def check_if_divisible(number):
    '''checks if number is divisible and returns boolean'''
    #checks if divisble by all primes
    for j in DIVISORS:
        #if any primes don't go in evenly, return false.
        if number % j != 0:
            return False
    return True

find_smallest_multiple()
