#Para sair de uma loop while, basta usar a função break.
frase = ('Gostaria de visitar qual lugar? ')
frase += "\n(Digite 'sair' para encerrar o programa.) "
while True:
    cidade = input(frase)
    if cidade == 'sair':
        break
    else:
        print('Eu gostaria de visitar, ' + cidade.title() + '!')
#O loop nesse programa contiua perguntando a cidade até o usuário digitar 'sair'.
#Quando digitam 'sair', a função de interrupção é exxecutada, fazendo com o que saia do loop.