#!/usr/bin/python

import sys
denominations = [1,5,10, 25, 50]
# recursive
def making_change(amount, denominations):
  if (amount<0):
    return 0
  elif (amount == 0):
    return 1
  else:
    return sum([making_change(amount, denominations) for amount in denominations])
print(making_change(5, [1,5,10,25,50]))

# dynamic
# target = 200
# coins = [1,2,5,10,20,50,100,200]
# ways = [1]+[0]*target
# for coin in coins:
#     for i in range(coin,target+1):
#         ways[i]+=ways[i-coin]
# print(ways[target])

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")