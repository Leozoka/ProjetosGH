#Podemos armazenar o prompt em uma variável para a função input().
frase = 'Seja bem-vindo(a) em nosso site.'
frase += '\nInforme seu nome: '
nome = input(frase)
print('Olá, ' + nome + '!')
#Este exemplo permite criar várias linhas. A primeira linha armazena parte da mensagem.
#Na segunda linha o operador += leva a string que foi armazenada na variável e adiciona a nova linha no final.
