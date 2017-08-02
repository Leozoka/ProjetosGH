# O método keys() é útil quando você não precisa trabalhar com todos os valores em um dicionário.
linguagens = {
    'leo': 'python',
    'bruno': 'C++',
    'diogo': 'java',
    }
for nome in linguagens.keys():
    print(nome.title())
#Python puxa todas as chaves do dicionário e armazena uma a uma no nome da variável. A saída mostra os nomes de todos os que fizeram a pesquisa.
