from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        dados_do_arquivo = []
        formato_arquivo = Importer.obter_extensao_arquivo(path)

        if formato_arquivo == "csv":
            with open(path) as file:
                dados_do_arquivo = [dict for dict in csv.DictReader(file)]
                return dados_do_arquivo
        else:
            raise ValueError("Arquivo inválido")
