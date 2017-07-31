usuario_1 = {'nickname': 'Leo',
    'nome': 'Leoander',
    'nome_2': 'Neves',
    }
# Se você quisesse ver todos os dados do usuario, você pode fazer um loop através do dicionário.
for chave, valor in usuario_1.items():
    print('\nChave: ' + chave)
    print('Valor: ' + valor)
# Para escrever um loop para um dicionário você cria nomes para as duas variáveis ​​que manterão a chave e o valor.
# A segunda metade da declaração for em que você inclui o nome do dicionário no método items() retorna a lista de vlaores.
# O loop for armazena cada um desses pares nas duas variáveis ​​fornecidas.