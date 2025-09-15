from alunos import alunos

while True:  
    print("\n=== MENU ALUNOS ===")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Exibir todos os alunos")
    print("5 - Exibir média dos alunos")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
       
        nome = input("Digite o nome do aluno: ")
        notas = []
        for i in range(4):  
            n = float(input(f"Digite a nota {i+1}: "))
            notas.append(n)
        alunos[nome] = notas
        print("Aluno adicionado com sucesso!")

    elif opcao == "2":
    
        nome = input("Digite o nome do aluno para atualizar: ")
        if nome in alunos:
            notas = []
            for i in range(4): 
                n = float(input(f"Digite a nova nota {i+1}: "))
                notas.append(n)
            alunos[nome] = notas
            print("Notas atualizadas!")
        else:
            print("Aluno não encontrado!")

    elif opcao == "3":
    
        nome = input("Digite o nome do aluno para remover: ")
        if nome in alunos:
            del alunos[nome]
            print("Aluno removido!")
        else:
            print("Aluno não encontrado!")

    elif opcao == "4":
      
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado!")
        else:
            for nome, notas in alunos.items():
                print("Aluno:", nome, "- Notas:", notas)

    elif opcao == "5":
        
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado!")
        else:
            for nome, notas in alunos.items():
                media = sum(notas) / len(notas)
                print("Aluno:", nome, "- Média:", media)

    elif opcao == "6":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")