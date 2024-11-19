"""
Dynamic Programming Implementation

  File: maximum_profit.py
  Description: This program finds the maximum possible profit of purchasing a subset of the
  listed houses inputted via houses.txt file using dynamic programming.

  Student Name: Marissa Shuchart
  Student UT EID: ms87339

  Partner Name: Trinity Thompson
  Partner UT EID: tyt242

  Course Name: CS 313E
  Unique Number: 50165
  Date Created: 11/21/2024
  Date Last Modified: 11/21/2024

"""

import sys

def max_profit(money, num_houses, prices, increase):
    """
    This function finds the maximum possible profit of purchasing a subset of the listed houses
    using dynamic programming (based off of the knapsack example in class).
    """
    # create a dynamic programming table where dp_table[i][w] stores the max profit
    dp_table = [[0 for _ in range(money + 1)] for _ in range(num_houses + 1) ]

    # iterate over each house
    for i in range(1, num_houses + 1):
        for w in range(money + 1):
            if prices[i - 1] <= w:
                # calculate the profit from selecting the house
                profit = prices[i - 1] * (increase[i - 1] / 100)
                # either don't pick the house or pick it and add its profit
                dp_table[i][w] = max(dp_table[i - 1][w],
                                     profit + dp_table[i - 1][w - prices[i - 1]])
            else:
                # if the house price exceeds the current budget, drop it
                dp_table[i][w] = dp_table[i - 1][w]

    # the maximum profit will be in the dp_table[num_houses][money]
    return dp_table[num_houses][money]

def main():
    """
    This main function reads the input houses.txt file, calls the max_profit function
    and prints the result output.
    """
    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)

    # The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    # The third line is a list of house prices in million dollar which is a list of
    # \textit{integer numbers}
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i, _ in enumerate(prices):
        prices[i] = int(prices[i])

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i, _ in enumerate(increase):
        increase[i] = float(increase[i])

# Add your functions and call them to generate the result.
    result = max_profit(money, num_houses, prices, increase)
    print(f"{result:.2f}")

main()
