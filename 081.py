idade = 12
if idade < 12:
    price = 0
elif idade < 18:
    price = 5
else:
    price = 10
print('Sua admissão é de R$' + str(price) + '.')

# Em vez de imprimir o preço de entrada dentro do if-elif-else, seria conciso definir apenas o preço de if-elif-else.
# O propósito da cadeia if-elif-else é mais estreito. Em vez de determinar um preço e uma mensagem, ele simplesmente determina o preço de admissão.
# É mais eficiente, e mais fácil de modificar. Fizemos apenas um declaração ao invés de três separadas.
