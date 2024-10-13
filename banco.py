from datetime import datetime

# Classe Conta que contém as operações de depósito, saque e extrato
class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0.0
        self.extrato = []
        self.limite = 500.0
        self.numero_saques = 0
        self.limite_saques = 3
    
    # Método de depósito
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito!")
            return

        self.saldo += valor
        self.extrato.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    
    # Método de saque
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente. Saldo atual: R${self.saldo:.2f}")
            return

        if valor > self.limite:
            print(f"O valor R${valor:.2f} excede o limite de R${self.limite:.2f} por saque.")
            return

        if self.numero_saques >= self.limite_saques:
            print("Você atingiu o limite de saques diários.")
            return

        self.saldo -= valor
        self.extrato.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R${valor:.2f}")
        self.numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    
    # Método para exibir extrato
    def exibir_extrato(self):
        print("\nEXTRATO:")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for item in self.extrato:
                print(item)
        print(f"\nSaldo atual: R${self.saldo:.2f}\n")

# Função para cadastrar usuários
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário cadastrado com este CPF.")
            return
    
    # Cria um novo usuário
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

# Função para criar conta corrente
def criar_conta(cpf_usuario):
    global numero_conta_sequencial
    
    # Verifica se o CPF do usuário existe
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf_usuario:
            usuario_encontrado = usuario
            break
    
    if not usuario_encontrado:
        print("Usuário não encontrado. Verifique o CPF e tente novamente.")
        return

    # Cria uma nova conta
    nova_conta = Conta("0001", numero_conta_sequencial, usuario_encontrado)
    contas.append(nova_conta)
    numero_conta_sequencial += 1
    print(f"Conta criada com sucesso! Número da conta: {nova_conta.numero_conta}")

# Função para listar todas as contas cadastradas
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("Contas cadastradas:")
    for conta in contas:
        usuario = conta.usuario
        print(f"Agência: {conta.agencia}, Conta: {conta.numero_conta}, Titular: {usuario['nome']} (CPF: {usuario['cpf']})")

# Exemplo de uso
usuarios = []  # Lista de usuários
contas = []  # Lista de contas
numero_conta_sequencial = 1  # Sequencial de contas

# Menu principal
while True:
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Exibir Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair
    => """
    
    opcao = input(menu).lower()

    if opcao == 'd':
        numero_conta = int(input("Informe o número da conta para depósito: "))
        valor = float(input("Informe o valor do depósito: "))
        for conta in contas:
            if conta.numero_conta == numero_conta:
                conta.depositar(valor)
                break
        else:
            print("Conta não encontrada.")

    elif opcao == 's':
        numero_conta = int(input("Informe o número da conta para saque: "))
        valor = float(input("Informe o valor do saque: "))
        for conta in contas:
            if conta.numero_conta == numero_conta:
                conta.sacar(valor)
                break
        else:
            print("Conta não encontrada.")

    elif opcao == 'e':
        numero_conta = int(input("Informe o número da conta para exibir o extrato: "))
        for conta in contas:
            if conta.numero_conta == numero_conta:
                conta.exibir_extrato()
                break
        else:
            print("Conta não encontrada.")

    elif opcao == 'nu':
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")
        cadastrar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == 'nc':
        cpf_usuario = input("Informe o CPF do usuário: ")
        criar_conta(cpf_usuario)

    elif opcao == 'lc':
        listar_contas()

    elif opcao == 'q':
        break

    else:
        print("Opção inválida!")
