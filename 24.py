#! /usr/bin/env python

# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.

# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def permutations(n):
    counts = [1] * (n + 1)

    for i in range(n + 1):
        counts[i] -= 1

        for perm in helper([i], counts):
            yield perm

        counts[i] += 1


def helper(permutation, counts):
    if sum(counts) == 0:
        yield ''.join(map(str, permutation))
        return

    for i in range(len(counts)):

        if counts[i] != 0:
            counts[i] -= 1
            permutation.append(i)

            for perm in helper(permutation, counts):
                yield perm

            counts[i] += 1
            permutation.pop()


perms = permutations(9)
for x in range(999999):
    perms.next()

print perms.next()
