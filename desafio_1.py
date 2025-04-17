saldo=0
limite=500
extrato=''
numero_saques = 0
LIMITE_SAQUES = 3

def limpa_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def deposito(valor):
    global saldo, extrato
    if( valor > 0):
        saldo+= valor
        print("Valor depositado com sucesso!")
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido para depósito!")
    pause = input("Pressione Enter para continuar...")
    # Limpa a tela após a operação
    limpa_tela()
    return

def saque(valor):
    global saldo, extrato, numero_saques
    if numero_saques >= LIMITE_SAQUES:
        print("Limite máximo de saques diários atingido!")
    else:
        if valor> saldo:
            print("Saldo insuficiente para esta operação!")
        elif valor > limite:
            print("Valor excede o limite de saque!")
        elif valor <= 0:
            print("Valor inválido para saque!")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
    pause = input("Pressione Enter para continuar...")
    # Limpa a tela após a operação
    limpa_tela()
    return

def extratos():
    print("\n========= EXTRATO =========")
    print(f"\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("\n===========================")
    pause = input("Pressione Enter para continuar...")
    # Limpa a tela após a operação
    limpa_tela()
    return

def main():
    menu = '''
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================
    '''

    while True:
        switch = input(menu).lower()
        if switch == 'd':
            valor = float(input("Digite o valor para depósito: "))
            deposito(valor)
        elif switch == 's':
            valor = float(input("Digite o valor para saque: "))
            saque(valor)
        elif switch == 'e':
            extratos()
        elif switch == 'q':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

main()