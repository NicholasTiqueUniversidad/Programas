import unittest

def encontrar_maximo(num1, num2, num3):
    maximo = max(num1, num2, num3)
    return f"El máximo es: {maximo}"

class TestEncontrarMaximo(unittest.TestCase):

    def test_maximo(self):
        self.assertEqual(encontrar_maximo(10, 20, 15), "El máximo es: 20")

    def test_maximo_negativo(self):
        self.assertEqual(encontrar_maximo(-5, -10, -3), "El máximo es: -3")

if __name__ == '__main__':
    unittest.main()
