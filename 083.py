idade = 66
if idade < 4:
    price = 0
elif idade < 18:
    price = 5
elif idade < 65:
    price = 10
elif idade >= 65:
    price = 5
print('Sua admissão é de R$' + str(price) + '.')
