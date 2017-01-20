#! /usr/bin/env python

# In England the currency is made up of pound, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, 1 pound (100p) and 2 pounds (200p).
#
# It is possible to make 2 pound in the following way:
#
# 1x1 pound + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
# How many different ways can 2 pounds be made using any number of coins?


def ways_make_change(n, denominations):
    ways = [1] + ([0] * n)

    for denom in denominations:
        for coins in range(1, n + 1):
            if coins - denom >= 0:
                ways[coins] += ways[coins - denom]

    return ways[-1]


print ways_make_change(200, [1, 2, 5, 10, 20, 50, 100, 200])
