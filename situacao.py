# Autor: Thiago.
def situacao(m):
    if media >= 60:
        print('Aprovado')
    elif media <= 50:
        print('Em recuperação')
    elif media < 50:
        print('Reprovado')