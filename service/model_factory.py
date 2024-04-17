from service import GenerativeModelFactor
from overrides import overrides
import importlib
import configparser


class ModelFactory(GenerativeModelFactor):
    __GENERATIVE_MODEL_SECTION = 'generative.model'

    @overrides
    def new_model(self):
        config = configparser.ConfigParser()

        config.read('resources/config.properties')

        model = config.get(self.__GENERATIVE_MODEL_SECTION, 'generative.model.module')
        class_name = config.get(self.__GENERATIVE_MODEL_SECTION, 'generative.model.class_name')
        model_name = config.get(self.__GENERATIVE_MODEL_SECTION, 'generative.model.name')
        api_key = config.get(self.__GENERATIVE_MODEL_SECTION, 'generative.model.name.api_key')

        if not all([model, class_name, model_name, api_key]):
            raise ValueError("Propriedades do arquivo 'config.properties' inválidas")

        generative_model = importlib.import_module(model)
        generative_model_instance = getattr(generative_model, class_name)

        return generative_model_instance(model_name, api_key)
