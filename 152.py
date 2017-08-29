class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odômetro = 25
    def descrição_carro(self):
        descrição = self.marca + ' ' + self.modelo + ' ' + str(self.ano)
        return descrição.title()
    def odômetro_km1(self):
        print('Este carro já andou ' + str(self.odômetro) + ' KM.')
    def odômetro_atu(self, km):
        if km >= self.odômetro:
            self.odômetro = km
        else:
            print('Você não pode reverter o odômetro')
carro1 = Carro('hyundai', 'hb20', 2012)
print(carro1.descrição_carro())
carro1.odômetro_km1()
carro1.odômetro_atu(23)
#Ampliamos o método para fazer trabalhos adicionais sempre que a leitura do odômetro é modificada.
#Agora odômetro_atu() verifica se a nova leitura faz sentido antes de modificar o atributo. Se a nova quilometragem,for superior ou igual à quilometragem existente, você pode atualizar a leitura do odômetro para a nova quilometragem.
#Caso for menor do que a quilometragem existente, você receberá um aviso de que não pode reverter o odômetro.