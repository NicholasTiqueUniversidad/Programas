import unittest

def es_triangulo_valido(angulo1, angulo2, angulo3):
    if angulo1 + angulo2 + angulo3 == 180:
        return "Los ángulos forman un triángulo válido."
    else:
        return "Los ángulos no forman un triángulo válido."

class TestTrianguloValido(unittest.TestCase):

    def test_triangulo_valido(self):
        self.assertEqual(es_triangulo_valido(60, 60, 60), "Los ángulos forman un triángulo válido.")

    def test_triangulo_no_valido(self):
        self.assertEqual(es_triangulo_valido(90, 45, 47), "Los ángulos no forman un triángulo válido.")

if __name__ == '__main__':
    unittest.main()
