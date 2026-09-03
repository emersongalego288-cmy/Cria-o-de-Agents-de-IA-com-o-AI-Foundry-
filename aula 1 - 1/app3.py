
print('SISTEMA DE NOTAS DE ALUNOS')


# cadastrar os alunos 
nome1 = input('Digite o nome do aluno 1:')
nome2 = input('Digite o nome do aluno 2:')
nome3 = input('Digite o nome do aluno 3:')


lista_nomes = []


# adicionar dentro da lista (append)
lista_nomes.append(nome1)
lista_nomes.append(nome2)
lista_nomes.append(nome3)


print(lista_nomes)


nota1 = float(input(f'Nota 1 -{nome1}'))
nota2 = float(input(f'Nota 2 -{nome2}'))
nota3 = float(input(f'Nota 3 -{nome3}'))


media  = (nota1 + nota2 + nota3) /3 


print('Medias dos alunos', round(media,2))

enter = input('Digite enter para sair')
