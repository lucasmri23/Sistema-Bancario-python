import textwrap

saldo=0
limite=500
extrato=''
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = {}
contas = []

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

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente número): ")
    user = verifica_cpf(cpf, usuarios)

    if user:
        print("Usuário já cadastrado com esse numero de CPF!")
        pause = input("Pressione Enter para continuar...")
        limpa_tela()
        return
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/UF): ")
    usuarios[cpf] = {"cpf":cpf,"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    print("Usuário cadastrado com sucesso!")
    pause = input("Pressione Enter para continuar...")
    limpa_tela()
    return

def verifica_cpf(cpf, usuarios):
    verificacao_usuario = [usuario for usuario in usuarios.values() if usuario["cpf"] == cpf]
    return verificacao_usuario[0] if verificacao_usuario else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    user = verifica_cpf(cpf, usuarios)

    if user:
        print("Conta cadastrada com sucesso!")
        pause = input("Pressione Enter para continuar...")
        limpa_tela()
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": user}
    
    print("Usuário não encontrado, a conta não foi criada!")
    pause = input("Pressione Enter para continuar...")
    limpa_tela()
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))
        pause = input("Pressione Enter para continuar...")
        limpa_tela()

def main():
    menu = '''
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar usuário
    [c] Criar conta corrente
    [l] Listar contas
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
        elif switch == 'u':
            criar_usuario(usuarios);
        elif switch == 'c':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios);
            if conta:
                contas.append(conta)
        elif switch == 'l':
            listar_contas(contas)
        elif switch == 'q':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

main()