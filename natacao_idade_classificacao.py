from datetime import date
ano = int(input('Digite sua data de nascimento: '))
atual = date.today().year
if atual - ano >= 1 and atual - ano <=9:
    print('Você se encaixa como MIRIM')
elif atual - ano > 9 and atual - ano <=14:
    print('Você se encaixa como INFANTIL')
elif atual - ano >14 and atual - ano <=19:
    print('Você se encaixa como JUNIOR')
elif atual - ano >19 and atual - ano <=20:
    print('Você se encaixa como SENIOR')
elif atual - ano >20:
    print('Você se encaixa como MASTER')