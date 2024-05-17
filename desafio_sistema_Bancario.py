import random
import string

def generate_password(length=4):
    digits = string.digits
    password = ''.join(random.choices(digits, k=length))
    return password

def depositar(saldo, extrato, /):
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

def sacar(*, saldo, extrato, numero_saques, limite, limite_saques):
    while True:
        try:
            valor = float(input("Informe o valor do saque: "))
            break
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

def exibir_extrato(saldo, / , *, extrato):
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
    [cu]criar usuario
    [cc]criar conta
    [q] Sair

    => """
    opcao = input(menu)
    return opcao

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if  usuario:
        print("CPF já está em nossa lista de usuarios")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd/mm/aaaa): ")
    endereco = input("Informe seu endereço (logradouro, numero - bairro - cidade - sigla do estado): ")
    password = generate_password()

    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "Endereço": endereco, "senha": password})

    print("Usuario cadastrado com sucesso!\nAnote sua senha: ", password)
    

def filtrar_usuario(cpf, usuarios):
    verificacao_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return verificacao_usuario[0] if verificacao_usuario else None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário(somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if(usuario):
        senha = input("Digite a senha do usuário: ")
        if senha == usuario["senha"]:
            print("Conta cadastrada com sucesso!\n")
            return { "Agência: ": AGENCIA, "Número da conta" : numero_conta, "usuário" : usuario}
        else: 
            print("Senha incorreta.")
            return None
    else:
        print(" Usuário não encontrado, verifique novamente as informações e tente novamente depois!")
    

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo=saldo, 
                                                  extrato=extrato, 
                                                  numero_saques= numero_saques, 
                                                  limite=limite, 
                                                  limite_saques=LIMITE_SAQUES,
                                                  )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "cu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta =  criar_conta(AGENCIA, numero_conta, usuarios)
            if conta: 
                contas.append(conta)

        elif opcao == "q":
            break

        else:
            print("Algo deu errado, valor inválido inserido")

main()