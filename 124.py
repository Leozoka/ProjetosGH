#Ao invés de sair de um loop sem executar o resto do seu código, você pode usar a instrução continue para retornar ao início do loop com base no resultado de um teste condicional.
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)
#Dentro do loop while incrementamos a contagem += 1, a instrução if verifica se o módulo é zero (contador é divisível por 2).
#A instrução continue diz a Python que ignore o resto do loop e retorna para o início. Se o número atual não for divisível por 2, o resto do loop é executado.