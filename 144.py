def fazendo_pizza(tamanhos, *coberturas):
    print("\nFazendo uma pizza de " + str(tamanhos) + " polegadas, com as seguintes coberturas:")
    for cobertura in coberturas:
        print("--" + cobertura)
fazendo_pizza(15, 'Queijo', 'Catupiry')
fazendo_pizza(20, 'Presunto e Mussarela', 'Chocolate')
#Na definição da função, o Python armazena o primeiro valor que recebe no tamanho do parâmetro. Os outros valores que seguem são armazenados nas caoberturas de tuplas.]
#As chamadas da função incluem um argumento para o tamanho primeiro, seguido das coberturas.
#Cada pizza tem um tamanho e um número de coberturas, e cada informação é impressa no lugar apropriad.