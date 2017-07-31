linguagens = {
    'bruno': 'python',
    'alan': 'java',
    'ana': 'c#',
    }
# Python não se preocupa com a ordem em que os pares chave-valor são armazenados. Ele rastreia apenas as conexões entre as chaves individuais e seus valores.
for nome, linguagem in linguagens.items():
    print(nome.title() + ' sua linguagem favorita é: ' +
          linguagem.title() + '.')
# Looping através de todos os pares de valores-chave funciona particularmente bem para os dicionários.
# Este tipo de looping funcionaria tão bem se o nosso dicionário armazenasse os resultados da pesquisa de mil ou mesmo um milhão de pessoas.