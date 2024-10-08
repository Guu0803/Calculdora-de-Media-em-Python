#Calculadora de Média
i = 1
#criando lista para armazenar as notas do aluno
notas_do_aluno = []
#while usado para adicionar quantas notas forem necessárias
while i == 1:
  #pegando e armazenando nota digitada pelo usuário
  nota = int(input("Digite a nota do aluno:"))
  #adicionando a nota a lista de notas do aluno
  notas_do_aluno.append(nota)
  #perguntando se deseja adicionar outra nota ou interromper o loop
  nova_nota = input("Deseja adicionar outra nota? S ou N")
  nova_nota = nova_nota.upper()
  #verificando se o valor digitado é válido
  if(nova_nota != "N" and nova_nota != "S"):
    print("Resposta inválida")
    break
  elif(nova_nota == "S"): continue
  else:
    print(f"Notas do aluno: {notas_do_aluno}")
    soma_notas = sum(notas_do_aluno) #somando todas as notas no array
    media  = soma_notas / len(notas_do_aluno) #calculando a média
    print(f"Media do aluno: {media}")
    #verificando a situação do aluno
    if media < 7: print("Situação: Aluno Reprovado")
    else: print("Situação: Aluno Aprovado")
    break