
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))


if numero1 == numero2 == numero3:
    print("Todos os números são iguais.")
else:
    
    if numero1 >= numero2 and numero1 >= numero3:
        maior = numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        maior = numero2
    else:
        maior = numero3

    if numero1 <= numero2 and numero1 <= numero3:
        menor = numero1
    elif numero2 <= numero1 and numero2 <= numero3:
        menor = numero2
    else:
        menor = numero3

    print("O maior número é " + str(maior) + ".")
    print("O menor número é " + str(menor) + ".")

    
    if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        print("Há números iguais.")
