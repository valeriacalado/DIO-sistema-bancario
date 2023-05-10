
saldo = 1500
deposito = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    operacao = input("Digite: \n[1] DEPÓSITO \n[2] SAQUE \n[3] EXTRATO \n[4] SAIR\n")

# DEPÓSITO
    if operacao == str(1):
        try:
            valor_depositado = float(input("Digite o valor a ser depositado: "))
            if valor_depositado > 0:
                print("Depósito realizado com sucesso. ")
                extrato += (f'Depósito: + R$ {valor_depositado:.2f}\n')
            saldo += valor_depositado
            print(f"Seu saldo é R${saldo}")
        except:
            print("Operação falhou, digite um valor válido.")
        continue

#SAQUE
    elif operacao == str(2):
        try:
            valor_a_sacar = float(input("Digite o valor a ser sacado: "))
            if (numero_saques < 3) == True:
                if (valor_a_sacar <= 500) and (valor_a_sacar <= saldo):
                    print("Saque realizado com sucesso.")
                    extrato += (f"Saque: - R$ {valor_a_sacar}\n")
                    saldo -= valor_a_sacar
                    print(f"Seu saldo é R${saldo}'")
                    numero_saques += 1
            if valor_a_sacar > saldo:
                print("Saldo insuficiente para realizar a operação.")
            elif valor_a_sacar > 500:
                print("Seu limite é de R$ 500,00 (quinhentos reais) por saque. Tente novamente.")
            elif numero_saques >= 3:
                print("Você atingiu o limite de saques diário.")
            else:
                print("Operação falhou, digite um valor válido.")
        except:
            print("Operação falhou, digite um valor válido.")
        continue

# EXTRATO
    elif operacao == str(3):
        print("==========================\nExtrato Bancário\n==========================")
        print(extrato)
        print("==========================")
        continue
    
    elif operacao == str(4):
        print("Obrigado por utilizar nossos serviços.")
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada.")
        continue