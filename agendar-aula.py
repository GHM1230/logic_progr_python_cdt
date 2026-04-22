while True:
    acesso_menu = input("O que precisa fazer? (1 = Agendar aula | 0 = Sair): ")

    if acesso_menu == '1':
        print("Agendando aula...")

        nome_aluno = input("Digite o nome do aluno: ")
        turma_aluno = input("Digite a turma do aluno: ")
        email_aluno = input("Digite o e-mail do aluno: ")

        print("\nAula agendada com sucesso!")
        print(f"Aluno: {nome_aluno}")
        print(f"Turma: {turma_aluno}")
        print(f"E-mail: {email_aluno}")

    elif acesso_menu == '0':
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.\n")
    