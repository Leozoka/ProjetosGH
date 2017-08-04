linguagens = {
    'leo': 'python',
    'pablo': 'c#',
    'eduardo': 'java',
    'gustavo': 'c#',
    }
print('Linguagens mencionadas:')
for linguagem in set(linguagens.values()):
    print(linguagem.title())
#Quando se envolve set() ao redor de uma lista que contém itens duplicados, Python identifica os itens exclusivos nessa lista e cria um conjunto desses itens.
#O resultado são as linguagens preferidas, mas sem repetições.