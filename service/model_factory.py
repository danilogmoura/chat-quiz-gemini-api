import importlib
import configparser
from overrides import overrides
from service import GenerativeModelFactor
from utils import Validator


class ModelFactory(GenerativeModelFactor):
    __GENERATIVE_MODEL_SECTION = 'generative.model'

    @overrides
    def new_model(self):
        config = configparser.ConfigParser()
        config.read('resources/config.properties')

        model = self.__config_validator(config, 'generative.model.module')
        class_name = self.__config_validator(config, 'generative.model.class_name')
        model_name = self.__config_validator(config, 'generative.model.name')
        api_key = self.__config_validator(config, 'generative.model.name.api_key')

        generative_model = importlib.import_module(model)
        generative_model_instance = getattr(generative_model, class_name)

        return generative_model_instance(model_name, api_key)

    def __config_validator(self, config, attribute):
        value = config.get(self.__GENERATIVE_MODEL_SECTION, attribute)
        return Validator(value, attribute).not_empty().not_null().minimum_size(3).value
