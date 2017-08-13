#Podemos chamar uma função quantas vezes for necessário.
#Podemos descrever mais um animal, e Python combina cada parâmetro.
#Sempre que quiser pode usar a função e colocar as novas informações.
def animal(animal_tipo, animal_nome):
    print('\nTenho um ' + animal_tipo.title() + '.')
    print('Meu ' + animal_tipo.title() + ', se chama ' + animal_nome.title() + '.')
animal('gato', 'epaminondas')
animal('cachorro', 'dougras')
