respostas = {}
votacao = True
while votacao:
    nome = input('\nQual seu nome? ')
    resposta = input('Gostaria de escalar qual montanha? ')
    respostas[nome] = resposta
    novamente = input('Gostaria de responder novamente? (sim/não) ')
    if novamente == 'não':
        votacao = False
print('\nResultados:')
for nome, resposta in respostas.items():
    print(nome.title() + ' gostaria de o escalar ' + resposta.title() + '!')
#O primeiro programa define um dicionário vazio (respostas) e depois define a variável para True, para indicar que está ativo.
#Enquanto for verdadeiro, o Python executará o código no loop while. Dentro do loop, o usuário é solicitado a inserir seu nome de usuário e uma montanha que eles gostariam de escalar. Essa informação é armazenada no dicionário de respostas.
#E o usuário pergunta se você deseja ou não manter a enquete em execução, caso diga sim irá te perguntar novamente, se for não (False) mostrará os resultados.