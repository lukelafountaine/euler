#! /usr/bin/env python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def prime_factors(n, factors):
    x = 2

    while True:

        count = 0
        while n % x == 0:
            n /= x
            count += 1

        factors[x] = max(count, factors[x])

        if x + 1 > n:
            break

        x += 1

    return factors


def smallest_multiple(n):
    factors = [0] * (n + 1)

    for num in range(2, n + 1):
        factors = prime_factors(num, factors)

    product = 1
    for i, exponent in enumerate(factors):
        product *= (i ** exponent)

    return product


print smallest_multiple(20)
