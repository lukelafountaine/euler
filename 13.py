#! /usr/bin/env python

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

with open('13.txt') as f:
    nums = f.readlines()

    sum = 0
    for num in nums:
        sum += int(num)

    print str(sum)[:10]
