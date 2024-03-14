#!/usr/bin/python3
"""
Prime Game
    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
"""


def isWinner(x, nums):
    """
    returns the winner at the end of the rounds
    """
    mariaWins = 0
    benWins = 0

    for num in nums:
        primeCount = countPrimes(num)
        if primeCount % 2 == 0:
            benWins += 1
        else:
            mariaWins += 1

    if mariaWins > benWins:
        return "Maria"
    elif mariaWins < benWins:
        return "Ben"
    else:
        return None


def countPrimes(number):
    """
    counts the prime number for a player
    """
    count = 0
    for i in range(2, number + 1):
        if isPrimeNumber(i):
            count += 1
    return count


def isPrimeNumber(number):
    """
    checks the number if prime returns True
    else returns False
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
