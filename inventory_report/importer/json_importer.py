from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        dados_do_arquivo = []
        formato_arquivo = Importer.obter_extensao_arquivo(path)

        if formato_arquivo == "json":
            with open(path) as file:
                dados_do_arquivo = json.load(file)
                return dados_do_arquivo
        else:
            raise ValueError("Arquivo inválido")
