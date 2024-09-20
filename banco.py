saldo = 0.0
saques_permitidos = 3
LIMITE = 500
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
        print("Impossivel sacar valor negativo!")
    if saques_permitidos == 0:
        print("Você não pode sacar mais nenhum valor hoje!")
        return False
    if valor > LIMITE:
        print(f"O valor R${valor:.2f} excede o limite de R${LIMITE:.2f}!")
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
    escolha = input(menu)
    if escolha == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        if deposito(valor):
            saldo += valor
            extrato.append(f"Depósito: R${valor:.2f}")
            #print(saldo, extrato)
    elif escolha == "s":
        valor = float(input("Digite o valor que deseja sacar: "))
        if saque(valor, saldo):
            saldo -= valor
            extrato.append(f"Saque: R${valor:.2f}")
            saques_permitidos -= 1
            #print(saldo, extrato)
    elif escolha == "e":
        mostrar_extrato(extrato)
    elif escolha == "q":
        break
    else:
        print("Operação invalida")
    
