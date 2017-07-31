game = {'posição_a': 1, 'posição_b': 31, 'velocidade': 'rápido'}
print('Posição inicial: ' + str(game['posição_a']) + '.')
if game['velocidade'] == 'lento':
    a_incremento = 1
elif game['velocidade'] == 'médio':
    a_incremento = 5
else:
    a_incremento = 10
game['posição_a'] = game['posição_a'] + a_incremento
print('Nova posição é: ' + str(game['posição_a']) + '.')

# Armazenamos um valor que representa a velocidade atual do personagem, e em seguida usamos para determinar sua velocidade.
# Utilizamos if-elif-else para ver até que ponto o personagem se move, de acordo com a velocidade que colocamos o personagem pode andar várias casas.
# Ao alterar um valor no dicionário, você pode mudar o comportamento geral do personagem, o if-elif-else atribui um valor para a nova posição.
# A nova posição é a posição antiga mais o incremento.
