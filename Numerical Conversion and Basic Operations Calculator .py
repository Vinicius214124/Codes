print("Calculadora de Conversão Numérica e de Operações Basicas")
while True:
    print("\n Escolha a operação:")
    print("1. Binário para Decimal")
    print("2. Hexadecimal para Decimal")
    print("3. Octal para Decimal")
    print("4. Decimal para Binário")
    print("5. Decimal para Hexadecimal")
    print("6. Decimal para Octal")
    print("7. multiplicação")
    print("8. Potenciação")
    print("9. Subtração")
    print("10. Divisão")
    print("11. Soma")
    print("12. Divisão Inteira")
    print("13. Resto da Divisão")
    print("14. Arredondar o Valor da conta")
    print("0. Sair")
    escolha = input(f"Digite o número da operação desejada: ")
 
    if escolha == '1':
        numero = input("Digite o Binario:")
        print("Resultado:", int(numero, 2))
       
    elif escolha == '2':
        numero = input("Digite o Hexadecimal:")
        print("Resultado", int(numero, 16))
 
    elif escolha == '3':
        numero = (input("Digite o Octal:"))
        print("Resultado:", int(numero, 8))
 
    elif escolha =='4':
        numero = int(input("Digite o Decimal:"))
        print("Resultado", bin(numero))
 
    elif escolha =='5':
        numero = int(input("Digite o Decimal:"))
        print("Resultado", hex(numero))
 
    elif escolha == '6':
        numero = int(input("Digite o Decimal:"))
        print("Resultado", oct(numero))
 
    elif escolha == '7':
        numero = float(input("Digite o seu primeiro numero da Multiplicação:"))
        numero1 = float(input("Digite o seu segundo numero da Multiplicação:"))
        resultado = numero * numero1
        print(f"A resposta é {resultado: .2f}")
   
    elif escolha == '8':
        numero = float(input("Digite o seu primeiro numero da Potenciação:"))
        numero1 = float(input("Digite o seu segundo numero da Potenciação:"))
        resultado = numero ** numero1
        print(f"A resposta é {resultado: .2f}")
   
    elif escolha =='9':
        numero = float(input("Digite o seu primeiro numero da Subtração:"))
        numero1 = float(input("Digite o seu segundo numero da Subtração:"))
        resultado = numero - numero1
        print(f"A resposta é {resultado: .2f}")
 
    elif escolha == '10':
        numero = float(input("Digite o seu primeiro numero da Divisão:"))
        numero1 = float(input("Digite o seu segundo numero da Divisão:"))
        resultado = numero / numero1
        print(f"A resposta é {resultado: .2f}")
   
    elif escolha == '11':
        numero = float(input("Digite o seu primeiro numero da Soma:"))
        numero1 = float(input("Digite o seu segundo numero da Soma:"))
        resultado = numero + numero1
        print(f"A resposta é {resultado: .2f}")
 
    elif escolha == '12':
        numero = float(input("Digite o seu primeiro numero da Divisão Inteira:"))
        numero1 = float(input("Digite o seu segundo numero da Divisão Inteira:"))
        resultado = numero // numero1
        print(f"A resposta é {resultado: .2f}")
   
    elif escolha == '13':
        numero = float(input("Digite o seu primeiro numero do Resto da Divisão:"))
        numero1 = float(input("Digite o seu segundo numero do Resto da Divisão:"))
        resultado = numero % numero1
        print(f"A resposta é {resultado: .2f}")
 
    elif escolha == '0':
        print("Se precisar de mais ajuda pode contar conosco!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")