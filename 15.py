#! /usr/bin/env python

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?


def unique_paths(m, n):
    return helper(m, n, {})


def helper(m, n, cache):
    if m == 0 or n == 0:
        return 1

    if (m, n) in cache:
        return cache[(m, n)]

    cache[(m, n)] = helper(m - 1, n, cache) + helper(m, n - 1, cache)
    return cache[(m, n)]


print unique_paths(20, 20)
