import unittest
from primes import isPrime, find_next_prime, find_previous_prime

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

    """Test find_next_prime function"""

    def test_find_next_prime_2(self):
        """Find next prime after 2"""
        next_prime_2 = find_next_prime(2)
        self.assertEqual(next_prime_2, 2)

    def test_find_next_prime_3(self):
        """Find next prime after 3"""
        next_prime_3 = find_next_prime(3)
        self.assertEqual(next_prime_3, 3)

    def test_find_next_prime_5(self):
        """Find next prime after 5"""
        next_prime_5 = find_next_prime(5)
        self.assertEqual(next_prime_5, 5)

    def test_find_next_prime_7(self):
        """Find next prime after 7"""
        next_prime_7 = find_next_prime(7)
        self.assertEqual(next_prime_7, 7)

    def test_find_next_prime_12(self):
        """Find next prime after 12"""
        next_prime_12 = find_next_prime(12)
        self.assertEqual(next_prime_12, 13)

    def test_find_next_prime_15(self):
        """Find next prime after 15"""
        next_prime_15 = find_next_prime(15)
        self.assertEqual(next_prime_15, 17)

    def test_find_next_prime_18(self):
        """Find next prime after 18"""
        next_prime_18 = find_next_prime(18)
        self.assertEqual(next_prime_18, 19)

    def test_find_next_prime_22(self):
        """Find next prime after 22"""
        next_prime_22 = find_next_prime(22)
        self.assertEqual(next_prime_22, 23)

    def test_find_next_prime_24(self):
        """Find next prime after 24"""
        next_prime_24 = find_next_prime(24)
        self.assertEqual(next_prime_24, 29)

    def test_find_next_prime_25(self):
        """Find next prime after 25"""
        next_prime_25 = find_next_prime(25)
        self.assertEqual(next_prime_25, 29)

    def test_find_next_prime_26(self):
        """Find next prime after 26"""
        next_prime_26 = find_next_prime(26)
        self.assertEqual(next_prime_26, 29)

    def test_find_next_prime_27(self):
        """Find next prime after 27"""
        next_prime_27 = find_next_prime(27)
        self.assertEqual(next_prime_27, 29)

    def test_find_next_prime_28(self):
        """Find next prime after 28"""
        next_prime_28 = find_next_prime(28)
        self.assertEqual(next_prime_28, 29)

    def test_find_next_prime_29(self):
        """Find next prime after 29"""
        next_prime_29 = find_next_prime(29)
        self.assertEqual(next_prime_29, 29)

    def test_find_next_prime_24(self):
        """Find next prime after 24"""
        next_prime_24 = find_next_prime(24)
        self.assertNotEqual(next_prime_24, 24)

    def test_find_next_prime_24(self):
        """Find next prime after 24"""
        next_prime_24 = find_next_prime(24)
        self.assertNotEqual(next_prime_24, 25)

    def test_find_next_prime_24(self):
        """Find next prime after 24"""
        next_prime_24 = find_next_prime(24)
        self.assertNotEqual(next_prime_24, 26)

    def test_find_next_prime_24(self):
        """Find next prime after 24"""
        next_prime_24 = find_next_prime(24)
        self.assertNotEqual(next_prime_24, 27)

    def test_find_next_prime_24(self):
        """Find next prime after 24"""
        next_prime_24 = find_next_prime(24)
        self.assertNotEqual(next_prime_24, 28)

    def test_find_next_prime_25(self):
        """Find next prime after 25"""
        next_prime_25 = find_next_prime(25)
        self.assertNotEqual(next_prime_25, 25)

    def test_find_next_prime_26(self):
        """Find next prime after 26"""
        next_prime_26 = find_next_prime(26)
        self.assertNotEqual(next_prime_26, 26)

    def test_find_next_prime_27(self):
        """Find next prime after 27"""
        next_prime_27 = find_next_prime(27)
        self.assertNotEqual(next_prime_27, 27)

    def test_find_next_prime_28(self):
        """Find next prime after 28"""
        next_prime_28 = find_next_prime(28)
        self.assertNotEqual(next_prime_28, 28)

    """Test find_previous_prime function"""

    def test_find_previous_prime_(self):
        """Find previous prime before 2"""
        previous_prime_2 = find_previous_prime(2)
        self.assertEqual(previous_prime_2, 2)

    def test_find_previous_prime_3(self):
        """Find previous prime before 3"""
        previous_prime_3 = find_previous_prime(3)
        self.assertEqual(previous_prime_3, 3)
        
    def test_find_previous_prime_4(self):
        """Find previous prime before 4"""
        previous_prime_4 = find_previous_prime(4)
        self.assertEqual(previous_prime_4, 3)

    def test_find_previous_prime_5(self):
        """Find previous prime before 5"""
        previous_prime_5 = find_previous_prime(5)
        self.assertEqual(previous_prime_5, 5)

    def test_find_previous_prime_6(self):
        """Find previous prime before 6"""
        previous_prime_6 = find_previous_prime(6)
        self.assertEqual(previous_prime_6, 5)

    def test_find_previous_prime_7(self):
        """Find previous prime before 7"""
        previous_prime_7 = find_previous_prime(7)
        self.assertEqual(previous_prime_7, 7)

    def test_find_previous_prime_8(self):
        """Find previous prime before 8"""
        previous_prime_8 = find_previous_prime(8)
        self.assertEqual(previous_prime_8, 7)

    def test_find_previous_prime_9(self):
        """8 is not the previous prime before 9"""
        previous_prime_9 = find_previous_prime(9)
        self.assertNotEqual(previous_prime_9, 8)

    def test_find_previous_prime_10(self):
        """10 is not the previous prime before 10"""
        previous_prime_10 = find_previous_prime(10)
        self.assertNotEqual(previous_prime_10, 10)

    def test_find_previous_prime_12(self):
        """12 is not the previous prime before 12"""
        previous_prime_12 = find_previous_prime(12)
        self.assertNotEqual(previous_prime_12, 12)

    def test_find_previous_prime_15(self):
        """14 is not the previous prime before 15"""
        previous_prime_15 = find_previous_prime(15)
        self.assertNotEqual(previous_prime_15, 14)

    def test_find_previous_prime_16(self):
        """14 is not the previous prime before 16"""
        previous_prime_16 = find_previous_prime(16)
        self.assertNotEqual(previous_prime_16, 14)


if __name__ == '__main__':
    unittest.main()
