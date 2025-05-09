nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segundaa nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) /4
print(media)

if(media >= 70):
    print("Você foi aprovado!")

elif(media >=50 and media <=69):
    print("Você está de recuperação!")

else:
    print("Você está reprovado")
