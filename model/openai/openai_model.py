from model import AbstractGenerativeModel
from overrides import overrides


class OpenAIModel(AbstractGenerativeModel):

    def __init__(self, model_name, api_key):
        super().__init__(model_name, api_key)

    @overrides
    def to_dictionary(self, raw_message):
        pass

    @overrides
    def message(self, topic):
        pass

    @overrides
    def generate_question(self, topic):
        pass
