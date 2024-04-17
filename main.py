from service import QuestionGenerator
from service import GeminiModelFactory
from rich.console import Console
from rich.prompt import Prompt

console = Console()
generative_model = GeminiModelFactory().new_model()


def wait_for_enter():
    console.input(
        prompt="Pressione ENTER para continar...",
        password=True
    )


def generate_question(topic):
    return QuestionGenerator(generative_model).ask(topic)


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

    title = "[bold yellow]Quiz GEMINI[/bold yellow]"
    console.print(f"Bem vindo ao {title}")

    run_quiz()


main()
