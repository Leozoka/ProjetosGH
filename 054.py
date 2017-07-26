fruits = ['apple', 'avocado', 'blueberries']
friends = fruits[:]
fruits.append('grapes')
friends.append('cherries')
print('Minhas frutas preferidas: ')
for fruit in fruits:
    print(fruit.title())
print('\nFrutas preferidas dos meus amigos: ')
for friend in friends:
    print(friend.title())
