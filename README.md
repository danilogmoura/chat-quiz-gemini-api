# Chat Quiz Gemini API

Este projeto é uma aplicação de quiz interativo alimentado por um modelo de IA generativa. O usuário pode escolher um tópico e o programa irá gerar perguntas relacionadas a esse tópico. Cada pergunta vem com quatro opções de resposta, e o usuário deve escolher a correta.

## Requisitos

- Python 3.12.3
- Docker (opcional)

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt` e incluem:

- rich
- openai
- google-generativeai

## Configuração

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Configure a chave da API do Google Generative AI no arquivo `quiz.py`.

## Execução

Para executar o programa, use o comando `python quiz.py`.

## Docker

Um `Dockerfile` está incluído para a construção de uma imagem Docker do projeto. Para construir a imagem, use o comando `docker build -t chat-quiz-gemini-api .`. Para executar o programa em um contêiner Docker, use o comando `docker run -p 8000:8000 chat-quiz-gemini-api`.
