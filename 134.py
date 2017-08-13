def animal(animal_tipo, animal_nome):
    print('Eu tenho um ' + animal_tipo + '.')
    print('Meu ' + animal_tipo + ', se chama ' + animal_nome.title() + '.')
animal(animal_tipo='cachorro', animal_nome='fred')
#Quando chamamos a função desse modo informamos a Python para ele armazenar cada argumento no parâmetro correto.
#Assim evitando erros.