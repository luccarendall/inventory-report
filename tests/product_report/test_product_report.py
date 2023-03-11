from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "Arroz"
    nome_da_empresa = "Marca X"
    data_de_fabricacao = "01/01/2022"
    data_de_validade = "01/01/2024"
    numero_de_serie = "12345"
    instrucoes_de_armazenamento = "em local seco e arejado"

    produto = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert repr(produto) == (
           f"O produto {nome_do_produto} fabricado em {data_de_fabricacao} "
           f"por {nome_da_empresa} com validade até {data_de_validade} "
           f"precisa ser armazenado {instrucoes_de_armazenamento}."
           )
