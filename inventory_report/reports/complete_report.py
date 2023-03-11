# Colocar caminho inteiro(com pontos). Se não o teste não encontra...
from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def get_produtos_por_empresa(list):
        contador = Counter(
            product["nome_da_empresa"] for product in list
        )

        lista_de_empresas = []
        for empresa, quatidade in contador.items():
            lista_de_empresas += f"- {empresa}: {quatidade}\n"
        return lista_de_empresas

    # https://www.programiz.com/python-programming/methods/built-in/classmethod
    @classmethod
    def generate(self, list):
        # Chama a função generate na versão dela que está na classe pai
        SimpleReport = super().generate(list)
        produtos_por_empresa = CompleteReport.get_produtos_por_empresa(list)
        return (
            f"{SimpleReport}\n"
            f"Empresa com mais produtos: {produtos_por_empresa}"
        )
