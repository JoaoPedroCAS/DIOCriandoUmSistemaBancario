from datetime import datetime

saldo = 0.0
saques_permitidos = 3
LIMITE = 500
transacoes_diarias = 0
LIMITE_TRANSACOES = 10
extrato = []
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def deposito(valor):
    if valor < 0:
        print("Não é possível depositar valores negativos!")
        return False
    return True

def saque(valor, saldo):
    if valor < 0:
        print("Impossível sacar valor negativo!")
        return False
    if saques_permitidos == 0:
        print("Você não pode sacar mais nenhum valor hoje!")
        return False
    if valor > LIMITE:
        print(f"O valor R${valor:.2f} excede o limite de R${LIMITE:.2f}!")
        return False
    if valor > saldo:
        print(f"O valor de R${valor:.2f} excede o saldo em conta de R${saldo:.2f}")
        return False
    return True

def mostrar_extrato(extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:  
        for item in extrato:
            print(item)

while True:
    if transacoes_diarias >= LIMITE_TRANSACOES:
        print("Você excedeu o número de transações permitidas para hoje.")
        break

    escolha = input(menu)
    
    if escolha == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        if deposito(valor):
            saldo += valor
            transacoes_diarias += 1
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{data_hora} - Depósito: R${valor:.2f}")
    
    elif escolha == "s":
        valor = float(input("Digite o valor que deseja sacar: "))
        if saque(valor, saldo):
            saldo -= valor
            transacoes_diarias += 1
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{data_hora} - Saque: R${valor:.2f}")
            saques_permitidos -= 1
    
    elif escolha == "e":
        mostrar_extrato(extrato)
    
    elif escolha == "q":
        break
    
    else:
        print("Operação inválida")
