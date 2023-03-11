from inventory_report.inventory.product import Product


def test_cria_produto():
    # Testa se é possível criar um produto com os dados corretos
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
    assert produto.id == id
    assert produto.nome_do_produto == nome_do_produto
    assert produto.nome_da_empresa == nome_da_empresa
    assert produto.data_de_fabricacao == str(data_de_fabricacao)
    assert produto.data_de_validade == str(data_de_validade)
    assert produto.numero_de_serie == numero_de_serie
    assert produto.instrucoes_de_armazenamento == instrucoes_de_armazenamento
