from model import AbstractGenerativeModel
from .gemini_message import GeminiMessage
import google.generativeai as genai
from overrides import overrides
import re


class GeminiModel(AbstractGenerativeModel):
    __PATTERN = r"```json\s*(?P<dictionary>{.*})\s*```"

    def __init__(self, model_name, api_key):
        super().__init__(model_name, api_key)
        self.__configure()

    def __configure(self):
        genai.configure(api_key=self.api_key)
        self.__model = genai.GenerativeModel(self.model_name)

    @overrides
    def to_dictionary(self, raw_message):
        match = re.search(self.__PATTERN, raw_message)
        if match:
            dicionario_texto = match.group("dictionary")
            return eval(dicionario_texto)
        else:
            raise ValueError("Não foi possível extrair um dicionário da mensagem fornecida")

    @overrides
    def message(self, topic):
        return GeminiMessage(topic)

    @overrides
    def generate_question(self, topic):
        raw_message = self.__model.generate_content(self.message(topic).content).text
        return self.to_dictionary(raw_message)
