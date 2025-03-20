menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saldo_extrato = 0
saque_extrato = 0
saldo_final = 0

while True:

    opcao = input(menu)
 
    if opcao == "d":

        valor_depositado = int(input("insira o valor que você quer depositar\n"))
       #se o valor for menos que 0, manda de volta para o menu, caso o contrário, atualiza e printa saldo
        if valor_depositado < 0:
          print(f'insira um valor positivo.')  

        else:
         saldo += valor_depositado
         saldo_extrato =+ saldo
         print(f'Seu saldo agora é R${saldo},00 Reais')

    elif opcao == "s":
        saque = int(input("insira o valor que você quer sacar\n"))
        #Caso o saque não seja negativo, maior que 500 ou maior que o saldo ele continua o saque
        if (saque < 0) or (saque >500):
           print("Valor inválido, tente novamente ")
        elif saque > saldo:
           print("Seu saque é maior que seu saldo! Deposite primeiro!")
        else:
 #Caso o numero de saques seja igual o limite, restringe o usuario e incrementa o valor do numero de saques para o extrato 
          if numero_saques == LIMITE_SAQUES:
           print(f"Você alcançou o limite de {numero_saques} saques diários ")
          else:
           saldo = saldo - saque
           numero_saques += 1
           saque_extrato += saque
           saldo_final = saldo
           print(f'Depois de seu saque de R${saque},00 Reais Seu saldo atual é de R${saldo},00 Reais!')
              
    elif opcao == "e":
        #puxa as informações coletadas
        if saldo_final == 0:
         print(f"Você depositou R${saldo_extrato},00 e depois sacou R${saque_extrato},00, ficando com um total de {saldo_extrato}")
        else:
          print(f"Você depositou R${saldo_extrato},00 e depois sacou R${saque_extrato},00, ficando com um total de {saldo_final}") 
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print("Obrigado por usar nosso sistema bancário!")
