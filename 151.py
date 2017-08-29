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
carro1.odômetro = 23
carro1.odômetro_km()
#A maneira mais simples de modificar o valor de um atributo é acessar o atributo diretamente através de uma instância.
#Estabelecemos a leitura do odômetro para 23 diretamente, assim quando executar o programa já mostrará a quantidade de km rodado pelo o carro.