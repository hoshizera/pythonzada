from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
atual = date.today().year
conta = atual - ano
falta = (ano - atual) + 18 # PARA O TEMPO QUE FALTA SE ALISTAR
passo = (atual - ano) - 18 # TEMPO QUE PASSOU DO ALISTAMENTO
if conta < 18:
    print('Falta(m) {} ano(s) para você se alistar'.format(falta))
elif conta == 18:
    print('Está na hora de se alistar.')
elif conta > 18:
    print('A data de se alistar já expirou em {} ano(s)'.format(passo))
