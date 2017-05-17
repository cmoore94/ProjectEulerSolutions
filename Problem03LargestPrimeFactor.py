'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

LIST_OF_PRIMES = [2]
LIST_OF_PRIME_FACTORS = []

def largest_prime(number):
    '''returns largest prime factor of 600851475143'''

    #Largest prime factor starts off as 1
    largest_prime_factor = 1

    #remainder will be 600851475143
    remainder = number

    #While loop. Variable declared outside
    i = 1
    while True:
        i += 1

        #If the number is prime, check if it's a factor
        if is_prime(i):

            #if it's a factor
            if remainder % i == 0:
                largest_prime_factor = i        #Set the largest prime factor
                multiply_factors = 1            #Set the multiply value to 1 to be checked in loop
                remainder = remainder / i       #remainder = remainder/prime factor
                LIST_OF_PRIME_FACTORS.append(largest_prime_factor) #Add prime factor to list

                i = 1 #There may be some optimization here if I set i to = lowest prime instead?

                #For loop that multiplies all prime factors to see if search is finished
                for j in LIST_OF_PRIME_FACTORS:
                    multiply_factors = multiply_factors * j

                    #If all prime factors found
                    if multiply_factors == number:
                        print "Largest Factor: ", largest_prime_factor
                        exit()


def is_prime(factor):
    '''Returns whether number is prime or not'''
    for i in LIST_OF_PRIMES:
        #if it's already in the list return true
        if factor == i:
            return True
        #If the number isn't prime, return false.
        if factor % i == 0:
            return False

    #Otherwise add it to the list and return true
    LIST_OF_PRIMES.append(factor)
    return True

#Call function
largest_prime(600851475143)
