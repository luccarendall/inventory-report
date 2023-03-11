from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ElementTree


class XmlImporter(Importer):
    def obter_extensao_arquivo(path):
        string_nome_arquivo = path.split(".")
        if len(string_nome_arquivo) == 1:
            return []
        else:
            return string_nome_arquivo[-1]

    @staticmethod
    def import_data(path):
        dados_do_arquivo = []
        formato_arquivo = XmlImporter.obter_extensao_arquivo(path)

        if formato_arquivo == "xml":
            with open(path) as file:
                dados_do_arquivo = ElementTree.parse(file).getroot()
                lista_dados = [{item.tag: item.text for item in info}
                               for info in dados_do_arquivo]
            return lista_dados
        else:
            raise ValueError("Arquivo inválido")
