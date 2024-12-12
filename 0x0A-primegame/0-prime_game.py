#!/usr/bin/python3
"""
This module contains the function isWinner which determines the winner of the
Prime Game.
"""


def isWinner(x, nums):
    """
    Determine the winner of each game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing each round.

    Returns:
        str: Name of the player that won the most rounds.
    """
    def sieve(n):
        """ Helper function to generate list of primes up to n """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    if x < 1 or not nums:
        return None

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        if n < 2:
            wins["Ben"] += 1
            continue

        primes = sieve(n)
        rounds = [0] * (n + 1)
        for prime in primes:
            for multiple in range(prime, n + 1, prime):
                rounds[multiple] = 1

        if sum(rounds) % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
