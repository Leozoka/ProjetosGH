def criando_nome(primeiro_nome, segundo_nome):
    pessoa = {'primeiro': primeiro_nome, 'segundo': segundo_nome}
    return pessoa
nome = criando_nome('fulano de', 'tal')
print(nome)
#A função criando_nome() leva o primeiro e o segundo nome, e coloca esses valores em um dicionário.
#Os valores são armazenados na chave.
#O valor do retorno agora é impresso com as informações textuais armazenadas em um dicionário.