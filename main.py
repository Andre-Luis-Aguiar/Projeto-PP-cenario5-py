from sistema import *

# Menu
def mostrarMenu():
    print("\n===== MENU =====")
    print("1. Cadastrar Paciente")
    print("2. Alterar Dados do Paciente")
    print("3. Excluir Paciente fornecendo o Código")
    print("4. Localizar um Paciente pelo Código")
    print("5. Listagem geral dos Pacientes")
    print("6. Sair do sistema")
    return input("Escolha uma opção: ")

# loop_principal
while True:
    opcao = mostrarMenu()
    
    if opcao == "1":
        codigo = input("Digite o código do paciente: ")
        nome = input("Digite o nome do paciente: ")
        idade = input("Digite a idade do paciente: ")
        sexo = input("Digite o sexo do paciente: ")
        diagnostico = input("Digite o diagnóstico do paciente: ")
        cadastrarPaciente(codigo, nome.upper(), idade, sexo.upper(), diagnostico.upper())
    elif opcao == "2":
        codigo = input("Digite o código do paciente: ")
        nome = input("Digite o nome do paciente: ")
        idade = input("Digite a idade do paciente: ")
        sexo = input("Digite o sexo do paciente: ")
        diagnostico = input("Digite o diagnóstico do paciente: ")
        alterarDados(codigo, nome, idade, sexo, diagnostico)
    elif opcao == "3":
        codigo = input("Digite o código do paciente que deseja excluir: ")
        excluirPaciente(codigo)
    elif opcao == "4":
        codigo = input("Digite o código do paciente que deseja localizar: ")
        localizarPaciente(codigo)
    elif opcao == "5":
        listarPacientes()
    elif opcao == "6":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")