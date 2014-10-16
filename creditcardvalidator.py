#Global variables for program. Credit card variables are not used in the code, but stored for potential use later on
number =  input("Enter a credit card number: ")
card_number = int(number)
visa = 4
master = 5
amex = 37
discover = 6

#Function that calculates the sum of the odd and even place numbers to determine if the card is valid or invalid
def is_valid(card_number):
    '''
    Return true if the card number is valid
    Return false if the card number is invalid
    '''
    result_2_3 = sum_of_odd_place(card_number) + sum_of_double_even_place(card_number)
    if result_2_3 % 10 == 0:
        print("Valid")
    else:
        print("Invalid")

#Sum of even place variables
def sum_of_double_even_place( card_number ):
    '''
    Get the result from Step 2
    '''
    x = get_size(card_number) 
    if x % 2:
        x = x - 1
        
    result = 0
    for digit_to_calc in range(2, x+1, 2):
        result += get_digit(digit_to_calc)
    return result    
        
        
        
#Function that uses an if-else statement to return either a single digit or the sum of 2 larger digits 
def get_digit( num ):
    '''
    Return this number if it is a single digit, otherwise return the sum of the two digits
    '''
    num = -1 * num
    red = int(number[num])
    red = red * 2
    if red <= 10:
        return red
    else:
        return (red // 10) + (red % 10)
     
#Sum of the odd place digits
def sum_of_odd_place( card_number ):
    '''
    Return the sum of odd-place digits in card_number
    '''
    x = get_size(card_number) 

    str_card_number = str(card_number)   
    result_odd = 0
    for digit_to_calculate in range(1, x, 2):
        result_odd += int(str_card_number[digit_to_calculate])
    return result_odd
 
#Determines if the card prefix is a valid credit card company
def prefix_match( card_number, prefix_num ):
    '''
    #Return true if the prefix_num digit is a prefix for card_number
    '''
    number = str(card_number)
    if number[0] == "4":
        True
    elif number[0] == "5":
        True
    elif number[0] == "6":
        True
    elif (number[0:1] == "37"):
        True
    else:
        False        
    return


def get_size( card_number ):
    #Takes variable digit and converts the card number to str in order to call its length
    '''
    Return the number of digits in digit 
    '''
    digit = len(str(card_number))
    return digit

#returns the first digit(s)(depending on credit card company) of the card number based on the if statement below the function
def get_prefix( card_number, k ):
    '''
    Return the first k number of digits from number.
    If the number of digits in number is less than k, return number
    '''
    return str(card_number)[0:k]

is_valid(card_number)

#if statement for k to determine if it is an amex card based on the standard amex card digit length being 15
#otherwise, k remains 1
k = 1
if get_size(card_number) == 15:
    k = 2

prefix_num = get_prefix(card_number, k)

