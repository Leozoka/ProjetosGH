#idade = 18
#msg = ('Parabéns,' + idade + ' anos!')
#Acontece esse erro porque o tipo string (str) não foi informado na variável
idade = int(18)
msg = ('Parabéns,' + str(idade) + ' anos!')
print(msg)
