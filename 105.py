#O método values() mostra os valores que um dicionário contém.
linguagens = {
    'leo': 'python',
    'eduardo': 'c++',
    'bruno': 'java'
    }
print('Linguagens mencionadas:')
for linguagem in linguagens.values():
    print(linguagem.title())
