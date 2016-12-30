#! /usr/bin/env python

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def get_divisors(n):
    divisors = []
    for x in range(n + 1):
        divisors.append([])

    for num in range(1, (n / 2) + 1):

        multiple = num + num

        while multiple < len(divisors):
            divisors[multiple].append(num)
            multiple += num

    return divisors


def amicable_pairs(n):
    complements = {}
    divisors = get_divisors(n)

    amicable_sum = 0
    for num in range(n):
        div_sum = sum(divisors[num])

        if num in complements and complements[num] == div_sum:
            amicable_sum += num + div_sum

        else:
            complements[div_sum] = num

    return amicable_sum


print amicable_pairs(10000)
