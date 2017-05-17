'''
Problem 4 Description:

A palindromic number reads the same both ways. The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def find_largest_palindrome_product():
    '''Returns largest 3 digit palindrome number'''

    #Largest palindrome variable to be printed on screen
    largest_palindrome = 0

    #Nested for loop to multiply all the numbers
    for first_number in range(1, 1000):

        #second number never needs to be set lower than first number
        for second_number in range(first_number, 1000):
            product = first_number * second_number

            #Check if palindrome
            if check_if_palindrome(product):

                #If palindrome check if it's the biggest one
                if product > largest_palindrome:
                    largest_palindrome = product

    print largest_palindrome

def check_if_palindrome(number):
    '''checks if number is a palindrome'''

    #Convert to string to make this easier.
    number_string = str(number)

    #For loop only needs to do half length of string
    for i in range(0, len(number_string)/2):
        #works from the outside in.
        if number_string[i] == number_string[-(i+1)]:
            i += 1                                      #If they match continue algorithm
        else:
            return False                                #else return

    #If algorithm gets past for loop return true because it's a palindrome.
    return True

find_largest_palindrome_product()
