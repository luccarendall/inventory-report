import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json


class Inventory:
    def obtem_dados_arquivo(file, formato_do_arquivo):
        if formato_do_arquivo == "csv":
            tabela_dados = csv.DictReader(file)
            dados_do_arquivo = [linha for linha in tabela_dados]
            return dados_do_arquivo
        if formato_do_arquivo == "json":
            return json.load(file)

    def obter_extensao_arquivo(caminho_arquivo):
        partes = caminho_arquivo.split(".")
        if len(partes) == 1:
            return []
        else:
            return partes[-1]

    @staticmethod
    def import_data(path, tipo_do_relatorio):
        formato_arquivo = Inventory.obter_extensao_arquivo(path)
        with open(path, encoding="utf-8") as file:
            inventorio = Inventory.obtem_dados_arquivo(file, formato_arquivo)

        if tipo_do_relatorio == "simples":
            return SimpleReport.generate(inventorio)

        if tipo_do_relatorio == "completo":
            return CompleteReport.generate(inventorio)
