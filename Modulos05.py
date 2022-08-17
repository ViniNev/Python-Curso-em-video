from random import choice
aluno1 = str(input('Qual nome do primeiro Aluno ? '))
aluno2 = str(input('Qual nome do segundo Aluno ? '))
aluno3 = str(input('Qual nome do terceiro Aluno ? '))
aluno4 = str(input('Qual nome do quarto Aluno? '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')

