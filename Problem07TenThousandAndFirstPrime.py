'''
Problem 7 Description:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

LIST_OF_PRIMES = [2, 3, 5, 7, 11, 13]

def biggest_prime():
    '''Returns whether number is prime or not'''

    #given up to element 13, only need to check odd numbers
    i = 13
    while True:
        i += 2
        #if prime, add to list of primes
        if is_prime(i):
            LIST_OF_PRIMES.append(i)

        #If list of primes is 10001 long, print last prime.
        if len(LIST_OF_PRIMES) >= 10001:
            print LIST_OF_PRIMES[-1]
            exit()

def is_prime(number):
    '''Checks if number is prime'''
    #only need to check if divisible by other primes
    for j in LIST_OF_PRIMES:
        #If the number isn't prime, return false.
        if number % j == 0:
            return False
    return True

#Call function
biggest_prime()
