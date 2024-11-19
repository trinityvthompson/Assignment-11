import sys

# Add Your functions here
def max_profit(money, num_houses, prices, increase):
    # create a dynamic programming table where dp_table[i][w] stores the max profit
    dp_table = [[0 for _ in range(money + 1)] for _ in range(num_houses + 1) ]

    # iterate over each house
    for i in range(1, num_houses + 1):
        for w in range(money + 1):
            # If the house price is greater than the current budget, skip it
            if prices[i - 1] <= w:
                # calculate the profit from selecting the house
                profit = prices[i - 1] * (increase[i - 1] / 100)
                # either don't pick the house or pick it and add its profit 
                dp_table[i][w] = max(dp_table[i - 1][w], profit + dp_table[i - 1][w - prices[i - 1]])
            else:
                # if the house price exceeds the current budget, drop it
                dp_table[i][w] = dp_table[i - 1][w]
    
    # the maximum profit will be in the dp_table[num_houses][money]
    return dp_table[num_houses][money]

# You are allowed to change the main function. 

# Do not change the template file name. 

def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)
    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])

# Add your implementation here .... 

# Add your functions and call them to generate the result. 
    result = max_profit(money, num_houses, prices, increase)
    print(result)

    

    
main()
