from SistemaAcademico import SistemaAcademico

def main():
    sistema = SistemaAcademico()

    while True:

        print("\n" + "="*30)
        print("   SISTEMA DE GESTÃO ACADÊMICA")
        print("="*30)
        print("1. Cadastrar Aluno")
        print("2. Listar Todos os Alunos")
        print("3. Buscar Aluno por Matrícula")
        print("4. Registrar Nota")
        print("5. Consultar Boletim Individual")
        print("6. Emitir Relatório Geral")
        print("7. Sair")
        
        opcao = input("\nEscolha uma opção (1-7): ")

        if opcao == "1":
            print("\n--- CADASTRO DE ALUNO ---")
            nome = input("Nome do aluno: ")
            curso = input("Curso: ")
            matricula = sistema.cadastrar_aluno(nome, curso)
            if matricula != None:
                print(f"Sucesso! Aluno cadastrado com a matrícula gerada: [{matricula}]")

        elif opcao == "2":
            print("\n--- LISTA DE ALUNOS ---")
            if len(sistema._alunos) == 0:
                print("Nenhum aluno cadastrado.")
            else:
                for mat, aluno in sistema._alunos.items():
                    print(f"Matrícula: {mat} | Nome: {aluno._nome} | Curso: {aluno._curso}")

        elif opcao == "3":
            print("\n--- BUSCAR ALUNO ---")
            mat = input("Digite a matrícula: ")
            aluno = sistema.buscar_aluno(mat)
            if aluno != None:
                print(f"Encontrado -> Nome: {aluno._nome} | Curso: {aluno._curso}")
            else:
                print("Aluno não encontrado.")

        elif opcao == "4":
            print("\n--- REGISTRAR NOTA ---")
            mat = input("Digite a matrícula do aluno: ")
            try:
                nota = float(input("Digite a nota (0 a 10): "))
                sistema.registrar_nota(mat, nota)
            except ValueError:
                print("Erro: Digite um número válido para a nota.")

        elif opcao == "5":
            print("\n--- BOLETIM INDIVIDUAL ---")
            mat = input("Digite a matrícula do aluno: ")
            aluno = sistema.buscar_aluno(mat)
            if aluno != None:
                print(f"\nAluno: {aluno._nome} | Curso: {aluno._curso}")
                print(f"Notas: {aluno._notas}")
                print(f"Média: {aluno.calcular_media():.2f}")
                print(f"Situação: {aluno.obter_situacao()}")
            else:
                print("Aluno não encontrado.")

        elif opcao == "6":
            print("\n" + "="*30)
            print("      RELATÓRIO GERAL")
            print("="*30)
            rel = sistema.gerar_relatorio_geral()
            if rel == None:
                print("Nenhum dado disponível no sistema.")
            else:
                print(f"Total de Alunos Cadastrados: {rel['total_alunos']}")
                print(f"Alunos com Notas: {rel['alunos_com_notas']}")
                print("-" * 30)
                print("Contagem por Situação:")
                for situacao, qtd in rel['contagem_situacao'].items():
                    print(f" - {situacao}: {qtd}")
                print("-" * 30)
                if rel['alunos_com_notas'] > 0:
                    print(f"Média Geral da Turma: {rel['media_geral']:.2f}")
                    print(f"Maior Média: {rel['maior_media']:.2f}")
                    print(f"Menor Média: {rel['menor_media']:.2f}")
                else:
                    print("Nenhum aluno possui notas para calcular médias.")
            print("="*30)

        elif opcao == "7":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha um número de 1 a 7.")

if __name__ == "__main__":
    main()