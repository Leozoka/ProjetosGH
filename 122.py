frase = ('Diga algo e eu repito novamente: ')
frase += ("\nDigite 'sair' para encerrar o programa. ")
msg = True
while msg:
    mensagem = input(frase)
    if mensagem == 'sair':
        msg = False
    else:
        print(mensagem)
#Configuramos a variável ativa para True, enquanto a variável True permanecer ativa o loop continuará.
#Na instrução if dentro do loop while, verificamos o valor da mensagem que o usuário digita, caso digite 'sair' Python reconhecerá False.
#Este exercicío tem o mesmo resultado do exercicío anterior, mas temos que indicar se o programa está em estado ativo.