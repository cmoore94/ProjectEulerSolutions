'''
Problem06 Description:

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
'''

def sum_square_difference():
    '''Prints the difference between the sum of squares and the squared sum'''
    #Set up variables
    sum_then_square = 0
    square_then_sum = 0

    #1-100 loop
    for i in range(1, 101):
        sum_then_square += i
        square_then_sum += i*i

    #Square at the end
    sum_then_square = sum_then_square * sum_then_square

    #Print at the end
    print sum_then_square - square_then_sum

sum_square_difference()
