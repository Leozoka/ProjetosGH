ingredientes = ['queijo', 'milho', 'tomate']
if 'queijo' in ingredientes:
    print('Queijo adicionado.')
elif 'milho' in ingredientes:
    print('Milho adicionado.')
elif 'tomate' in ingredientes:
    print('Tomate adicionado.')
print('\nIngredientes para a pizza finalizados!')

# Este código não funcionaria corretamente se usássemos if-elif-else, porque o código deixaria de funcionar depois de um único teste passar.
# Neste caso o primeiro teste passou e Python não executa o nenhum teste além do primeiro teste que passa em if-elif-else.
# Se mais de um bloco de código precisar ser executado, use uma série de declarações if.
