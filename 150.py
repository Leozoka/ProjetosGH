class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odômetro = 0
    def descrição_carro(self):
        descrição = self.marca + ' ' + self.modelo + ' ' + str(self.ano)
        return descrição.title()
    def odômetro_km(self):
        print('Este carro já andou ' + str(self.odômetro) + ' KM.')
carro1 = Carro('hyundai', 'hb20', 2012)
print(carro1.descrição_carro())
carro1.odômetro_km()
#Cada atributo em uma classe precisa de um valor inicial, mesmo que esse valor seja 0 ou uma string vazia.
#Em alguns casos quando se configura um valor padrão, faz sentido especificar esse valor inicial no corpo do método __init __ ().
#Se você fizer isso por um atributo, não é necessário incluir um parâmetro para esse atributo.
#Quando Python chama o método __init __ () para criar uma nova instância, ele armazena os valores de marca, modelo e ano como atributos.