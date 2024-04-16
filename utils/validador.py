class Validador:
    def __init__(self, valor):
        self.__valor = valor
        self.__erros = []

    @property
    def valor(self):
        if self.__erros:
            raise ValueError(self.__erros)
        return self.__valor

    def nao_nulo(self):
        if not self.__valor:
            self.__erros.append('Tópico não pode ser nulo')
        return self

    def nao_vazio(self):
        if not self.__valor:
            return self

        if not self.__valor.strip():
            self.__erros.append('Tópico não pode ser vazio')
        return self

    def tamanho_minimo(self, minimo):
        if self.__valor is None:
            return self

        if len(self.__valor) < minimo:
            self.__erros.append('Tópico deve possuir no mínimo {minimo} caracteres')
        return self
