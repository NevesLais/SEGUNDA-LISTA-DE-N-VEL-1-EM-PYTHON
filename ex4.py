salario = float(input("Digite o seu salário:\n"))

if salario <= 280:
    percentualAumento = 20
    aumento = (salario * percentualAumento) / 100
    novoSalario = salario + aumento

elif salario > 280 and salario <= 700:
    percentualAumento = 15
    aumento = (salario * percentualAumento) / 100
    novoSalario = salario + aumento

elif salario > 700 and salario <= 1500:
    percentualAumento = 10
    aumento = (salario * percentualAumento) / 100
    novoSalario = salario + aumento 

elif salario > 1500:
    percentualAumento = 5
    aumento = (salario * percentualAumento) / 100
    novoSalario = salario + aumento

print("Seu aumento foi de R$", aumento)
print("Seu novo salário é R$", novoSalario)
