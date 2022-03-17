

# cadastrar
# atualizar
# deletar
# buscar
# banco de dados sql3


while True:
    print('-=' * 15)
    print('Sistem de Cadastro Mecanica')
    print('-=' * 15)
    print('Cadastrar cliente: 1')
    print('Buscar Cliente: 2')
    print('Atualizar Cadastro: 3')
    print('Deletar Cliente: 4')
    print('Sair do programa: 5')
    print('-=' * 15)
    opc = int(input('Digite a Opção: '))
    if opc == 5:
        print('Exit')
        break
    elif opc == 1:
        print()