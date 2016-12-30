#! /usr/bin/env python

# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#     13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz(n, lengths):
    length = 1
    sequence = [n]

    while n != 1:

        if n in lengths:
            length += lengths[n] - 1
            break

        if n % 2 == 0:
            n /= 2

        else:
            n = (3 * n) + 1

        sequence.append(n)
        length += 1

    for i, number in enumerate(sequence):
        if number in lengths:
            break

        else:
            lengths[number] = length - i

    return length


def longest_collatz(n):
    lengths = {}

    length_of_longest = 0
    longest = 0

    for x in range(1, n):

        collatz_len = collatz(x, lengths)

        if collatz_len > length_of_longest:
            length_of_longest = collatz_len
            longest = x

    return longest


print longest_collatz(1000000)
