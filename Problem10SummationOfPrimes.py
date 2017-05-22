'''
Problem 10 Description:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def sum_primes():
    '''prints sum of all primes from 2-2000000'''
    #Generate list of primes
    list_of_primes = sundaram3(2000000)

    #set up sum
    sum_of_primes = 0

    #go through list and add each number.
    for j in list_of_primes:
        sum_of_primes = sum_of_primes + j

    #Print Result
    print sum_of_primes


def sundaram3(max_n):
    '''Used sudarams sieve code for enerating primes, found here:
    https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/2073279#2073279
    Had originally tried brute forcing a solution by checking if it was divisible by other primes.
    Not fully sure how thit works yet, will need to look into it further.'''
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

sum_primes()
