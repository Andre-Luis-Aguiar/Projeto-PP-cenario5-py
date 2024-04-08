# dicionario
pacientes = {}

# cadastro_paciente
def cadastrarPaciente(codigo, nome, idade, sexo, diagnostico):
    pacientes[codigo] = {'nome': nome, 'idade': idade, 'sexo': sexo, 'diagnostico': diagnostico}
    print("Paciente cadastrado com sucesso.")
    
# alterar_dados
def alterarDados(codigo, nome, idade, sexo, diagnostico):
    if codigo in pacientes:
        pacientes[codigo] = {'nome': nome,'\n' 'idade': idade,'\n' 'sexo': sexo,'\n' 'diagnostico': diagnostico}
        print("Dados do paciente alterados com sucesso.")
    else:
        print("Paciente não encontrado.")

# excluir_paciente 
def excluirPaciente(codigo):
    if codigo in pacientes:
        del pacientes[codigo]
        print("paciente excluído com sucesso.")
    else:
        print("Paciente não encontrado.")

# localizar_paciente
def localizarPaciente(codigo):
    if codigo in pacientes:
        print("Código: ", codigo)
        for key, value in pacientes[codigo].items():
            print(key.capitalize()+ ":", value)
    else:
        print("Paciente não encontrado.")

# listar_pacientes
def listarPacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado ainda.")
        return
    
    quantidade_pacientes = len(pacientes)
    
    somatorio_idades = sum(int(paciente['idade']) for paciente in pacientes.values())
    
    # Média das idades dos pacientes
    if quantidade_pacientes > 0:
        media_idades = somatorio_idades / quantidade_pacientes
    else:
        media_idades = 0
    
    print("\n===== LISTA DE PACIENTES =====")
    for codigo, paciente in pacientes.items():
        print("Código:", codigo)
        for key, value in paciente.items():
            print(key.capitalize() + ":", value)
        print()
    
    print("\nQuantidade geral de pacientes:", quantidade_pacientes)
    print("Média das idades dos pacientes:", media_idades)