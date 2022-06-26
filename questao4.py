# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# 	SP – R$67.836,43
# 	RJ – R$36.678,66
# 	MG – R$29.229,88
# 	ES – R$27.165,48
# 	Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

soma = sp + rj + mg + es + outros

sp_percent = round((sp/soma)*100, 2)
rj_percent = round((rj/soma)*100, 2)
mg_percent = round((mg/soma)*100, 2)
es_percent = round((es/soma)*100, 2)
outros_percent = round((outros/soma)*100, 2)

print('Percentual SP:',sp_percent,'%')
print('Percentual RJ:',rj_percent,'%')
print('Percentual MG:',mg_percent,'%')
print('Percentual ES:',es_percent,'%')
print('Percentual Outros:',outros_percent,'%')