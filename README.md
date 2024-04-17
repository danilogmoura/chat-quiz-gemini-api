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
3. Configure a chave da API do Google Generative AI no resourses\config.properties

    #### resources/config.properties

    O arquivo `resources/config.properties` é um arquivo de configuração usado pelo projeto. Ele contém várias propriedades que são usadas para configurar o modelo generativo usado pelo aplicativo de quiz.

    Aqui estão as propriedades definidas no arquivo:

   - `generative.model.module`: Este é o módulo Python que contém a classe do modelo generativo. No caso do seu projeto, o módulo é `model.gemini.gemini_model`.
   - `generative.model.class_name`: Este é o nome da classe do modelo generativo dentro do módulo especificado. No seu projeto, a classe é `GeminiModel`.
   - `generative.model.name`: Este é o nome do modelo generativo a ser usado. No seu projeto, o modelo é `models/gemini-1.5-pro-latest`.
   - `generative.model.name.api_key`: Esta é a chave da API usada para acessar o modelo generativo. No seu projeto, a chave da API deve ser fornecida aqui.

    Para usar o arquivo `resources/config.properties`, você deve preencher a propriedade `generative.model.name.api_key` com a chave da API apropriada. As outras propriedades já estão preenchidas para você.

## Execução

Para executar o programa, use o comando `python main.py`.

## Docker

Um `Dockerfile` está incluído para a construção de uma imagem Docker do projeto. Para construir a imagem, use o comando `docker build -t chat-quiz-gemini-api .`. Para executar o programa em um contêiner Docker, use o comando `docker run -p 8000:8000 chat-quiz-gemini-api`.
