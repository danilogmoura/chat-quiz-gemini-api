from overrides import overrides
from model import AbstractGenerativeModel


class OpenAIModel(AbstractGenerativeModel):

    @overrides
    def to_dictionary(self, raw_message):
        pass

    @overrides
    def message(self, topic):
        pass

    @overrides
    def generate_question(self, topic):
        pass
