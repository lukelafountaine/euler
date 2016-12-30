#! /usr/bin/env python

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pythagorean(num_sum):
    for a in range(1, num_sum):

        for b in range(a + 1, num_sum):

            c = num_sum - a - b

            if (a ** 2) + (b ** 2) == (c ** 2):
                return a * b * c


print pythagorean(1000)
