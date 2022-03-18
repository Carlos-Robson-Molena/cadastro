import sqlite3
# banco de dados sqlite
banco = sqlite3.connect('oficina.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE clientes (nome text, cpf integer, carro text, placa text)")
#cursor.execute("INSERT INTO clientes VALUES('karem', 123456789, 'celta', 'asd1234' )")
#banco.commit()

cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())
# cadastrar
# atualizar
# deletar
# buscar


'''
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
        print()'''