def usuarios_login(usuarios):
    for usuario in usuarios:
        msg = 'Bem-vindo(a) ' + usuario.title() + '!'
        print(msg)
apelidos = ['joaozin089', 'clarice084']
usuarios_login(apelidos)
#Definimos um login para os usuários, com isso fizemos uma lista de nomes dos usários que armazena nos parâmetros.
#Depois passamos os logins para a chamada de função.
#A função percorre a lista que recebe e imprime uma frase para o usuário.