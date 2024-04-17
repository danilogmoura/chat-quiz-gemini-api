from abc import ABC, abstractmethod


class AbstractGenerativeModel(ABC):

    def __init__(self, model_name, api_key):
        self.__model_name = model_name
        self.__api_key = api_key  # Validar key

    @property
    def model_name(self):
        return self.__model_name

    @property
    def api_key(self):
        return self.__api_key

    @abstractmethod
    def to_dictionary(self, raw_message):
        pass

    @abstractmethod
    def message(self, topic):
        pass

    @abstractmethod
    def generate_question(self, topic):
        pass
