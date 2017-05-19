'''
Problem 9 Description: Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def special_pythagorean_triplet():
    '''Returns special pythagorean triplte where a + b + c = 1000'''

    #Side_A must be between 1 and 333
    for side_a in range(1, 333):
        for side_b in range(side_a+1, 1000):

            #C^2 = A^2 + B^2
            side_c_squared = (side_a * side_a) + (side_b * side_b)

            #side_c = root(side_c^2)
            side_c = side_c_squared ** (1/2.0) #Originally tried to find this myself with a for loop

            #if side_c is an integer
            if int(side_c) == side_c:

                #Save time by breaking loop if a+b+c>1000
                if side_a + side_b + side_c > 1000:
                    break

                #if a+b+c == 1000, problem solved and exit
                if side_a + side_b + int(side_c) == 1000:
                    print side_a * side_b * int(side_c)
                    exit()

special_pythagorean_triplet()
