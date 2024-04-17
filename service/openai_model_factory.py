from service import GenerativeModelFactor
from overrides import overrides


class OpenAIModelFactory(GenerativeModelFactor):

    @overrides
    def new_model(self):
        pass
