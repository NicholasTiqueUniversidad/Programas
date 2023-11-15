import unittest

def es_divisible_por_5_y_11(numero):
    if numero % 5 == 0 and numero % 11 == 0:
        return "El número es divisible por 5 y 11."
    else:
        return "El número no es divisible por 5 y 11."

class TestDivisiblePor5Y11(unittest.TestCase):

    def test_divisible(self):
        self.assertEqual(es_divisible_por_5_y_11(55), "El número es divisible por 5 y 11.")

    def test_no_divisible(self):
        self.assertEqual(es_divisible_por_5_y_11(39), "El número no es divisible por 5 y 11.")

if __name__ == '__main__':
    unittest.main()
