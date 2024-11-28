# 0x08. Making Change

## Description

This project focuses on developing a solution to determine the fewest number of coins needed to meet a given total amount from a pile of coins of different values.

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the PEP 8 style (version 1.7.x).
- All your files must be executable.

## Files

- `0-making_change.py`: Contains the function `makeChange(coins, total)` that determines the fewest number of coins needed to meet a given total amount.
- `0-main.py`: The main file for testing the `makeChange` function.

## Function Prototype

### `makeChange`

```python
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
