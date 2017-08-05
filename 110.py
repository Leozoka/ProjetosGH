#As vezes é útil colocar uma lista dentro de um dicionário.
pizza = {
    'tamanho': 'médio',
    'coberturas': ['chocolate', 'pepperoni']
    }
print('Vocês pediram uma pizza de tamanho ' + pizza['tamanho'] + ', com as seguintes coberturas:')
for cobertura in pizza['coberturas']:
    print('\t' + cobertura.title())
#Criamos um dicionário que tem uma pizza encomendada, uma chave é o tamanho e outra é de coberturas.
#Fazemos um loop para imprimir as coberturas da lista e assim a pizza fica pronta.