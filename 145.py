def criando_perfil(primeiro, ultimo, **info_usuario):
    perfil = {}
    perfil['priemiro_nome'] = primeiro
    perfil['último_nome'] = ultimo
    for chave, value in info_usuario.items():
        perfil[chave] = value
    return perfil
info_usuario = criando_perfil('fulano de', 'tal', local='nove zelândia', trabalho='programador')
print(info_usuario)
#A definição de criando_perfil() espera um primeiro e último nome e permite que o usuário passe em tantos pares nome-valor quanto quiserem.
#Os asteriscos duplos antes do parâmetro fazem com que o Python crie um dicionário vazio e conecte o mesmo nome-valor que ele recebe nesse dicionário.
#Dentro da função, você pode acessar os pares de valor de nome em info_usuario exatamente como você faria para qualquer dicionário.