def criando_nome(primeiro_nome, segundo_nome, idade= ''):
    pessoa = {'primeiro': primeiro_nome, 'segundo': segundo_nome}
    if idade:
        pessoa['idade'] = idade
    return pessoa
nome = criando_nome('fulano de', 'tal', idade=38)
print(nome)
#Adicionamos idade como parâmetro opcional à definição da função e e atribuímos o parâmetro a um valor padrão vazio.
#Se a chamada de função incluir um valor para este parâmetro, o valor é armazenado no dicionário.
#Esta função sempre armazena o nome de uma pessoa, mas também pode ser modificada para armazenar qualquer outra informação.