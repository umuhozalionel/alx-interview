#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be met.

    Returns:
        int: Fewest number of coins needed to meet total.
             If total cannot be met, return -1.
             If total is 0 or less, return 0.
    """
    if total <= 0:
        return 0

    # Initialize a list to hold the minimum coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(
                    min_coins[i],
                    min_coins[i - coin] + 1
                )

    if min_coins[total] != float('inf'):
        return min_coins[total]
    else:
        return -1
