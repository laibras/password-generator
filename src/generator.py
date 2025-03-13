import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """
    Gera uma senha aleatória.
    
    :param length: Comprimento da senha (padrão: 12)
    :param use_digits: Incluir números (padrão: True)
    :param use_special_chars: Incluir caracteres especiais (padrão: True)
    :return: Senha gerada como string
    """
    characters = string.ascii_letters  # Letras maiúsculas e minúsculas
    
    if use_digits:
        characters += string.digits  # Adiciona números
    if use_special_chars:
        characters += string.punctuation  # Adiciona caracteres especiais
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Gerador de Senhas Seguras 🔑")
    length = int(input("Digite o comprimento da senha: "))
    use_digits = input("Incluir números? (s/n): ").strip().lower() == 's'
    use_special_chars = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

    senha = generate_password(length, use_digits, use_special_chars)
    print(f"Senha gerada: {senha}")