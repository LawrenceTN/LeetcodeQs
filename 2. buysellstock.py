# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# how i tackled this: 
# find the smallest value as you iterate through the list 1-by-1. do this by comparing it to the largest number (infinity)
# when you find the smallest number so far, subtract it by the subsequent numbers and compare the differences between each other
# the biggest difference will be the largest profit

prices = [7,1,5,3,6,4]

def maxProfit(prices):
    lowest_stock = float('inf')
    diff = 0
    largest_profit = 0

    for price in prices:
        if price < lowest_stock:
            lowest_stock = price
        diff = price - lowest_stock
        if diff > largest_profit:
            largest_profit = diff
        
    print(largest_profit)

maxProfit(prices)









# class Solution(object):
#     def maxProfit(self, prices):
#         smallest = float('inf')
#         diff = 0
#         max_profit = 0

#         for num in prices:
#             if num < smallest:
#                 smallest = num
#             diff = num - smallest
#             if diff > max_profit:
#                 max_profit = diff
#         return max_profit
    