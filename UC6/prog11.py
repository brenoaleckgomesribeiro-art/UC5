valores = []

for i in range(5):
    v = int(input("Digite um valor: "))
    valores.append(v)

for v in valores:
    if v % 2 == 0:
        print(f"Seu número {v} é par")
    else:
        print(f"Seu número {v} é ímpar")