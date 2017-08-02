#Vamos percorrer os nomes no dicionário como fizemos anteriormente, mas quando o nome corresponde a um dos nossos amigos, iremos exibir uma mensagem sobre a sua linguagem favorita.
linguagens = {
    'ana': 'java',
    'beatriz': 'python',
    'pablo': 'c',
    }
amigos = ['ana', 'beatriz']
for nome in linguagens.keys():
    print(nome.title())
    if nome in amigos:
        print('Olá ' + nome.title() +
              ', sua linguagem favorita é: ' +
              linguagens[nome].title() + '!')
#Criamos uma lista de amigos para os quais queremos imprimir uma mensagem. Dentro do loop imprimimos o nome de cada pessoa.
#Se o nome da pessoa estiver dentro da lista de amigos. irá imprimir uma mensagem para ela.