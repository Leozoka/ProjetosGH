def fazendo_pizza(*coberturas):
    print(coberturas)
fazendo_pizza('queijo')
fazendo_pizza('presunto e mussarela', 'chocolate')
#O asterisco no parâmetro diz a Python para fazer uma tupla vazia chama coberturas e colocar os valores que ela recebe nessa tupla.
#A impressão no corpo da função produz a saída mostrando qe o Python pode lidar com uma chamada de função com um valor e uma chamada com três valores.
#Fica em uma tupla, mesmo so com um valor.