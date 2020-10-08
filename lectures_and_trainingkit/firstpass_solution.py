"""A FIRST PASS SOLUTION lecture with Tom Tarpley October 5th(6:30-8:30pm)

AGENDA:
======
1. Demo "Asking for help"
2. Breakout Rooms - group will decide on a question to ask
3. Demo the "Plan" Step of UPER
4. Demo "First-Pass" approaches (knapsack)

==========================
1. DEMO "ASKING FOR HELP =
==========================
At some point you will need to ask for help at your job: how will you formulate that question to make
    it easier for someone to help you.


What should you do if you were stuck while trying to format your Python output to use exactly 3 decimal places (using f-strings)

1. Attempt a solution. If it doesn't work **search and research** for fixes on your own. The following are some queries you could use:
    a. Search for a module that allows us to use the exact value of PI
    b. Recap how to format text with f-strings

2. Go to a forum such as Stack Overflow or the cohort's help channel in Slack.
    a. Write an **introduction of the problem**
    b. Provide source code or specific inputs that allow others to **reproduce the problem**
    c. **Proofread** your question so that it is easy to read and easy to answer

3. Keep an eye on your post, **responding to feedback** promptly

Example:(demo_0.py) 
-------
Print out the area of a circle to 3 decimal places in feet squared.

    First pass attempt
    How do we find the area of a circle?
    Let's just get the area and print it then work from there

So we need to:
    print out the output of something
    how do we find the area of a circle
    how do we format a number to 3 decimal places
"""

# 1. import math module to use math.pi or numpy to use np.pi
import numpy as np
import math 

# 2. Set a radius variable(r)
r = 3

# 3. Set an area of a circle by using pi * r * r(math.pi * r * r)
# area = (math.pi)*(r**2)
area = (np.pi)*(r**2)

# using rounding
print(f'The area of a circle is {round(area,3)} feet squared')

# or us the :.3f format
print(f'The area of a circle is {area:.3f} feet squared')

# look up unicode for squred feet (u+23CD)
# look up unicode for superscript for the 2 (U+00B2)
print(f'The area of a circle is {area:.3f} ft\u00b2 ')

""" 
===================
2. BREAKOUT ROOMS =
===================
    -How would you want a question asked to you? 
    -What are the relevant parts? 
    -What needs to be included in the question?

We went into breakout rooms and came up with a question to ask for it to be evaluated later to see if it was
    a good question or what have you"""

"""
=================================
3. Demo the "Plan" Step of UPER =
=================================

Let's come up with a plan for the following problem:

    We'll say that a positive int divides itself if every digit in the number divides into the number evenly. 
    For example, 128 divides itself since 1,2, and 8 all divide into 128 evenly.
    And we'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself
    
    Write a function to determine if a number divides itself.

    Problem on CodingBat (https://codingbat.com/prob/p165941)

Understand: review and think of clarifying questions to ask to better understand problem such as:
----------

    1. Do we need to handle non-numeric input? Doesnt say anything in description so leave it up to engineer
    2. How should we handle decimal values? We should only take in int
    3. Should this function return something? True or False?


Plan: think about what sort of things we can do
-----

    1. Loop through the digits in the number
    2. Use % to get the rightmost digit
    3. use / to discard the rightmost digit
    4. if dividing by a single digit leaves a remainder, return False 
    5. if the digit is a zero, return False
    6. if the loop exits without returning False, then return True 
"""

# # Then use pseudocode that you can use in your Execute phase
# def divides_self(num):
#     # Set a temp variable to hold the number
#     temp = num
#     # Loop through the digits in the number
#      # check if the digit is zero or if the num mod the digit is not zero
#     if num % 10 == 0:
#         # return False
#         return False 

#     # while the value is not zero, we will go through loop
#     while num != 0:
#         # check if our value modded against our num modded against 10 is not zero         
#         if temp % (num % 10) != 0:                                                       
#             # return False                                                                
#             return False

#         # divide our value by 10 to make sure we do not get an infinite loop
#         temp /= 10 
#     # return True since we exited loop without a False so has to be true
#     return True  

def divides_self(num):
    value = [int(x) for x in str(num)]
    for v in value:
        if v==0 or num % v != 0:
            return False
    return True 
    
# Test Cases 
print(divides_self(128))    # --> True
print(divides_self(12))     # --> True
print(divides_self(120))    # --> True

# first pass solution above still not working correctly - will do later

"""
4. Demo "First-Pass" approaches (knapsack)

Knapsack problem: 
    The idea is that we have a backpack with a size or weight limit that constrains how many things we can put inside.
    We have lots of items we want to put into the knapsack. However, they wont all fit. 
    Choosing the optimal combination of items taht meets size or weight constraints while maximizing value might seem
        doable with a small example, but this becomes a difficult problem very quickly.

    Example weights - need good ratio of value to weight to get optimal for backpack that can hold 15kg
    ---------------
    $4: 12 kg
    $2:  2 kg
    $2:  1 kg
    $10: 4 kg
    $10: 1 kg


"""
# First pass solution - naive_fill_knapsack
def naive_fill_knapsack(sack, items):
    """ Put highest value items in knapsack until full"""
    # Sort items by value
    items.sort(key=lambda i: i.value, reverse=True)

    weight = 0      # to keep track of the weight

    # Put most valuable items in knapsack until full
    # Loop over all items
    for i in items:
        # increment the weight by the items weight
        weight += i.weight
        # if weight is greater than 15
        if weight > 15:
            # return sack
            return sack 
        # otherwise
        else:
            # append the item to teh sack
            sack.append(i)
    return sack 

def brute_force_fill_knapsack(sack,item):
    """Try every combination to find the best"""

    # Generate all possible combinations of items

    # Calculate the value of all combinations

        # find the combo with the highest value

    return sack 
    pass

def greedy_fill_knapsack(sack,items):
    """Use ratio of [value] / [weight] to choose items for knapsack"""

    # Calculate efficiencies

    # Sort items by efficiency

    # Put items in knapsack until full

    return sack 
    pass
# Tests
# Below are a series of tests that can be utilized to demonstrate the differences
#   between each approach. Timing is included to give students an idea of how poorly
#   some approaches scale. However, efficiency should also be formalized using Big O notation.

fill_cave_with_items()
knapsack = []

# Test 1 - Naive
print('\nStarting test 1, naive approach...')
items = large_cave
start = time.time()
print_results(items, knapsack)

# Test 2 - Brute Force
# print('Starting test 2, brute force...')
# items = medium_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print_results(items, knapsack)

# Test 3 - Brute Force
# print('Starting test 3, brute force...')
# items = large_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print_results(items, knapsack)

# Test 4 - Greedy
# print('Starting test 4, greedy approach...')
# items = medium_cave
# start = time.time()
# greedy_fill_knapsack(knapsack, items)
# print_results(items, knapsack)

# Test 5 - Greedy
# print('Starting test 5, greedy approach...')
