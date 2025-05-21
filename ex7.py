a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))


if a == b and b == c:
    print("Triângulo Equilátero")
elif a == b or b == c or a == c:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")
