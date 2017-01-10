#! /usr/bin/env python

# Euler discovered the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
# However, when n = 40, 40^2 + 40 + 41 = 40 (40 + 1) + 41 is divisible by 41, and certainly when n = 41,
#
# 41^2 + 41 + 41
#
# is clearly divisible by 41.
#
# The incredible formula n^2 - 79n + 1601
# was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
#
# The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
# n^2 + an + b,
# where |a| < 1000 and |b| <= 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

import random


def is_prime(n):
    if n <= 0:
        return False

    prime = True

    # fermat's little theorem
    for _ in range(5):
        a = random.randint(1, n)
        if (a ** n) % n != (a % n):
            prime = False

    return prime


def num_of_primes(a, b):
    n = 0

    while is_prime((n ** 2) + (a * n) + b):
        n += 1

    return n

most = 0
coeffs = (0, 0)
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        primes = num_of_primes(a, b)

        if primes > most:
            most = primes
            coeffs = (a, b)

print most, coeffs
