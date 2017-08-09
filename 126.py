u_nconfirmados = ['bia', 'joão', 'maria']
u_convi = []
while u_nconfirmados:
    u_confirmados = u_nconfirmados.pop()
    print('Verificando convidado(a): ' + u_confirmados.title())
    u_convi.append(u_confirmados)
print('\nLista dos convidados confirmados:')
for u_convi in u_convi:
    print(u_convi.title())
#Começamos com uma lista de usuários não confirmados e uma lista vazia para manter usuários confirmados.
#O loop while corre enquanto a lista de convidados não confirmados não está vazia, dentro deste loop a função pop() remove usuários não verificados a cada vez do final de não confirmados.
#Confirmamos a presença de cada usuário, imprimindo uma mensagem de verificação e depois adicionando-os à lista de usuários confirmados.