class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def descrição_carro(self):
        descrição = self.marca + ' ' + self.modelo + ' ' + str(self.ano)
        return descrição.title()
carro1 = Carro('hyundai', 'hb20', 2012)
print(carro1.descrição_carro())
#Definimos o método __init __ () com o primeiro parâmetro Carro. Depois colocamos mais três parâmetros marca, modelo, ano.
#O método __init __ () aceita esses parâmetros e os armazena nos atributos que serão associados a instâncias feitas a partir desta classe.
#Quando fazemos uma nova instância de carro, precisamos especificar uma marca, modelo e ano para nossa instância.