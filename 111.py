#Pode aninhar uma lista dentro de um dicionário sempre que quiser que mais de um valor seja associado a uma única chave em um dicionário.
linguagens_favoritas = {
    'leo': ['python', 'java'],
    'edu': ['object pascal'],
    'hulgo': ['c#', 'c++', 'python']
    }
for nome, linguagens in linguagens_favoritas.items():
    print('\n' + nome.title() + ', suas linguagens favoritas são:')
    for linguaguem in linguagens:
        print('\t' + linguaguem.title())
#Associamos cada nome a sua lista de linguagens favoritas.
#No primeiro loop percorremos a lista de nomes e no segundo loop as linguagens.