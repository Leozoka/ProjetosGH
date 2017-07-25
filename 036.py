jogadores = ['Ana', 'Beatriz', 'Eduardo']
'''for jogador in jogadores:
    print(jogador.title() + ', foi um bom jogo!')
    print('Vamos nos ver no próximo jogo, ' + jogador.title() + '.\n')
    
    print('Obrigado pelo jogo!')'''
#Esse problema pode ocorrer quando recuamos o código acidentalmente, para voltar ao normal basta deixar os mesmo número de espaços para cada string ou não pular uma string.

#Arrumado:
for jogador in jogadores:
    print(jogador.title() + ', foi um bom jogo!')
    print('Vamos nos ver no próximo jogo, ' + jogador.title() + '.')
    print('Obrigado pelo jogo!\n')
