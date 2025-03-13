# Password Generator

O **Password Generator** é um projeto em Python para gerar senhas seguras. Ele permite que você defina o comprimento da senha e escolha se deseja incluir números e caracteres especiais.

## Funcionalidades

- Geração de senhas com comprimento customizável.
- Opção de incluir números na senha.
- Opção de incluir caracteres especiais.
- Testes automatizados para garantir a funcionalidade.

## Como Usar

### Rodando o Gerador de Senhas

1. Clone o repositório:

   bash
   git clone https://github.com/laibras/password-generator.git
   cd password-generator

2. Execute o gerador de senhas:

    bash
    python src/generator.py
    O programa pedirá para você inserir o comprimento da senha e se deseja incluir números e caracteres especiais.

## Rodando os Testes

O projeto utiliza o framework de testes unittest. Para rodar os testes, execute o seguinte comando:

    bash
    python -m unittest discover tests

## Estrutura do Projeto

    password-generator/
    │── src/
    │   ├── __init__.py
    │   ├── generator.py  # Lógica de geração de senhas
    │── tests/
    │   ├── __init__.py
    │   ├── test_generator.py  # Testes automatizados para o gerador de senhas
    │── requirements.txt  (opcional)  # Dependências do projeto (se houver)
    │── README.md  (opcional)  # Este arquivo

## Licença

    Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contribuindo
    
    Se você gostaria de contribuir para este projeto, por favor, abra uma issue ou envie um pull request com suas sugestões ou melhorias.







