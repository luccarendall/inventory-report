from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def obter_extensao_arquivo(path):
        string_nome_arquivo = path.split(".")
        if len(string_nome_arquivo) == 1:
            return []
        else:
            return string_nome_arquivo[-1]

    @staticmethod
    def import_data(path):
        dados_do_arquivo = []
        formato_arquivo = JsonImporter.obter_extensao_arquivo(path)

        if formato_arquivo == "json":
            with open(path) as file:
                dados_do_arquivo = json.load(file)
                return dados_do_arquivo
        else:
            raise ValueError("Arquivo inválido")
