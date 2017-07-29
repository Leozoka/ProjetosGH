usuarios_banidos = ['Ana', 'Beatriz', 'Bruno', 'Gustavo']
usuarios = 'José'
if usuarios not in usuarios_banidos:
    print(usuarios.title() + ', você já pode enviar sua resposta agora.')

# Para saber se um valor não aparece em uma lista, você pode utilizar not in.
# Se não estiver na lista, Python retrona True e executa a mensagem desejada.
