cober_disps = ['pimentão', 'calabresa', 'queijo extra', 'bacon', 'milho']
cober_peds = ['queijo extra', 'chocolate', 'milho']
for cober_ped in cober_peds:
    if cober_ped in cober_disps:
        print('Adicionando ' + cober_ped + '.')
    else:
        print('Não temos ' + cober_ped + ' no momento.')
print('\nPizza pronta.')
