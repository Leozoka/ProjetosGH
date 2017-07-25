jogadores = ['Ana', 'Beatriz', 'Eduardo']
for jogador in jogadores:
    print(jogador.title() + ', foi um bom jogo!')
print('Vamos nos ver no próximos jogo, ' + jogador.title() + '.')

#É um erro lógico. Python reconheceu a linha recuada depois do comando for, o primeiro print está com o espaço, já no segundo não tem o espaço, isso faz com que o loop pare de funcionar.
