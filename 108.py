bots = []
for bot in range(30):
    new_bots = {'cor': 'vermelho', 'pontuação': 10, 'velocidade': 'média'}
    bots.append(new_bots)

for bot in bots[:5]:
    print(bot)
print('...\n')
print('Número total de dicionários na lista: ' + str(len(bots)) + '.')
#Neste exemplo criamos uma lista vazia para armazenar todos os bots, usando range() informamos a quantidade de vezes que queremos que o loop se repita.
#Cada vez que o loop é executado criamos um bot novo. Usamos o fatiamento para imprimir os 5 primeiros, e em seguida imprimimos o comprimento da lista.
#Todos os bots tem a mesma características, mas Python considera cada um separado, assim podemos mudar suas características.
