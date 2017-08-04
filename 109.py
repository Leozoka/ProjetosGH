bots = []
for bot in range(0,30):
    new_bots = {'cor': 'vermelho', 'pontuação': 10, 'velocidade': 'média'}
    bots.append(new_bots)

for bot in bots[:3]:
    if bot['cor'] == 'vermelho':
        bot['cor'] = 'preto'
        bot['pontuação'] = 15
        bot['velocidade'] = 'rápido'
for bot in bots[:5]:
    print(bot)
#Quando quisermos algo, podemos usar um loop for e if (nesse exemplo mudamos a cor dos 3 primeiros bots).
#Colocamos o fatiamento [:3] , porque mudamos somente os 3 primeiros.
#(POderiamos expandir adicionando um bloco elif).