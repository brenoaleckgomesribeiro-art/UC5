carros ={}
for i in range(2):
    carro=input("Diite o seu carro: ")
    marca=input("Digita a marca: ")
    valor=float(input("Digite o valor: "))
    carros[carro] = {
    "MARCA" : marca,
    "VALOR" : valor
    }
print(f"Lista de carros {carros}")