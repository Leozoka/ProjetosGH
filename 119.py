num = int(input('Digite um número para saber se ele é ou não divisível por 5: '))
if num % 5 == 0:
    print('Este número é divisível por 5.')
else:
    print('Este número não é divisível por 5.')
#Quando um número é divisível por outro, o restante é 0 (zero), então o operador do módulo retorna 0.
#Os números divisíveis por 5 sempre terminam com 0 ou 5, o módulo reconhece e retorna que ele é um número divisível, caso contrário ele não é.
