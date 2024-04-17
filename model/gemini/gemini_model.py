import json
import sys
import re
import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument

from overrides import overrides
from model import AbstractGenerativeModel
from .gemini_message import GeminiMessage


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
        cleaned_message = re.sub(r'\s+', ' ', raw_message)
        match = re.search(self.__PATTERN, cleaned_message)
        if match:
            dicionario_texto = match.group("dictionary")
            return json.loads(dicionario_texto)

        raise ValueError("Não foi possível extrair um dicionário da mensagem fornecida")

    @overrides
    def message(self, topic):
        return GeminiMessage(topic)

    @overrides
    def generate_question(self, topic):
        try:
            raw_message = self.__model.generate_content(self.message(topic).content).text
            return self.to_dictionary(raw_message)
        except InvalidArgument as e:
            print(e.args[0])
            sys.exit()
