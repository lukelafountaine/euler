#! /usr/bin/env python

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.


def sum_square_difference(n):
    sum_of_squares = 0
    sums = 0

    for x in range(1, n + 1):
        sum_of_squares += x ** 2
        sums += x

    return (sums ** 2) - sum_of_squares


print sum_square_difference(100)
