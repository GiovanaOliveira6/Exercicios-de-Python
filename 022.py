nota1 = float(input('Qual é a sua primeira nota? '))
nota2 = float(input('Qual é a sua segunda nota?'))
media = (nota1 + nota2) / 2 
print(f' O resultado eh: {media} ')

if media >= 6:
    print('A média foi otima')

else: 
    print('Esta precisando estudar mais...')