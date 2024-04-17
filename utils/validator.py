class Validator:
    def __init__(self, value, attribute):
        self.__value = value
        self.__attribute = attribute
        self.__errors = []

    @property
    def value(self):
        if self.__errors:
            raise ValueError(self.__errors)
        return self.__value

    def not_null(self):
        if not self.__value:
            self.__errors.append(f'"{self.__attribute}" não pode ser nulo')
        return self

    def not_empty(self):
        if not self.__value:
            return self

        if not self.__value.strip():
            self.__errors.append(f'"{self.__attribute}" não pode ser vazio')
        return self

    def minimum_size(self, value):
        if self.__value is None:
            return self

        if len(self.__value) < value:
            self.__errors.append(f'"{self.__attribute}" deve possuir no mínimo "{value}" '
                                 f'caracteres')
        return self
