menu = '''
Selecione a opção desejada!

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

'''
saldo = 0
valor_limite_por_saque = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = int(input(menu))

    if opcao == 0:
        print("Você selecionou a opção DEPOSITAR\n")
        deposito = int(input('Quanto você deseja depositar?\n'))
        if deposito > 0:
            saldo += deposito
            extrato += (f'Depósito: R$ {deposito:.2f}\n')
            print ('\nDepósito realizado!')
        else:
            print('Operação inválida! O valor deve ser maior que 0!')

    elif opcao == 1:
        if numero_saques < LIMITE_SAQUES:
            print("Você selecionou a opção SACAR\n")
            saque = int(input('Quanto você deseja sacar?\n'))
            if saque <= valor_limite_por_saque:
                if saque <= saldo:
                    saldo -= saque
                    extrato += (f'Saque:   -R$ {saque:.2f}\n')
                    print ('\nSaque realizado!')
                    numero_saques += 1
                else:
                    print('Saldo insuficiente!')
            else:
                print('Valor limite de saque excedido!')
        else:
            print ('Limite de saques diários excedido!')

    elif opcao == 2:
        mensagem_extrato = f'''
========== EXTRATO ==========\n
{extrato}
Saldo atual: R$ {saldo:.2f}'''
        print(mensagem_extrato)

    elif opcao == 3:
        print('Obrigado por usar o nosso sistema!')
        break

    else:
        print('Operação inválida. Selecione novamente a operação desejada!')

    

