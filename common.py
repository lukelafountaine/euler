import itertools


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
