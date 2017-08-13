def animal(animal_tipo, animal_nome):
    print('Eu tenho um ' + animal_tipo + '.')
    print('Meu ' + animal_tipo +  (' se chama ' + animal_nome. title() + '.'))
animal('espinafre', 'cachorro')
#Listamos o nome primeiro e depois o tipo de animal.
#O argumento de nome ficou armazenado no tipo de animal, fazendo com que quando mostramos o resultado, ele saia ao contrário.
#Para voltar ao normal, basta inverter o nome e o tipo de animal.