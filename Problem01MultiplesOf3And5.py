'''
Problem 1.

Description:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum_of_multiples_of_3_and_5():
    ''' returns the sum of all multiples of either 3 or 5 '''
    #Sum set up at beginning to keep track.
    sum_of_multiples = 0

    #For loop between 0 and 1000.
    for i in range(0, 1000):
        if i % 3 == 0:          #If divisible by 3
            sum_of_multiples += i
        elif i % 5 == 0:        #else if divisible by 5
            sum_of_multiples += i

    print sum                   #print answer

sum_of_multiples_of_3_and_5()
