animais = ['peixe', 'pato', 'arara', 'peixe', 'tartaruga', 'peixe']
print(animais)
while 'peixe' in animais:
    animais.remove('peixe')
print(animais)
#Tinhamos uma lista com a palavra 'peixe' repetida várias vezes.
#Depois que Python entra no loop while, ele remove cada instância 'peixe' até que o valor não esteja na lista.
#Depois sai do loop e imprime a lista.