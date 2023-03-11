import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def obtem_dados_do_arquivo(file):
        tabela_de_dados = csv.DictReader(file)
        dados_obtidos = [linha for linha in tabela_de_dados]
        return dados_obtidos

    @staticmethod
    def import_data(path, tipo_do_relatorio):
        with open(path, encoding="utf-8") as file:
            inventorio = Inventory.obtem_dados_do_arquivo(file)

        if tipo_do_relatorio == "simples":
            return SimpleReport.generate(inventorio)

        if tipo_do_relatorio == "completo":
            return CompleteReport.generate(inventorio)
