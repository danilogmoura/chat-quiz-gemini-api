from rich.console import Console
from rich.prompt import Prompt
import json
import google.generativeai as genai
import re

console = Console()
genai.configure(api_key="")

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")


def wait_for_enter():
    console.input(
        prompt="Pressione ENTER para continar...",
        password=True
    )


def generate_question(topic):
    message = [
        {
            'role': 'model',
            'parts': f"""
            Você é um especialista desenvolvedor muito experiente com conhecimento em diferentes
            assuntos e conceitos teóricos e práticos sobre {topic}.
            Você está trabalhando em um processo de contratação e seu trabalho agora é escrever perguntas
            para uma entrevista. Cada pergunta deve ter quatro respostas possíveis e uma delas
            deve ser correta. Escreva essas perguntas no seguinte formato:
            {{'statement': 'question', 'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'], 'correct': 'Option 3'}}
        """
        },
        {
            'role': 'user',
            'parts': f'Gere uma questão sobre {topic}'
        }
    ]
    pattern = r'{[^}]+}'
    raw_response = model.generate_content(message).text
    matched_response = re.findall(pattern, raw_response)

    return json.loads(matched_response[0].replace("'", "\""))


def run_quiz():
    score = 0
    continue_quiz = ""

    topico = Prompt.ask("Qual é o tópico do quiz?")

    while continue_quiz.lower() != "n":
        with console.status("Processando", spinner="dots"):
            question = generate_question(topico)

        options = question["options"]
        console.clear()
        console.print(f"[bold]{question["statement"]}")

        for i, option in enumerate(options, start=1):
            console.print(f"{i}) {option}")

        answer_index = int(
            Prompt.ask(
                prompt="Opção",
                choices=["1", "2", "3", "4"])
        ) - 1

        user_answer = options[answer_index]
        correct_answer = question["correct"]

        if user_answer == correct_answer:
            score += 1
            console.print(f"[green]Você acertou! Agora você tem {score} pontos")
        else:
            console.print(f"[red]Você errou! Você continua {score} pontos")
            console.print(f"A resposta certa é [yellow]{user_answer}")

        continue_quiz = Prompt.ask(
            prompt="Desejesa continuar? ",
            choices=["S", "n"],
            default="S"
        )


def main():
    console.clear()

    title = "[bold yellow]Quiz GPT[/bold yellow]"
    console.print(f"Bem vindo ao {title}")

    run_quiz()


main()
