import itertools
import random

def incremental_sieve():
    composites = {}

    yield 2

    for x in itertools.count(3, 2):
        if x not in composites:
            yield x

            composites[x * x] = [x]

        else:
            for prime in composites[x]:

                next = x + prime
                while next % 2 == 0:
                    next += prime

                composites.setdefault(next, []).append(prime)

            del composites[x]


def is_prime(n):
    if n < 2:
        return False

    prime = True

    # fermat's little theorem
    for _ in range(5):
        a = random.randint(1, n)
        if (a ** n) % n != (a % n):
            prime = False
            break

    return prime
