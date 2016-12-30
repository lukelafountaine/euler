#! /usr/bin/env python

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial


def digit_factorials(x):
    sum = 0
    while x > 0:
        digit = x % 10
        sum += factorial(digit)
        x /= 10

    return sum


total = 0
for x in range(3, 1000000):
    if x == digit_factorials(x):
        total += x

print total
