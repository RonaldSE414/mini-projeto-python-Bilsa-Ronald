alunos = {}
nomes_cadastrados = set()

def cadastrar_aluno():
    print('\n--- Cadastro de Aluno ---')
    matricula = input('Digite a matrícula do aluno: ')

    if matricula in alunos:
        print('Matrícula já cadastrada')
        return

    nome = input('Digite o nome do aluno: ')
    if nome in nomes_cadastrados:
        print('Nome já cadastrado')
        return

    alunos[matricula] = (nome, ())
    nomes_cadastrados.add(nome)
    print(f'Aluno {nome} cadastrado com sucesso!')

def registrar_notas():
    print('\n--- Registro de Notas ---')
    matricula = input('Digite a matrícula do aluno: ')

    if matricula not in alunos:
        print('Aluno não encontrado')
        return

    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f'Digite a nota {i}: '))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print('A nota deve estar entre 0 e 10')
            except ValueError:
                print('Digite um valor válido')

    nome = alunos[matricula][0]
    alunos[matricula] = (nome, tuple(notas))
    print(f'Notas registradas para {nome}')

def listar_alunos_medias():
    print('\n--- Lista de Alunos e Médias ---')
    if not alunos:
        print('Nenhum aluno cadastrado')
        return

    for matricula, (nome, notas) in alunos.items():
        if notas:
            media = sum(notas) / len(notas)
            print(f'{nome} (Matrícula {matricula}) - Média: {media:.2f}')
        else:
            print(f'{nome} (Matrícula {matricula}) - Sem notas registradas')

def buscar_aluno():
    print('\n--- Buscar Aluno ---')
    matricula = input('Digite a matrícula do aluno: ')

    if matricula in alunos:
        nome, notas = alunos[matricula]
        print(f"Nome: {nome}")
        if notas:
            print(f"Notas: {notas} | Média: {sum(notas)/len(notas):.2f}")
        else:
            print("Sem notas registradas.")
    else:
        print(" Aluno não encontrado.")

def mostrar_aprovados_reprovados():
    print("\n--- Aprovados e Reprovados ---")
    for matricula, (nome, notas) in alunos.items():
        if notas:
            media = sum(notas) / len(notas)
            status = "Aprovado " if media >= 7 else "Reprovado "
            print(f"{nome} - Média: {media:.2f} - {status}")
        else:
            print(f"{nome} - Sem notas registradas.")

def relatorios():
    print("\n--- Relatórios ---")
    print("1 - Alunos cadastrados")
    print("2 - Médias individuais")
    print("3 - Aprovados e Reprovados")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nAlunos cadastrados:")
        for matricula, (nome, _) in alunos.items():
            print(f"{matricula} - {nome}")
    elif opcao == "2":
        listar_alunos_medias()
    elif opcao == "3":
        mostrar_aprovados_reprovados()
    else:
        print(" Opção inválida!")

# ----------- MENU PRINCIPAL -----------
while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar aluno")
    print("2 - Registrar notas")
    print("3 - Listar alunos e médias")
    print("4 - Buscar aluno")
    print("5 - Mostrar aprovados e reprovados")
    print("6 - Relatórios")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        registrar_notas()
    elif opcao == "3":
        listar_alunos_medias()
    elif opcao == "4":
        buscar_aluno()
    elif opcao == "5":
        mostrar_aprovados_reprovados()
    elif opcao == "6":
        relatorios()
    elif opcao == "0":
        print("Encerrando o sistema... ")
        break
    else:
        print(" Opção inválida! Tente novamente.")
