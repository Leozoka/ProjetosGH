#Podemos aninhar um dicionário dentro de outro dicionário (mas podemos nos complicar facilmente).
usuarios = {
    'lneves.8': {
        'nome': 'leo',
        'sobrenome': 'neves',
        'localização': 'nova zelândia',
        },
    'peres.60': {
        'nome': 'edu',
        'sobrenome': 'peres',
        'localização': 'canadá',
        },
    }
for usuario, usuarios_info in usuarios.items():
    print('\nNome de usuário: ' + usuario)
    nome_comp = usuarios_info['nome'] + ' ' + usuarios_info['sobrenome']
    local = usuarios_info['localização']
    print('\tNome completo: ' + nome_comp.title())
    print('\tLocalização: ' + local.title())
#Definimos um dicionário com duas chaves para cada usuário, Python armazena cada chave na variável usuário e o dicionário associado a cada nome de usuário.
#Dentro do loop imprimimos o nome de usuário, depois acessamos o dicionário interno com as informações do usuário. Cada chave gera o nome, a localização, perfeitamente formatados para cada pessoa.
