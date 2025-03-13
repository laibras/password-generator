import unittest
from src.generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        """Testa se a senha gerada tem o comprimento padrão de 12 caracteres"""
        senha = generate_password()
        self.assertEqual(len(senha), 12)

    def test_custom_length(self):
        """Testa se a senha gerada tem um comprimento específico"""
        senha = generate_password(20)
        self.assertEqual(len(senha), 20)

    def test_contains_digits(self):
        """Testa se a senha contém pelo menos um número quando a opção está ativada"""
        senha = generate_password(12, use_digits=True, use_special_chars=False)
        self.assertTrue(any(c.isdigit() for c in senha))

    def test_contains_special_chars(self):
        """Testa se a senha contém pelo menos um caractere especial quando a opção está ativada"""
        senha = generate_password(12, use_digits=False, use_special_chars=True)
        special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
        self.assertTrue(any(c in special_chars for c in senha))

if __name__ == "__main__":
    unittest.main()
