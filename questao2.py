# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: 
# 	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


fibo = [0,1]
i = 0
num = input('Insira um número inteiro para saber se este está contido nos primeiros 20 números da sequência de Fibonacci: \n')

try:
    num = int(num)
    if (num < 0):
        print('Nenhum número negativo faz parte da sequência de fibonacci')
    else:
        for i in range(21):
                fibo.append(fibo[i] + fibo[i+1])
        if num in fibo:
            print('Na mosca! O número digitado é um dos 20 primeiros números de Fibonacci')
        else:
            print('O número digitado não está contido nos primeiros 20 números de Fibonacci.')
        print(fibo)
except Exception as erro:
    print('Entrada inválida')