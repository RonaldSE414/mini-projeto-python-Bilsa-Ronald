categorias = ("Alimentos", "Limpeza", "Bebidas")
produtos = []
codigos = set()

def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")
    codigo = input("Digite o código do produto: ")
    if not codigo.isdigit():
        print("Código inválido! Use apenas números.")
        return
    codigo = int(codigo)
    if codigo in codigos:
        print("Código já cadastrado!")
        return

    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    if not preco.replace('.', '', 1).isdigit():
        print("Preço inválido!")
        return
    preco = float(preco)

    quantidade = input("Digite a quantidade: ")
    if not quantidade.isdigit():
        print("Quantidade inválida!")
        return
    quantidade = int(quantidade)

    print("Categorias disponíveis:")
    for i, cat in enumerate(categorias):
        print(f"{i + 1} - {cat}")
    escolha = input("Escolha a categoria (número): ")
    if not escolha.isdigit() or not (1 <= int(escolha) <= len(categorias)):
        print("Categoria inválida!")
        return
    categoria = categorias[int(escolha) - 1]

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "categoria": categoria
    }

    produtos.append(produto)
    codigos.add(codigo)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for p in produtos:
            print(f"Código: {p['codigo']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Qtd: {p['quantidade']} | Categoria: {p['categoria']}")

def buscar_produto():
    print("\n--- Buscar Produto ---")
    codigo = input("Digite o código do produto: ")
    if not codigo.isdigit():
        print("Código inválido!")
        return
    codigo = int(codigo)
    for p in produtos:
        if p["codigo"] == codigo:
            print(f"Produto encontrado: {p}")
            return
    print("Produto não encontrado.")

def atualizar_produto():
    print("\n--- Atualizar Produto ---")
    codigo = input("Digite o código do produto: ")
    if not codigo.isdigit():
        print("Código inválido!")
        return
    codigo = int(codigo)

    for p in produtos:
        if p["codigo"] == codigo:
            print(f"Produto atual: {p}")
            novo_nome = input("Novo nome (enter para manter): ")
            if novo_nome:
                p["nome"] = novo_nome

            novo_preco = input("Novo preço (enter para manter): ")
            if novo_preco:
                if not novo_preco.replace('.', '', 1).isdigit():
                    print("Preço inválido!")
                else:
                    p["preco"] = float(novo_preco)

            nova_qtd = input("Nova quantidade (enter para manter): ")
            if nova_qtd:
                if not nova_qtd.isdigit():
                    print("Quantidade inválida!")
                else:
                    p["quantidade"] = int(nova_qtd)

            print("Produto atualizado!")
            return
    print("Produto não encontrado.")

def excluir_produto():
    print("\n--- Excluir Produto ---")
    codigo = input("Digite o código do produto: ")
    if not codigo.isdigit():
        print("Código inválido!")
        return
    codigo = int(codigo)

    for p in produtos:
        if p["codigo"] == codigo:
            produtos.remove(p)
            codigos.remove(codigo)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        buscar_produto()
    elif opcao == "4":
        atualizar_produto()
    elif opcao == "5":
        excluir_produto()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
