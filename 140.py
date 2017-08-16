def criando_nome(primeiro_nome, segundo_nome):
    nome_completo = primeiro_nome + ' ' + segundo_nome
    return nome_completo.title()
while True:
    print('\nSeu nome:')
    print("(coloque a letra 'q' e pressione enter para sair.)")
    pri_nome = input('Primeiro nome: ')
    if pri_nome == 'q':
        break
    seg_nome = input('Segundo nome: ')
    if seg_nome == 'q':
        break
    formatando_nome = criando_nome(pri_nome, seg_nome)
    print('\nOlá, ' + formatando_nome + '!')
#Nesse exemplo usamos um loop while. Solicitamos ao usuário que digite seu nome separadamente, mas não definimos uma condição de encerramento.
#Para o usuário sair mais fácil, a cada prompt oferecemos uma maneira de sair do loop.
#Assim que o usuário entrar com o valor de saída ele sairá do loop.