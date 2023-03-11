from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def obter_extensao_arquivo(path):
        string_nome_arquivo = path.split(".")
        if len(string_nome_arquivo) == 1:
            return []
        else:
            return string_nome_arquivo[-1]

    @staticmethod
    def import_data(path):
        dados_do_arquivo = []
        formato_arquivo = CsvImporter.obter_extensao_arquivo(path)

        if formato_arquivo == "csv":
            with open(path) as file:
                dados_do_arquivo = [dict for dict in csv.DictReader(file)]
                return dados_do_arquivo
        else:
            raise ValueError("Arquivo inválido")
