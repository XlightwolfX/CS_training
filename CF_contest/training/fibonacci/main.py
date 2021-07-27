# File: main.py
# Auth: David Cerny
# Date: 26/07/2021
##################################################

""" Find the nth number in the Fibonacci sequence """

import argparse


def calculate_fib_number(n):
    assert n >= 0, "n must be non-negative!"

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # init seq
        second_last = 0
        last = 1
        current = 0

        for i in range(2, n + 1):

            # calc ith number
            current = second_last + last

            # update previous numbers
            second_last = last
            last = current

        return current


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, required=True)
    args = parser.parse_args()

    fib_num = calculate_fib_number(args.n)

    print(f"{args.n}. fibonacci number is {fib_num}")
