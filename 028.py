# Crie um Script qe tente acessar uma posição em sua lista, maior que os elementos que nela possui, vai ocorrer um erro, explique por que isso acontece.

'''
refri = ['pepsi', 'coca-cola', 'fanta']
print(refri[3])
'''

#Acontece esse erro, porque listas começam a contar do 0 (zero), ou seja, o item correto seria o número 2 (dois).
#Tendo em mente que o último item da lista pode ser localizado com [-1].

refri = ['pepsi', 'coca-cola', 'fanta']
print(refri[2])
