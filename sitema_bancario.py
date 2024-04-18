menu = '''[D]-Depositar 
[S]-Sacar
[E]-Extrato
[Q]-Sair
'''
saldo = 1000
limite = 500
limite_saques = 3
numero_saques = 0
extrato = ''

while True:
    opcao = input(menu)
    opcao = opcao.lower()
    if opcao == 'd':
        print('Depósito')
        try:
            deposito = float(input('Digite o valor do depósito: R$'))
            if deposito > 0:
                saldo += deposito
                extrato += f'Depósito: R${deposito:.2f}\n'
            else:
                print('Valor inválido!!!')
        except ValueError:
            print('Valor inválido!!!')
    elif opcao == 's':
        print('Saques')
        if numero_saques < limite_saques:
            saque = float(input('Digite o valor do saque: R$'))
            if 0 < saque <= saldo and saque <= 500:
                saldo -= saque
                extrato += f'Saque: R${saque:.2f}\n'
                numero_saques += 1
            elif 500 <= saque <= saldo:
                print('Valor acima do limite!')
            else: 
                print('Saldo insuficiente!!!')
        else:
            print('Limite de saques excedido!!!')
    elif opcao == 'e':
        print('Extrato')
        print(extrato)
    elif opcao == 'q':
        print('Saindo...')
        break
