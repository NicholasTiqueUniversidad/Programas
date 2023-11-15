import unittest

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

class TestParImpar(unittest.TestCase):

    def test_par(self):
        self.assertEqual(es_par_o_impar(8), "El número es par.")

    def test_impar(self):
        self.assertEqual(es_par_o_impar(7), "El número es impar.")

if __name__ == '__main__':
    unittest.main()
