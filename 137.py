def criando_um_nome(primeiro, segundo, terceiro=''):
    if terceiro:
        nome_completo = primeiro + ' ' + segundo + ' ' + terceiro
    else:
        nome_completo = primeiro + ' ' + segundo
    return nome_completo.title()
nome = criando_um_nome('leo', 'neves')
print(nome)
nome = criando_um_nome('fulano', 'de', 'tal')
print(nome)
#Para tornar alguma parte do nome opcional podemos dar o argumento com um padrão vazio e ignorar o argumento, a menos que fornecemos um valor.
#Para funcionar sem uma parte do nome definimos um padrão para o valor.
#Valores opcionais permitem que as funções muitos casos de usos, enquanto as chamadas de função permanecem tão simples quanto possiveis.