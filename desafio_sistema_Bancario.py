def depositar(saldo, extrato):
    while True:
        try:
            valor = float(input("Qual o valor que será depositado: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número.")    
    if valor > 0:
        saldo += valor
        extrato += f"Depositado: R$ {valor:.2f}\n"
    else:
        print("ERROR 404, certifique-se que o valor inserido é positivo")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques,limite, limite_saques):
    while True:
        try:
            valor = float(input("Informe o valor do saque: "))
            break  # Sai do loop se o valor for válido
        except ValueError:
            print("Valor inválido. Digite um número.")

    if valor > saldo:
        print("Você não possui saldo suficiente para realizar esta operação.")

    elif valor > limite:
        print(f"Valor superior ao limite de saque, seu limite é de R$ {limite:.2f} por saque\n")
    
    elif numero_saques >= limite_saques:
        print(f"Operação falhou! Número máximo de saques diários excedido. Seu limite diário é de: {limite_saques}")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    
    else: 
        print("Algo deu errado, valor inválido inserido")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n############## EXTRATO ##############")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("##########################################")

def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    opcao = input(menu)
    return opcao

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques,limite, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            break

        else:
            print("Algo deu errado, valor inválido inserido")

main()