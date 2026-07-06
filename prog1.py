valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
print("-- Escolha a operação ---")
print('("1 -Somar ")')
print('("1 - Subtrair ")')
print('("3 - Multiplicar ")')
print('("4 - Dividir")')
o= input("Digite sua operação: ")
match o:
    case "1":
        o = valor1 + valor2
    case "2":
        o = valor1 - valor2
    case "3":
        o = valor1 * valor2
    case "4":
        o = valor1 / valor2
    case _:
        o=0
        print("Opeção inválida")
print(f"O resultado da operação é {o}")