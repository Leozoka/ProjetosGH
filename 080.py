idade = 12
if idade < 4:
    print('Não paga nada para entrar no parque.')
elif idade < 18:
    print('Pagará R$ 5,00 para entrar no parque.')
else:
    print('Pagará R$ 10,00 para entrar no parque.')

# As vezes precisará testar mais de duas situações possíveis e avaliar, pode usar a sintaxe if-elif-else.
# Python executa apenas um na sintaxe if-elif-else. Executa cada Teste Condicional em ordem até um passar.
# Quando um teste passa, o código que segue esse teste é executado e Python ignora o resto dos testes.