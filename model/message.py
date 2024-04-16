from enum import Enum
from utils import Validador


class _Role(Enum):
    MODEL = 'model'
    USER = 'user'


class Message:
    PARTS_MODEL = """
        Você é um especialista desenvolvedor muito experiente com conhecimento em diferentes
        assuntos e conceitos teóricos e práticos sobre {topic}.
        Você está trabalhando em um processo de contratação e seu trabalho agora é escrever perguntas
        para uma entrevista. Cada pergunta deve ter quatro respostas possíveis e uma delas
        deve ser correta. Escreva essas perguntas no seguinte formato:
        {{'statement': 'question', 'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],'correct': 'Option 3'}}
    """

    def __init__(self, topic):
        self.__topic = Validador(topic).nao_nulo().nao_vazio().tamanho_minimo(4).valor

    @property
    def message(self):
        return [
            {
                'role': _Role.MODEL.name,
                'parts': self.PARTS_MODEL.format(topic=self.__topic)
            },
            {
                'role': _Role.USER.name,
                'parts': f'Gere uma questão sobre {self.__topic}'
            }
        ]
