'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache):
    if n < 0:
        return 0
    if n == 0:
        return 1
    # check the cache to see if it holds the answer this branch is looking for
    elif n in cache:
        return cache[n]
    else:
        # otherwise, n is not in the cache, so we need to computer the answer the "normal" way
        # Once the answer is computed, sve it in the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]

# test it
num_cookies = 5
cache = {i: 0 for i in range(num_cookies+1)}
print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to eat {num_cookies}")


# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5
#     print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")