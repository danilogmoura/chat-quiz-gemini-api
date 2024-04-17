from abc import ABC, abstractmethod


class GenerativeModelFactor(ABC):
    GENERATIVE_MODEL_SECTION = 'generative.model'

    @abstractmethod
    def new_model(self):
        pass
