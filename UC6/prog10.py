for i in range(5):
    v = int(input("Digite um valor: "))
    v= v % 2
    if v % 2 == 0:
        print(f"Seu número {v} é par")
    else:
        print(f"Seu número {v} é ímpar")