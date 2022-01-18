import unittest
from primes import isPrime

class IsPrimeTestCase(unittest.TestCase):
    """Test for isPrime function"""

    def test_isPrime_2(self):
        """Is 2 a prime number"""
        is_2_prime = isPrime(2)
        self.assertTrue(is_2_prime
                )
    def test_isPrime_5(self):
        """Is 5 a prime number"""
        is_5_prime = isPrime(5)
        self.assertTrue(is_5_prime)

    def test_isPrime_7(self):
        """Is 7 a prime number"""
        is_7_prime = isPrime(7)
        self.assertTrue(is_7_prime)

    def test_isPrime_13(self):
        """Is 13 a prime number"""
        is_13_prime = isPrime(13)
        self.assertTrue(is_13_prime)

    def test_isPrime_19(self):
        """Is 19 a prime number"""
        is_19_prime = isPrime(19)
        self.assertTrue(is_19_prime)

    def test_isPrime_4(self):
        """Is 4 a prime number"""
        is_4_prime = isPrime(4)
        self.assertFalse(is_4_prime)

    def test_isPrime_10(self):
        """Is 10 a prime number"""
        is_10_prime = isPrime(10)
        self.assertFalse(is_10_prime)

    def test_isPrime_27(self):
        """Is 27 a prime number"""
        is_27_prime = isPrime(27)
        self.assertFalse(is_27_prime)

    def test_isPrime_39(self):
        """Is 39 a prime number"""
        is_39_prime = isPrime(39)
        self.assertFalse(is_39_prime)

    def test_isPrime_81(self):
        """Is 81 a prime number"""
        is_81_prime = isPrime(81)
        self.assertFalse(is_81_prime)

if __name__ == '__main__':
    unittest.main()
