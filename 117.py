altura = int(input('Sua altura em polegadas? '))
if altura >= 40:
    print('\nAltura aprovada para andar no park!')
else:
    print('\nVocê está abaixo do permitido para andar no park!')
#Nesse exemplo o programa comparou a altura porque o função int() coverte o valor da entrada em uma representação numérica antes da comparação ser feita.
#Sempre que for usar entrada numérica para cálculos ou comparações, se atente para utilizar a função int().
