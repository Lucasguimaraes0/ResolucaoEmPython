# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# 	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# 	b) Evite usar funções prontas, como, por exemplo, reverse;

string = 'Aprovado'
tamanho = len(string)
invertida = []
while tamanho > 0:
    invertida += string[tamanho -1]
    tamanho = tamanho -1
    
print(invertida)