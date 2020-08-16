"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""

def single_number(arr):
    for x in arr: # O(n)
    #   loop through every element in the list
        if arr.count(x) == 1:  # O(n)  --he looked up runtime complexity of .count()
    #       do a comparision to see if the two elements ever match
            return x

# Checking for a key in a dictionary is O(1) - constant time
# Inserting a key in a dictionary is O(1) - constant time

    s = set() # O(1)
    
    for x in arr: # O(n)
        if x in s: # O(1)
            s.remove(x)  # O(1)
        else:
            s.add(x)  # O(1)

    # at this point, we should only have one element in our set
    return list(s)[0]   # O (1)
                        # take our set, convert into list, and take 1st element out



if __name__ == '__main__':
    # use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
