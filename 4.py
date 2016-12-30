#! /usr/bin/env python

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome():
    largest = 0

    for x in range(999, 100, -1):
        for y in range(x, 100, -1):

            product = x * y
            if str(product) == str(product)[::-1]:
                largest = max(largest, x * y)

    return largest


print largest_palindrome()
