from datetime import datetime

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        conta.adicionar_transacao(transacao)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica que herda de Cliente
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Classe Historico para armazenar transações
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Interface de Transação
class Transacao:
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        pass

# Classe Deposito que herda de Transacao
class Deposito(Transacao):
    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao({
            "tipo": "Depósito",
            "valor": self.valor,
            "data": datetime.now()
        })

# Classe Saque que herda de Transacao
class Saque(Transacao):
    def registrar(self, conta):
        if conta.saldo >= self.valor and conta.numero_saques < conta.limite_saques and self.valor <= conta.limite:
            conta.saldo -= self.valor
            conta.numero_saques += 1
            conta.historico.adicionar_transacao({
                "tipo": "Saque",
                "valor": self.valor,
                "data": datetime.now()
            })
            return True
        return False

# Classe Conta
class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def adicionar_transacao(self, transacao):
        transacao.registrar(self)

# Classe ContaCorrente que herda de Conta
class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente):
        super().__init__(numero, agencia, cliente)
        self.limite = 500.0
        self.numero_saques = 0
        self.limite_saques = 3

# Listas para armazenar clientes e contas
clientes = []
contas = []
numero_conta_sequencial = 1

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF (somente números): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    # Verificar se o CPF já está cadastrado
    for cliente in clientes:
        if cliente.cpf == cpf:
            print("Já existe um cliente cadastrado com este CPF.")
            return

    novo_cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")

# Função para criar uma nova conta
def criar_conta():
    cpf_cliente = input("Informe o CPF do cliente: ")

    # Buscar cliente pelo CPF
    cliente_encontrado = None
    for cliente in clientes:
        if cliente.cpf == cpf_cliente:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        global numero_conta_sequencial
        nova_conta = ContaCorrente(numero_conta_sequencial, "0001", cliente_encontrado)
        contas.append(nova_conta)
        cliente_encontrado.adicionar_conta(nova_conta)
        numero_conta_sequencial += 1
        print(f"Conta criada com sucesso! Número da conta: {nova_conta.numero}")
    else:
        print("Cliente não encontrado. Verifique o CPF e tente novamente.")

# Função para listar as contas de um cliente
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("Contas cadastradas:")
    for conta in contas:
        cliente = conta.cliente
        print(f"Agência: {conta.agencia}, Conta: {conta.numero}, Titular: {cliente.nome} (CPF: {cliente.cpf})")

# Função para realizar um depósito
def realizar_deposito():
    numero_conta = int(input("Informe o número da conta para depósito: "))
    valor = float(input("Informe o valor do depósito: "))

    for conta in contas:
        if conta.numero == numero_conta:
            deposito = Deposito(valor)
            conta.adicionar_transacao(deposito)
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            return
    print("Conta não encontrada.")

# Função para realizar um saque
def realizar_saque():
    numero_conta = int(input("Informe o número da conta para saque: "))
    valor = float(input("Informe o valor do saque: "))

    for conta in contas:
        if conta.numero == numero_conta:
            saque = Saque(valor)
            if saque.registrar(conta):
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print(f"Não foi possível realizar o saque. Verifique o saldo ou o limite de saques.")
            return
    print("Conta não encontrada.")

# Função para exibir o extrato de uma conta
def exibir_extrato():
    numero_conta = int(input("Informe o número da conta para exibir o extrato: "))

    for conta in contas:
        if conta.numero == numero_conta:
            print("\nEXTRATO:")
            if not conta.historico.transacoes:
                print("Não foram realizadas movimentações.")
            else:
                for transacao in conta.historico.transacoes:
                    tipo = transacao["tipo"]
                    valor = transacao["valor"]
                    data = transacao["data"].strftime("%d/%m/%Y %H:%M:%S")
                    print(f"{data} - {tipo}: R${valor:.2f}")
            print(f"\nSaldo atual: R${conta.saldo:.2f}")
            return
    print("Conta não encontrada.")

# Menu principal
while True:
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Exibir Extrato
    [nc] Nova Conta
    [nu] Novo Cliente
    [lc] Listar Contas
    [q] Sair
    => """

    opcao = input(menu).lower()

    if opcao == 'd':
        realizar_deposito()

    elif opcao == 's':
        realizar_saque()

    elif opcao == 'e':
        exibir_extrato()

    elif opcao == 'nc':
        criar_conta()

    elif opcao == 'nu':
        cadastrar_cliente()

    elif opcao == 'lc':
        listar_contas()

    elif opcao == 'q':
        break

    else:
        print("Opção inválida!")
