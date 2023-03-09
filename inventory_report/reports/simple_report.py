from collections import Counter
from datetime import date


class SimpleReport:
    def __init__(list):
        pass

    # Buscar data de fabricação mais antiga: YYYY-MM-DD
    def get_produto_mais_antigo(list):
        datas_de_fabricacao = [
            # https://acervolima.com/funcao-fromisoformat-da-classe-datetime-date-em-python/
            date.fromisoformat(product["data_de_fabricacao"])
            for product in list
            # datas_de_fabricacao retorna todas as datas de fabricação.
            # Precisamos usar o método data para ela vir em formato de data
            # (YYYY-MM-DD) e não em string, para daí fazermos as comparações
        ]

        fabricacao_mais_antiga = min(datas_de_fabricacao)

        return fabricacao_mais_antiga

    # Buscar data de validade mais próxima: YYYY-MM-DD
    def get_validade_mais_proxima(list):
        # https://acervolima.com/obtenha-a-data-atual-usando-python/
        data_atual = date.today()

        datas_de_validade = [
            date.fromisoformat(product["data_de_validade"])
            for product in list
            # Assim como datas_de_fabricacao, datas_de_validade retorna
            # todas as datas de validade dos produtos. E precisamos usar o
            # método data para ela vir em formato de data (YYYY-MM-DD)
        ]

        data_de_vencimento = [
            date for date in datas_de_validade if date >= data_atual
            # data_de_vencimento verifica se cada data iterada em
            # datas_de_validade é maior ou igual a data atual.
            # Assim verificamos se o produto está dentro da validade
        ]

        validade_mais_proxima_do_vencimento = min(data_de_vencimento)
        # por fim verificamos qual data, dentre as que sobraram é
        # a mais próxima do vencimento e retornamos ela

        return validade_mais_proxima_do_vencimento

    # Buscar empresa com mais produtos: NOME DA EMPRESA
    def get_maior_empresa(list):
        # na verdade era get_empresa_com_mais_produtos mas o lint
        # reclamou do tamanho na linha 60
        contador = Counter(
            product["nome_da_empresa"] for product in list
        )
        # https://blog.csdn.net/Silentli20/article/details/121518963
        return contador.most_common()[0][0]

    @staticmethod
    def generate(list):
        produto_mais_antigo = SimpleReport.get_produto_mais_antigo(list)
        validade_mais_proxima = SimpleReport.get_validade_mais_proxima(list)
        empresa_com_mais_produtos = SimpleReport.get_maior_empresa(list)

        return (
            f"Data de fabricação mais antiga: {produto_mais_antigo}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produtos}"
        )
