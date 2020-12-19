#Programa desenvolvido por Lidiane Mel Loureiro em 2020

#EXERCICIO: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro.
#O usuário deve informar de qual número ele deseja ver a tabuada.

print("Escolha um número: ") #Usuário escolhe o número
Num = int(input())
cont = 0
result = 0
print("\n Tabuada do Número",Num)
while (cont < 10): #Repetição para gerar a tabuada
    result = result + Num #Conta para cada resultado da tabuada
    #print(result)
    cont = cont + 1
    print(Num, "X ",cont, "= ",result) #Exibindo o resultado para o usuário
print("Fim da Tabuada!")