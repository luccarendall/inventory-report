from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(path):
        pass

    @classmethod
    def obter_extensao_arquivo(self, path):
        string_nome_arquivo = path.split(".")
        if len(string_nome_arquivo) == 1:
            return []
        else:
            return string_nome_arquivo[-1]
