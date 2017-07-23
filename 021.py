mesa = ['Maria', 'João', 'José']
print(mesa)
expul = mesa.pop(2)
print('Pedimos pra que você se retire ' + expul.title() + ', pois você não pagou a conta.')
print(mesa)

msg1 = ('Maria e João avistam Léo e perguntam se ele deseja se juntar a mesa.')
msg2 = ('Ele aceita.')
mesa.append('Léo')
print(msg1)
print(msg2)
print(mesa)

expul2 = mesa.pop(0)
print('Depois de um tempo Maria retirou-se.')
print(mesa)
