#Talvez você deseje armazenar um conjunto de dicionários em uma lista ou uma lista como um valor em um dicionário, isso se chama aninhamento.
#Um dicionário tem espaço para tal variável, mas nõa tem espaço para armazenar sobre uma segunda variável.
#Uma maneira é criar uma lista e adicionar os dicionários dentro dela (como nesse exemplo). E assim quando imprimimos sai todas as informações.
jog1 = {'cor': 'vermelho', 'pontos': 8}
jog2 = {'cor': 'preto', 'pontos': 5}
jog3 = {'cor': 'azul', 'pontos': 10}
jogadores = [jog1, jog2, jog3]
for jogador in jogadores:
    print(jogador)
