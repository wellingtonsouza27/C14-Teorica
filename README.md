# Password Validator - CI/CD Pipeline

## Descrição

Este projeto foi desenvolvido para a disciplina de Engenharia de Software com o objetivo de implementar um pipeline completo de CI/CD utilizando GitHub Actions.

O sistema consiste em um módulo em Python capaz de validar senhas, gerar senhas seguras e avaliar sua força, aplicando boas práticas de desenvolvimento, testes automatizados e integração contínua.

---

## Funcionalidades

* Validação de senha com regras de segurança
* Geração de senha aleatória segura
* Avaliação da força da senha (fraca, média, forte)
* Testes automatizados utilizando pytest
* Pipeline CI/CD com GitHub Actions

---

## Tecnologias Utilizadas

* **Python 3.11** → linguagem principal do projeto
* **pytest** → framework de testes automatizados
* **pip** → gerenciamento de dependências
* **flake8** → ferramenta de lint (qualidade de código)
* **GitHub Actions** → automação de CI/CD
* **Git** → controle de versão

---

## Regras de validação

Uma senha válida deve atender aos seguintes critérios:

* Possuir no mínimo 8 caracteres
* Conter pelo menos uma letra maiúscula
* Conter pelo menos uma letra minúscula
* Conter pelo menos um número
* Conter pelo menos um caractere especial
* Não conter espaços

---

## Testes Automatizados

O projeto contém mais de 20 cenários de teste, incluindo:

* Casos válidos (fluxo principal)
* Casos inválidos (fluxo de erro)
* Testes da avaliação de força da senha
* Testes da geração de senha

---

## Gerenciamento de Dependências

O projeto utiliza o gerenciador de pacotes padrão do Python, o **pip**, juntamente com o arquivo `requirements.txt`, que lista todas as dependências necessárias para execução do sistema.

### Arquivo requirements.txt

O arquivo `requirements.txt` contém as bibliotecas utilizadas no projeto, por exemplo:

```txt
pytest
pytest-cov
flake8
```
As dependências listadas são instaladas automaticamente durante a execução do pipeline CI/CD, garantindo que o ambiente esteja corretamente configurado antes da execução dos testes.

---

## Como executar os testes localmente

```bash
git clone https://github.com/wellingtonsouza27/C14-Teorica.git
cd C14-Teorica
pip install -r requirements.txt
py -m pytest
```

---

## Pipeline CI/CD

O pipeline foi implementado utilizando GitHub Actions e contém os seguintes jobs:

### Jobs

* **test** → executa todos os testes automatizados
* **lint** → verifica a qualidade do código com flake8
* **build** → gera um pacote do projeto (.zip)
* **deploy** → realiza o deploy via GitHub Releases
* **notify** → executa uma notificação ao final do pipeline

---

## Estrutura do Projeto

```
src/
  validator.py
  generator.py
  strength.py

tests/
  test_validator.py
  test_generator.py
  test_strength.py

.github/workflows/
  ci.yml

requirements.txt
README.md
```

---

## Variáveis de Ambiente

O projeto utiliza secrets do GitHub Actions:

* EMAIL → utilizado na etapa de notificação do pipeline

---

## Notificação

A etapa de notificação do pipeline utiliza uma variável de ambiente para simular o envio de notificação ao final da execução.

A mensagem é exibida no log do GitHub Actions, indicando o término do pipeline.

---

## Uso de Inteligência Artificial

Durante o desenvolvimento deste projeto, foi utilizada inteligência artificial como ferramenta de apoio.

### Prompts utilizados

* como criar um pipeline CI/CD com GitHub Actions com testes, build, deploy e notificação
* como configurar secrets no GitHub Actions
* como organizar um projeto Python com testes automatizados

### Avaliação do uso de IA

O uso da inteligência artificial foi considerado:

* Positivo para acelerar o desenvolvimento
* Útil para estruturação do código
* Importante na criação do pipeline CI/CD

Porém:

* Algumas soluções precisaram ser ajustadas manualmente
* Foi necessário interpretar e corrigir erros sugeridos

---

## Integrantes

* Wellington Henrique Dias de Souza
* Otavio da Silva Barbosa
