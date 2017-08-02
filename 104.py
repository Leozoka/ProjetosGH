#Você pode usar a função sorted() para obter uma cópia das chaves em ordem.
pesquisa = {
    'leo': 'python',
    'pablo': 'c',
    'diogo': 'java',
    'bruno': 'php'
    }
for nome in sorted(pesquisa.keys()):
    print(nome.title() + ', obrigado pela pesquisa.')
#Quando colocamos a função sorted() em torno da função keys(), informa a Python para listar todas as chaves e classificar a lista.
#A saída mostra os nomes em ordem.