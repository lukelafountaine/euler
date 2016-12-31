#! /usr/bin/env python

# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from common import incremental_sieve


def is_circular(prime, primes):
    prime = str(prime)

    for x in range(len(prime) - 1):
        prime = prime[1:] + prime[0]

        if int(prime) not in primes:
            return False

    return True


prime_set = set()
for i, prime in enumerate(incremental_sieve()):

    if i == 1000000:
        break

    prime_set.add(prime)

count = 0
for prime in prime_set:
    if is_circular(prime, prime_set):
        count += 1

print count
