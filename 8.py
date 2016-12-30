#! /usr/bin/env python

# The four adjacent digits in the 1000-digit number that have the greatest product are 9 * 9 * 8 * 9 = 5832.
#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?


def largest_product(series, n):
    series_without_zero = series.split('0')

    for i, x in enumerate(series_without_zero):
        series_without_zero[i] = map(int, x)

    max_prod = 0

    for series in series_without_zero:
        if len(series) < n:
            continue

        product = 1
        for x in range(n):
            product *= series[x]

        max_prod = max(max_prod, product)

        for x in range(n, len(series)):
            product /= series[x - n]
            product *= series[x]

        max_prod = max(max_prod, product)

    return max_prod


with open('8.txt') as f:
    series = f.read()

print largest_product(series, 4)
