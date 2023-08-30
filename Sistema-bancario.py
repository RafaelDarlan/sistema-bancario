menu = """

[c] Criar Conta
[u] Criar Usuário
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

contas = {}

def criar_conta(numero, limite):
    global contas
    if numero not in contas:
        contas[numero] = {
            "saldo": 0,
            "limite": limite,
            "extrato": "",
           "numero_saques": 0,
            "LIMITE_SAQUES": 3,
            "usuario": None
        }
        print(f"Conta {numero} criada com sucesso.")
    else:
        print("Operação falhou! Número de conta já existente.")

def criar_usuario(numero, nome, sobrenome):
    global contas
    if numero in contas:
        if contas[numero]["usuario"] is None:
            contas[numero]["usuario"] = {"nome": nome, "sobrenome": sobrenome}
            print(f"Usuário {nome} {sobrenome} criado com sucesso.")
        else:
            print("Operação falhou! Conta já possui um usuário associado.")
    else:
        print("Operação falhou! Conta não encontrada.")

def depositar(numero, valor):
    global contas
    if numero in contas:
        conta = contas[numero]
        if valor > 0:
            conta["saldo"] += valor
            conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Operação falhou! Conta não encontrada.")

def sacar(numero, valor):
    global contas
    if numero in contas:
        conta = contas[numero]
        excedeu_saldo = valor > conta["saldo"]
        excedeu_limite = valor > conta["limite"]
        excedeu_saques = conta["numero_saques"] >= conta["LIMITE_SAQUES"]
 
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido")
        elif valor > 0:
            conta["saldo"] -= valor
            conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
            conta["numero_saques"] += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Operação falhou! Conta não encontrada.")

def mostrar_extrato(numero):
    global contas
    if numero in contas:
        conta = contas[numero]
        extrato = conta["extrato"]
        saldo = conta["saldo"]
        print("\n###############Extrato###############")

        if conta["usuario"] is not None:
            print(f"Usuário: {conta['usuario']['nome']} {conta['usuario']['sobrenome']}")
        else:
            print("Usuário: Não associado")
      
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("######################################")
    else:
        print("Operação falhou! Conta não encontrada.")

while True:
 
    opcao = input(menu)

    if opcao == "c":
        numero = input("Informe o número da conta: ")
        limite = int(input("Informe o limite de saques: "))
        criar_conta(numero, limite)
    elif opcao == "u":
        numero = input("Informe o número da conta: ")
        nome = input("Informe o nome do usuário: ")
        sobrenome = input("Informe o sobrenome do usuário: ")
        criar_usuario(numero, nome, sobrenome)  
    elif opcao == "d":
        numero = input("Informe o número da conta: ")
        valor = float(input("Informe o valor do depósito: "))
        depositar(numero, valor)
    elif opcao == "s":
        numero = input("Informe o número da conta: ")
        valor = float(input("Informe o valor do saque: "))
        sacar(numero, valor)
    elif opcao == "e":
        numero = input("Informe o número da conta: ")
        mostrar_extrato(numero)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, selecione umas das opções do menu.")