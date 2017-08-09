frase = ('Diga algo e eu repito novamente: ')
frase += ("\nDigite 'sair' para encerrar o programa. ")
usuario = ''
while usuario != 'sair':
    usuario = input(frase)
    print(usuario)
#POdemos manter um programa em funcionamento, desde que o usuário não digite o valor da saída.
#Definimos ao usuário duas opções (inserir uma valor qualquer, ou o valor 'sair', para encerrar o programa).
#Depois definimos uma string vazia '', com isso na primeira vez que o programa é executado Python compara a mensagem digitada com o valor de saída.
