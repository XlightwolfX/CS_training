# File: main.py
# Auth: David Cerny
# Date: 26/07/2021
##################################################
""" See if presented integer is a deletable prime and check
the number of possibilities to reduce it into a single-digit prime"""

import math
import argparse
from copy import deepcopy


def is_prime(n):
    if n % 2 == 0 or n <= 1:
        return False
    if n == 2:
        return True

    sqrt_n = int(math.sqrt(n)) + 1

    for div in range(3, sqrt_n, 2):
        if n % div == 0:
            return False
    return True


def reduce_prime(prime_digits):
    decomposed_primes = []

    for idx, digit in enumerate(prime_digits):
        new_num = prime_digits.copy()
        new_num.pop(idx)
        if is_prime(int(''.join(new_num))):
            decomposed_primes.append(new_num)
    return decomposed_primes


def count_primes_in_deletable_prime(n):
    assert is_prime(n), "Input not a prime!"

    prime_digits = list(str(n))
    prime_buffer = []
    prime_new_buffer = []
    prime_buffer.append(prime_digits)

    # are all primes single digit?
    while not all(len(x) == 1 for x in prime_buffer):
        for number in prime_buffer:
            new_primes = reduce_prime(number)
            if not new_primes:
                continue
            prime_new_buffer.extend(new_primes)

        prime_buffer = deepcopy(prime_new_buffer)
        prime_new_buffer.clear()

    return len(prime_buffer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, required=True)
    args = parser.parse_args()

    # do stuff
    num_of_reductions = count_primes_in_deletable_prime(args.n)

    print(f"number of reductions: {num_of_reductions}")

