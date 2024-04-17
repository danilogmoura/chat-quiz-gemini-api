from model import Message
from overrides import overrides


class GeminiMessage(Message):

    def __init__(self, topic):
        super().__init__(topic)

    @property
    @overrides
    def content(self):
        pass
