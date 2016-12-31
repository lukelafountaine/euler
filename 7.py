#! /usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from common import incremental_sieve


def nth_prime(n):
    sieve = incremental_sieve()

    for x in range(n):
        prime = sieve.next()

    return prime


print nth_prime(10001)
