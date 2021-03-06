#!/bin/bash

"""
This module works with prime numbers.
"""

from math import sqrt

def isPrime(number):
    """Returns true if `number` is a prime number.

    :param number: int - number to check.
    :return: boolean - is `number` prime?
    """

    midpoint = int(round(sqrt(number)))

    for value_to_check in range(2, midpoint + 1):
        if number % value_to_check == 0:
            return False

    return True


def find_next_prime(number):
    """Given a `number` the function returns the next prime number

    :param number: int - find next prime after `number`.
    :return: int - next prime number after `number`.
    """

    if isPrime(number):
        return number

    return find_next_prime(number + 1)


def find_previous_prime(number):
    """Given a `number` the function returns the previous prime number

    :param number: int - find previous prime before `number`.
    :return: int - previous prime number before `number`.
    """

    if isPrime(number):
        return number

    return find_previous_prime(number - 1)


def primes_list(start_number, end_number):
    """

    :param start_number: int - begin search for prime numbers at `start_number`

    :param end_number: int - end search for prime numbers at and including `end_number`.
    :return: list - returns a list of prime numbers found between `start_number` and `end_number`.
    """

    prime_numbers = []

    for number in range(start_number, end_number + 1):
        if isPrime(number):
            prime_numbers.append(number)

    return prime_numbers

