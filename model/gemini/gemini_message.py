from model import Message
from overrides import overrides


class GeminiMessage(Message):

    def __init__(self, topic):
        super().__init__(topic)

    @property
    @overrides
    def content(self):
        return [
            {
                'role': 'model',
                'parts': self.PARTS_MODEL.format(topic=self.topic)
            },
            {
                'role': 'user',
                'parts': f'Gere uma questão sobre {self.topic}'
            }
        ]
