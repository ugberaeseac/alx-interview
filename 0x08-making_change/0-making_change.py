#!/usr/bin/python3
"""
Greedy algorithm to find the least number of coins needed
to make change for a given amount of total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination of
    coin in the list
"""


def makeChange(coins, total):
    """
    return fewest number of coins
    needed to meet the total
    """
    if total <= 0:
        return 0

    num_of_denoms = len(coins)
    sorted_denoms = sorted(coins)
    change_denoms = []

    i = num_of_denoms - 1
    while(i >= 0):
        while(total >= sorted_denoms[i]):
            total = total - sorted_denoms[i]
            change_denoms.append(sorted_denoms[i])
        i = i - 1

    if total == 0:
        return len(change_denoms)
    return -1
