from typing import final
 
print("Seja Bem Vindo, aqui voce podera ver quanto voce tera que gastar em seus bilhetes")
 
name = input("Por favor, digite o seu nome: ")
 
# Solicita o número de trechos do usuário
while True:
    try:
        trecho = int(input(f"{name.title()}, digite quantos transportes publicos voce usa na ida: "))
        dias = int(input(f"{name.title()}, digite a quantidade de dias que voce deseja para fazer o calculo:"))
        if trecho > 0:
            break
        else:
            print("Por favor, digite um número válido de trechos.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
 
print("Lembre-se que ao colocar o valor, utilize um ponto (.) como separador decimal.")
 
# Calcula o valor total das passagens
total = 0
for i in range(trecho):
    passagem = float(input("Digite o valor da sua passagem:"))
    total += passagem * 2
 
print("O valor que voce ira pagar no dia ida e volta é: %.2f" % total)
 
VLNMS = total * dias
print("Voce tera que colocar ao todo em todos bilhetes o valor de: %.2f" % VLNMS)
 
VECBLT = VLNMS / 2
print("Voce tera que colocar no BenFácil: %.2f" % VECBLT)
 
MNOS = VLNMS - VECBLT
print("Voce tera que colocar no Bilhete Único: %.2f" % MNOS)
 
resposta = input("Você ja tem algum saldo em seu bilhete? (sim/não): ").lower()
 
if resposta in ["sim", "yes","YES", "SIM"]:
    print("Ótimo! Continuando...")
    saldo_conta = float(input("Digite o saldo que voce tem em seu bilhete:"))
    saldo_new = VLNMS - saldo_conta
    saldo_newU = MNOS - saldo_conta
    saldo_newF = VECBLT - saldo_conta
    print("Nesse caso você terá que colocar o valor de: %.2f" % saldo_new)
    print("O seu bilhete Único ficará com o valor de: %.2f" % saldo_newU)
    print("O seu BenFácil ficará com o valor de: %.2f" % saldo_newF)
 
elif resposta in ["não", "no", "NAO","nao","NO",'NÃO']:
    print("Ok, obrigado por usar o meu programa!")
 
print("Espero ter te ajudado, até a proxima")
 
print("Criador do programa: Vinicius Alves")
 
print("Para:", name.title())