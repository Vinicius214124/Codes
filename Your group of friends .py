sexo = input("Digite o seu sexo (Feminino/Masculino): ")
 
if sexo == 'feminino':
    num_mulheres = int(input("Digite quantas Mulheres tem no grupo: "))
 
    alturas_mulheres = [float(input("Digite a altura de cada Mulher: ")) for _ in range(num_mulheres)]
 
    media_altura_mulheres = sum(alturas_mulheres) / num_mulheres
 
    print(f"A média de altura das mulheres do grupo é: {media_altura_mulheres:.2f} metros")
 
 
elif sexo in ['masculino', 'm']:
 
    num_homens = int(input("Digite quantos Homens tem no grupo: "))
 
    alturas_homens = [float(input("Digite a altura de cada Homem: ")) for _ in range(num_homens)]
 
    media_altura_homens = sum(alturas_homens) / num_homens
 
    print(f"A média de altura dos homens do grupo é: {media_altura_homens:.2f} metros")
 
 
else:
   
     print("Te espero na próxima")