tarefas = []
while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Marcar tarefa como concluída")
    print("3 - Listar tarefas")
    print("4 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Título da tarefa: ")
        descricao = input("Descrição: ")
        tarefa = {"titulo": titulo, "descricao": descricao, "status": "Pendente"}
        tarefas.append(tarefa)
        print("Tarefa adicionada.")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, t in enumerate(tarefas):
                print(i, "-", t["titulo"], "-", t["status"])
            idx = int(input("Digite o número da tarefa concluída: "))
            if 0 <= idx < len(tarefas):
                tarefas[idx]["status"] = "Concluído"
                print("Tarefa atualizada.")
            else:
                print("Número inválido.")

    elif opcao == "3":
        print("\nTarefas Pendentes:")
        for t in tarefas:
            if t["status"] == "Pendente":
                print(t["titulo"], "-", t["descricao"])
        print("\nTarefas Concluídas:")
        for t in tarefas:
            if t["status"] == "Concluído":
                print(t["titulo"], "-", t["descricao"])

    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")