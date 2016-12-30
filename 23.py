#! /usr/bin/env python

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers.
#
# However, this upper limit cannot be reduced any further by analysis even though it is known
# that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def get_divisors(n):
    divisors = []
    for x in range(n + 1):
        divisors.append([])

    for num in range(1, (n / 2) + 1):

        multiple = num + num

        while multiple < len(divisors):
            divisors[multiple].append(num)
            multiple += num

    return divisors


def get_abundants(n, divisors):
    abundants = []

    for x in range(n):
        if sum(divisors[x]) > x:
            abundants.append(x)

    return abundants


def non_abundant():
    upper_limit = 28123
    divisors = get_divisors(upper_limit)
    abundants = get_abundants(upper_limit, divisors)
    can_sum = set()

    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            can_sum.add(abundants[i] + abundants[j])

    total = 0
    for x in range(upper_limit):
        if x not in can_sum:
            total += x

    return total


print non_abundant()
