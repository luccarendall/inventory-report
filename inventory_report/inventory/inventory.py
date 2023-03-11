import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import xml.etree.ElementTree as ElementTree


class Inventory:
    def obtem_dados_arquivo(file, formato_do_arquivo):
        if formato_do_arquivo == "csv":
            tabela_dados = csv.DictReader(file)
            dados_do_arquivo = [linha for linha in tabela_dados]
            return dados_do_arquivo
        elif formato_do_arquivo == "json":
            return json.load(file)
        elif formato_do_arquivo == "xml":
            # Esse método funcionou mas deu excesso de complexidade \/
            # arquivo = file.read()
            # dados_do_arquivo = ElementTree.fromstring(arquivo)
            # lista_dados = []
            # for info in dados_do_arquivo:
            #     dados = {}
            #     for item in info:
            #         dados[item.tag] = item.text
            #     lista_dados.append(dados)
            dados_do_arquivo = ElementTree.parse(file).getroot()
            lista_dados = [{item.tag: item.text for item in info}
                           for info in dados_do_arquivo]
            return lista_dados
        else:
            return "Aceitamos apenas arquivos csv, json e xml. "\
                   "Tente novamente usando um arquivo em formato válido."

    def obter_extensao_arquivo(path):
        string_nome_arquivo = path.split(".")
        if len(string_nome_arquivo) == 1:
            return []
        else:
            return string_nome_arquivo[-1]

    @staticmethod
    def import_data(path, tipo_do_relatorio):
        formato_arquivo = Inventory.obter_extensao_arquivo(path)
        with open(path, encoding="utf-8") as file:
            inventorio = Inventory.obtem_dados_arquivo(file, formato_arquivo)

        if tipo_do_relatorio == "simples":
            return SimpleReport.generate(inventorio)

        if tipo_do_relatorio == "completo":
            return CompleteReport.generate(inventorio)
