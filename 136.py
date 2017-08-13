def formando_um_nome(primeiro, ultimo):
    nome_completo = primeiro + ' ' + ultimo
    return nome_completo.title()
nome = formando_um_nome('fulano', 'de tal')
print(nome)
#A definição formando_um_nome() leva como parâmetros um primeiro e último nome. Depois a função combina esses dois.
#Quando você usa uma função que retorna um valor, precisará fornecer uma varável onde o valor de retorno pode ser armazenado.
#Nesse caso ficou armazenado em nome, a saída mostra o nome completo.
