# UTF-8 Validation

This project is about implementing a method to determine if a given dataset represents a valid UTF-8 encoding. It involves understanding UTF-8 encoding rules, bitwise operations, and logical reasoning.

## Learning Objectives

By the end of this project, you should be able to:
- Understand what a caching system is and its purpose.
- Explain the FIFO, LIFO, LRU, MRU, and LFU caching algorithms.
- Manipulate bits in Python using bitwise operations.
- Work with data at the byte level.
- Apply logical operations to make decisions within the program.
- Handle the least significant bits (LSB) of integers to simulate byte data.
- Iterate through lists, access list elements, and understand list comprehensions.

## Requirements

- Python 3.7
- PEP 8 style (version 1.7.x)

## Structure

- `base_caching.py`: Base class for caching systems.
- `0-basic_cache.py`: Basic caching system implementation.
- `1-fifo_cache.py`: FIFO caching system implementation.
- `2-lifo_cache.py`: LIFO caching system implementation.
- `3-lru_cache.py`: LRU caching system implementation.
- `4-mru_cache.py`: MRU caching system implementation.
- `100-lfu_cache.py`: LFU caching system implementation.
- `0-validate_utf8.py`: Method to validate UTF-8 encoding.

## Usage

Each caching class can be tested with the provided main scripts (e.g., `0-main.py` for BasicCache).

## Example

To check if a dataset represents a valid UTF-8 encoding:

```python
#!/usr/bin/python3
""" Main file for testing """

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
