numero1  = int(input("Digite o primeiro número: "))
numero2  = int(input("Digite o segundo número: "))

if(numero1 > numero2):
    maiorValor = numero1
    print("O maior número é o número: ",str(maiorValor))

elif(numero2 > numero1):
    maiorValor = numero2
    print("O maior número é o numero: ",str(maiorValor))

else:
    print("Os números são iguais")
