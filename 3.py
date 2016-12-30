#! /usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(n):
    x = 2

    while True:

        while n % x == 0:
            n /= x

        if x + 1 > n:
            return x

        x += 1

    return x


print largest_prime_factor(600851475143)
