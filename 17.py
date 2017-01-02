#! /usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
# there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


def number_to_word(n):
    if n > 1000:
        return -1

    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    hundred = 'hundred'
    thousand = 'onethousand'

    number = ''
    place_val = 1
    while n > 0:
        val = n % 10
        n /= 10

        if val == 0:
            place_val *= 10
            continue

        if place_val == 1:

            if n % 10 == 1:
                n /= 10
                place_val *= 10
                number = '{}'.format(teens[val - 1])

            else:
                number = '{}{}'.format(ones[val - 1], number).strip()

        elif place_val == 10:
            number = '{}{}'.format(tens[val - 1], number).strip()

        elif place_val == 100:

            if len(number) > 0:
                number = '{}{}{}{}'.format(ones[val - 1], hundred, 'and', number).strip()

            else:
                number = '{}{}{}'.format(ones[val - 1], hundred, number).strip()

        elif place_val == 1000:
            number = '{}{}'.format(thousand, number).strip()

        place_val *= 10

    return number


length = 0
for x in range(1, 1001):
    length += len(number_to_word(x).strip())

print length
