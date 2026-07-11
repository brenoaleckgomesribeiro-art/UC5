nome1 = input("Digite o nome do aluno 1: ")
for i in range(1):
    media1 =float(input("Digite as médias: "))
    media2 =float(input("Digite as médias: "))
    media3 =float(input("Digite as médias: "))
    mediafinal1 = (media1 + media2 + media3) / 3
    if mediafinal1 >= 7:
        print(f"{nome1} está aprovado")
    elif mediafinal1 == 5 or 6:
        print(f"{nome1} está de recuperação")
    else:
        print(f"{nome1} está reprovado")