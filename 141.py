def lista_usuários(nomes):
    for nome in nomes:
        msg = 'Olá, ' + nome.title() + '!'
        print(msg)
usuários = ['epaminôndas', 'fulano']
lista_usuários(usuários)
#Definimos uma lista de nomes em lista_usuários, que ele armazena nos nomes dos parâmetros.
#A função percorre a lista e imprime um Olá para cada usuário.