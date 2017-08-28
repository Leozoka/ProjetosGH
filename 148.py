class Cachorro():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def sentado(self):
        print(self.nome.title() + ' está sentado!')
    def toda_parte(self):
        print(self.nome.title() + ' está em toda parte!')
    def rolando(self):
        print(self.nome.title() + ' está rolando!')
p_dog = Cachorro('shifu', 8)
s_dog = Cachorro('rex', 5)
print('O primeiro cachorro se chama ' + p_dog.nome.title() + '.')
print('Tem ' + str(p_dog.idade) + ' anos.')
p_dog.sentado()
p_dog.toda_parte()
p_dog.rolando()

print('\nO segundo cachorro se chama ' + s_dog.nome.title() + '.')
print('Tem ' + str(s_dog.idade) + ' anos')
s_dog.sentado()
s_dog.toda_parte()
s_dog.rolando()
#O método __init__() é um método especial. O Python é executado automaticamente sempre que criamos uma nova instância baseada na classe Cachorro.
# O parâmetro self é necessário na definição do método, e deve vir primeiro antes dos outros parâmetros. Ele deve ser incluído na definição, porque quando Python chama esse método __init __ () mais tarde (para criar uma instância de Cachorro), a chamada do método passará automaticamente o próprio argumento.
#A classe Cachorro tem três outros métodos definidos: sentado(), toda_parte() e rolando(). Como esses métodos não precisam de informações adicionais como um nome ou idade, nós apenas os definimos para ter um parâmetro, self(auto).
