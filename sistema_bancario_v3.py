from time import sleep

# Cria uma  linha com =
def linha():
  print("="*42)
  

# Cria um tiulo centralizado 
def titulo(txt):
  linha()
  print(f'|{txt:^40}|')
  linha()


# deposita um valor na conta
def deposito(saldo, extrato):
  while True:
    try:
      titulo('DEPÓSITO')
      deposito = float(input('Digite o valor do depósito: '))
      # verifica se o valor é positivo
      if deposito > 0:
        saldo += deposito
        print(f'Depósito realizado com sucesso.\nSaldo atual: R${saldo:.2f}')
        linha()
        # adiciona o valor do depósito ao extrato
        texto_extrato = f'R${deposito:.2f}'
        extrato += f'\033[92mDepósito{texto_extrato:.>20}\033[0m\n'
        # Da a opção de sair ou continuar
        acao = input('Deseja realizar outro depósito? (S/N): ')
        if acao.lower() == 'n':
          print('Saíndo', end='')
          for c in range(3):
            print('.', end='', flush=True)
            sleep(1)
          print()
          break
        elif acao.lower() == 's':
          print('Continuando' , end='')
          for c in range(3):
            print('.', end='', flush=True)
            sleep(1)
          print()
          continue
        else:
          print('Opção inválida. Tente novamente.')
          continue
      else:
        print('Valor inválido. Digite um valor positivo.')
    except ValueError:
      print('Valor inválido!')
  return saldo, extrato    


# saca um valor da conta
def saque(saldo, extrato,):
  numero_saques = 0
  limite_saque = 500
  while True:
    try:
      titulo('SAQUE')
      saque = float(input('Digite o valor do saque: '))
      # verifica se o valor é positivo e se tem saldo na conta
      saldo_suficiente = 0 < saque <= saldo
      # verifica se o número de saques é menor que o limite e se o valor do saque é menor ou igual ao limite de saque
      condicoes_saque = numero_saques <= 2 and saque <= limite_saque
      # verifica se as condições estão ok para o saque
      if saldo_suficiente and condicoes_saque is True:
        saldo -= saque
        numero_saques += 1
        texto_extrato = f'R${saque:.2f}'
        extrato += f'\033[91mSaque{texto_extrato:.>23}\033[0m\n'
        print(f'Saque realizado com sucesso.\nSaldo atual: R${saldo:.2f}')
      # Mensagem para saldo insuficiente 
      elif limite_saque <= saque > saldo:
        print('Saldo insuficiente para realizar o saque.')
      # Mensagem para número de saques excedido
      elif numero_saques > 2:
        print('Número máximo de saques excedido.')
      # Mensagem para valor de saque ultrapassando o limite de saque
      elif limite_saque < saque <= saldo:
        print('Valor de saque excede o limite de saque.')
      # Verifica se o usuário deseja continuar 
      opcao = input('Deseja realizar outro saque? (S/N): ')
      if opcao.lower() == 'n':
        print('Saindo', end='')
        for c in range(3):
          print('.', end='', flush=True)
          sleep(1)
        print()
        return saldo, extrato
      elif opcao.lower() == 's':
        print('Continuando', end='')
        for c in range(3):
          print('.', end='', flush=True)
          sleep(1)
        print()
      else:
        print('Opção inválida. Tente novamente.')
      
    except ValueError:
      print('Valor inválido!')
  

def criar_usuario(usuarios):
    while True:    
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF sem . ou -: ')
        if '-' and '.' not in cpf:
            if cpf not in usuarios:
                data_nascimento = input('Digite sua data de nascimento:')
                endereco = input('Digite seu endereço:\n(Rua - Número da Casa - Bairro - Cidade - Sigla do Estado)')
                usuarios.append({'Nome': nome, 'Data de nascimento': data_nascimento,
                                          'cpf': cpf, 'Endereço': endereco})
                opcao = input('Cadastrar novo usúario ? [S/N]: ')
                if opcao.lower() == 'n':
                    print('Saindo')
                    break
                elif opcao == '' or opcao.lower() == 's':
                    print('Continuando')
                else:
                    print('Opção inválida!!!')
            else:    
                print('Usúario já cadastrado!!!')           
        else:
            print('CPF inválido!!!')
        

def criar_contas(usuarios, contas, agencia):
    contador = 1
    while True:
        cpf = input('Informe seu CPF, sem - ou . : ')
        if cpf in usuarios:
            numero_conta = f'conta{contador}'
            contas.append({'agencia': agencia, 'nro_conta': numero_conta, 'usuario': cpf})
            contador += 1
            print(usuarios)

# Cria um cabeçalho personalizável 
def cabecalho(txt):
  linha()
  print(f'|{txt:^40}|')
  linha()
  

# Cria um menu para o usuário
def menu(txt):
  texto_menu = '''[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Sair
:'''
  saldo = 1330
  extrato = 'Extrato de Transações\n'
  while True:
    titulo(txt)
    saldo_atual = f'Saldo atual: R${saldo:.2f}'
    print(f'|{saldo_atual:<40}|')
    linha()
    
    opcao = input(texto_menu)
    try:
      # seleciona que o usuário deseja fazer
      if opcao == '1':
        saldo, extrato = deposito(saldo, extrato)
      elif opcao == '2':
        saldo, extrato = saque(saldo, extrato)
      elif opcao == '3':
        print(extrato)
      elif opcao == '0':
        print('Saindo', end='')
        for c in range(3):
          print('.', end='', flush=True)
          sleep(1)
        print()
        break
    except ValueError:
      print('Valor inválido!')


def main():
   usuarios = []
   contas = []
   agencia = '0001'

menu('Menu Principal')