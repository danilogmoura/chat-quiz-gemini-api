from model import AbstractGenerativeModel


class QuestionGenerator:
    def __init__(self, generative_model: AbstractGenerativeModel):
        self.__generative_model = generative_model

    def ask(self, topic):
        return self.__generative_model.generate_question(topic)
