
#Sistema de Gestão Estoque
estoque = { #dicionário onde a chave é o nome do produto, pois achei mais fácil de desenvolver por esse modelo.
    "Blusas": {
        "Quantidade": 10,
        "ValorOriginal": 20,
        "ValorFinal":20
    },
    "Bermudas": {
        "Quantidade": 5,
        "ValorOriginal": 40,
        "ValorFinal":40
    },
    "Calças": {
        "Quantidade": 8,
        "ValorOriginal": 60,
        "ValorFinal":60
    }
}
while True:

    print("----- CONTROLE DE ESTOQUE -----")
    print("1 - Ver estoque")
    print("2 - Entrada de produtos")
    print("3 - Saída de produtos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # VER ESTOQUE
    if opcao == "1":
        status = ""  # Reseta o status a cada visualização
        print("\nESTOQUE ATUAL:\n")

        for produto, dados in estoque.items():#FOR para percorrer todo o dicionário
            quantidade = dados["Quantidade"]#Adicionei um if para automatizar uma promoção quando o estoque estiver alto
            if quantidade > 50:
                dados["ValorFinal"] = dados["ValorOriginal"] * 90 / 100
                status = "Produto em promoção: "

            elif quantidade < 20:
                dados["ValorFinal"] = dados["ValorOriginal"]
                status = ""
               
            else:
                dados["ValorFinal"] = dados["ValorFinal"]
                status = status
                # Mantém o status anterior
            
            print(status + produto)
            print(f"Quantidade: {quantidade}")
            print(f"Valor: R${dados['ValorFinal']:.2f}\n")

    # ENTRADA DE PRODUTOS
    elif opcao == "2":

        produto = input("Digite o nome do produto: ").capitalize()

        if produto in estoque:

            try:
                quantidade = int(input("Digite a quantidade de entrada: "))
                estoque[produto]["Quantidade"] += quantidade
                print("Estoque atualizado com sucesso!\n")

            except ValueError:
                print("Digite apenas números inteiros\n")

        else:
            print("Produto inexistente\n")

    # SAÍDA DE PRODUTOS
    elif opcao == "3":

        produto = input("Digite o nome do produto: ").capitalize()

        if produto in estoque:

            try:
                quantidade = int(input("Digite a quantidade de saída: "))

                if estoque[produto]["Quantidade"] >= quantidade:

                    estoque[produto]["Quantidade"] -= quantidade
                    print("Saída realizada com sucesso!\n")

                else:
                    print("Estoque insuficiente\n")

            except ValueError:
                print("Digite apenas números inteiros\n")

        else:
            print("Produto não encontrado\n")

    # SAIR
    elif opcao == "4":

        print("Sistema encerrado")
        break

    # BLOCO DE VALIDAÇÃO
    else:
        print("Opção inválida\n")
