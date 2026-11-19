alunos = []


def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media


def classificar_aluno(media):
    if media >= 7:
        return 'aluno aprovado'
    elif media >= 5:
        return 'aluno de recuperação'
    else:
        return 'reprovado'


while True:

 nome = input("Digite o nome do aluno ou (sair): ")

 if nome.lower() == 'sair':
   break

 notas = []

 for i in range(3):
  while True:
    try:
      nota = float(input(f"Digite a {i + 1}ª nota: "))
      notas.append(nota)
      break

    except ValueError:
     print("Número inválido! Digite novamente.")


 aluno = {
    "nome": nome,
    "notas": notas
 }

 alunos.append(aluno)
 print('aluno cadastrado!')

 print("\nAlunos cadastrados:")

 print("\n===== ALUNOS CADASTRADOS =====")

for aluno in alunos:
    media = calcular_media(aluno["notas"])
    situacao = classificar_aluno(media)

    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Media: {media:.2f}")
    print(f"situacão: {situacao}")

print(len(alunos))

def pesquisar(nome):

    for aluno in alunos:
     if nome.lower() == aluno['nome'].lower():
         return  aluno

    return None





