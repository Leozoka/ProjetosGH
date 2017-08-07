'''idade = input('Qual é sua idade? ')
print(idade >= 20)'''

idade = int(input('Qual é sua idade? '))
print(idade >= 20)
#Quando você tenta usar a entrada para fazer uma comparação numérica, Python produz um erro porque não pode comparar uma string com um número inteiro.
#POdemos usar a função int() que informa ao Python para tratar a entrada como um valor numérico.
#int() converte uma sequência de caracteres de um número para uma representação numérica, mostrado neste exemplo.
