def fazendo_pizza(tamanhos, *coberturas):
    print('\nFazendo uma pizza de ' + str(tamanhos) + ' polegadas, com as seguintes coberturas:')
    for cobertura in coberturas:
        print('--' + cobertura)