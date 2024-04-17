from overrides import overrides
from model import Message


class GeminiMessage(Message):

    def __init__(self, topic):
        super().__init__(topic)

    @property
    @overrides
    def content(self):
        pass
