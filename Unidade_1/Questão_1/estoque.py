estoque = {} 

while True:  
    print("\n=== MENU ESTOQUE ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir produtos")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        
        nome = input("Digite o nome do produto: ")
        qtd = int(input("Digite a quantidade: "))
        estoque[nome] = qtd  
        print("Produto adicionado com sucesso!")

    elif opcao == "2":
        
        nome = input("Digite o nome do produto para remover: ")
        if nome in estoque:
            del estoque[nome] 
            print("Produto removido!")
        else:
            print("Produto não encontrado!")

    elif opcao == "3":
        
        nome = input("Digite o nome do produto: ")
        if nome in estoque:
            qtd = int(input("Digite a nova quantidade: "))
            estoque[nome] = qtd  
            print("Quantidade atualizada!")
        else:
            print("Produto não encontrado!")

    elif opcao == "4":
        
        if len(estoque) == 0:
            print("Estoque vazio!")
        else:
            print("\n=== Produtos no estoque ===")
            for nome, qtd in estoque.items():
                print("Produto:", nome, "- Quantidade:", qtd)

    elif opcao == "5":
        
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente de novo.")