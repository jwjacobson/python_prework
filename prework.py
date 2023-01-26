#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range(1, 100):
        if number % 2 == 1:
            print(number)

def first_odds_one_line():      # doing it in one line, codewars style
    [print(number) for number in range(1, 100) if number % 2 == 1]

#Question 3: write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    return max(a_list)

#Question 4: Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def is_leap_year(a_year):           # This function divides the set of all possible numbers into increasingly smaller subsets.
    if a_year % 4 == 0:             # First, separate numbers divisible by 4 from those that are not (all returning True will be divisible by 4)
        if a_year % 100 > 0:        # Of those divisible by 4, separate those not divisible by 100
            return True             # They are all leap years
        else:
            if a_year % 400 == 0:   # Of the remaining numbers, separate those divisible by 400
                return True         # They are our last subset of leap years
            else:
                return False        # Dispose of the rest
    else:
        return False                # Dispose of all numbers not divisible by 4

#Question 5: Write a function to check to see if all numbers in list are consecutive numbers.

def is_consecutive(a_list):
    x = 0                                   # I'm using a while loop to move through each item in the list, starting at the first item, with an index of [0].
    while x < len(a_list) - 1:              # len(a_list) - 1 is equivalent to the index of the last item in the list. 
        if a_list[x] + 1 != a_list[x + 1]:  # If the loop encounters a non-consecutive number,  
            return False                    # it immediately returns False.                                     
        else:
            x+=1                            # If it hasn't encountered a non-consecutive number, it increases x by 1 and tries again.
    return True                             # If the function makes it to the end of the loop then the list must have been consecutive.     