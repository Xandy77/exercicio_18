# Tupla com as chaves para os dicionários de usuários
chaves = ('Nome', 'Data de Nascimento', 'CPF', 'Profissão', 'E-mail', 'Endereço', 'Telefone')

# Lista de dicionários, cada um representando um usuário
usuarios = [
    {
        chaves[0]: 'Ellen Silva',
        chaves[1]: '22/03/1982',
        chaves[2]: '585.624.798-51',
        chaves[3]: 'Fisiculturista',
        chaves[4]: 'ellen.silva@gmail.com',
        chaves[5]: 'QNO 02 - G - 33',
        chaves[6]: '(61) 99232-1212'
    },
    {
        chaves[0]: 'Rosangela Santos',
        chaves[1]: '17/11/1972',
        chaves[2]: '951.753.852-64',
        chaves[3]: 'Recepcionista',
        chaves[4]: 'Rosapink@gmail.com',
        chaves[5]: 'QNO 13 - J - 17',
        chaves[6]: '(61) 99204-6551'
    },
    {
        chaves[0]: 'Vera Lucia',
        chaves[1]: '24/07/1979',
        chaves[2]: '753.159.654-82',
        chaves[3]: 'Faxineira',
        chaves[4]: 'vera.lucia@gmail.com',
        chaves[5]: 'QNM 23 - D - 01',
        chaves[6]: '(61) 98456-6604'
    }
]

while True:
    # Exibe o menu de opções
    print("Escolha uma opção:")
    print("1. Cadastrar usuário")
    print("2. Listar todos os usuários")
    print("3. Alterar dados do usuário")
    print("4. Excluir usuário")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        # Cadastrar usuário
        print("Cadastro de Usuário")
        usuario = {}
        for chave in chaves:
            valor = input(f"Digite {chave}: ")
            usuario[chave] = valor
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!\n")

    elif opcao == "2":
        # Listar todos os usuários
        if not usuarios:
            print("Nenhum usuário cadastrado.\n")
        else:
            print("Lista de Usuários:")
            for i, usuario in enumerate(usuarios):
                print(f"\nUsuário {i+1}:")
                for chave in chaves:
                    print(f"{chave}: {usuario[chave]}")
            print()

    elif opcao == "3":
        # Alterar dados do usuário
        nome_procurado = input("Qual nome do usuário você deseja alterar?: ")
        encontrado = False

        for usuario in usuarios:
            if nome_procurado.lower() in usuario[chaves[0]].lower():
                encontrado = True
                print("\nUsuário encontrado. Digite os novos dados (deixe em branco para manter o valor atual):")
                for chave in chaves:
                    novo_valor = input(f"{chave} (atual: {usuario[chave]}): ")
                    if novo_valor:
                        usuario[chave] = novo_valor
                print("Dados do usuário atualizados com sucesso!\n")
                break

        if not encontrado:
            print("Nenhum usuário encontrado com o nome informado.\n")

    elif opcao == "4":
        # Excluir usuário
        nome_procurado = input("Qual nome do usuário você deseja excluir?: ")
        usuarios_anteriores = len(usuarios)
        usuarios = [usuario for usuario in usuarios if nome_procurado.lower() not in usuario[chaves[0]].lower()]

        if len(usuarios) < usuarios_anteriores:
            print("Usuário excluído com sucesso!\n")
        else:
            print("Nenhum usuário encontrado com o nome informado.\n")

    elif opcao == "5":
        # Sair do programa
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")
