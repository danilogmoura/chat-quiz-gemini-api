from service import GenerativeModelFactor
from overrides import overrides
import importlib
import configparser


class GeminiModelFactory(GenerativeModelFactor):
    __GENERATIVE_MODEL_SECTION = 'generative.model'

    @overrides
    def new_model(self):
        config = configparser.ConfigParser()

        config.read('resources/config.properties')

        model = config.get(self.__GENERATIVE_MODEL_SECTION, 'generative.model.module')
        class_name = config.get(self.__GENERATIVE_MODEL_SECTION, 'generative.model.class_name')
        model_name = config.get(self.__GENERATIVE_MODEL_SECTION, 'generative.model.name')
        api_key = config.get(self.__GENERATIVE_MODEL_SECTION, 'generative.model.name.api_key')

        generative_model = importlib.import_module(model)
        gemini_model = getattr(generative_model, class_name)

        return gemini_model(model_name, api_key)
