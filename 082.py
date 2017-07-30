idade = 65
if idade < 4:
    price = 0
elif idade < 18:
    price = 5
elif idade < 65:
    price = 10
else:
    price = 5
print('Sua admissão é de R$' + str(price) + '.')

# Pode usar tantos elif quiser em seu código. Neste exemplo implementamos um desconto para idosos.
# A maior parte do código é inalterada.
