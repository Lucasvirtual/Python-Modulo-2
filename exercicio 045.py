from random import choice
from time import sleep
print('\033[33m-=-\033[m' * 8)
print('VAMOS JOGAR JOKENPÔ?')
print('\033[36m-=-\033[m' * 8)
lista = 'PEDRA', 'PAPEL', 'TESOURA'
pc = choice(lista)
lista2 = ['ESSA FOI SORTE!', 'A PRÓXIMA EU GANHO!', 'ESSA FOI BOA!', 'AH NÃO! VAMOS DE NOVO!',
          'VOCÊ É MUITO BOM NISSO!']
pc3 = choice(lista2)
lista3 = ['HAHA!', 'ESSA FOI FÁCIL!', 'SOU MUITO BOM NESSE JOGUINHO!', 'QUE TAL NA PRÓXIMA?', 'JAJÁ DEIXO VOCÊ JOGAR!',
          'HEHE BOY!']
pc4 = choice(lista3)
sleep(2)
print('\033[33mJO..\033[m')
sleep(1)
print('\033[31mKEN..\033[m')
sleep(1)
print('\033[32mPÔ!!\033[m')
player = str(input('ESCOLHA PEDRA, PAPEL OU TESOURA! ')).strip().upper()
sleep(0.5)
print(' ')
print(f'\033[32m{player}\033[m', '\033[33mX\033[m', f'\033[31m{pc}\033[m')
sleep(0.5)
print(' ')
if player == lista[0] and pc == lista[0]:
    print('\033[33mEMPATE!\033m')
elif player == lista[0] and pc == lista[1]:
    print(f'\033[31mVOCÊ PERDEU! {pc4} TENTE NOVAMENTE!\033[m')
elif player == lista[0] and pc == lista[2]:
    print(f'\033[32mVOCÊ GANHOU! {pc3}\033[m')
elif player == lista[1] and pc == lista[0]:
    print(f'\033[32mVOCÊ GANHOU! {pc3}\033[m')
elif player == lista[1] and pc == lista[1]:
    print('\033[33mEMPATE!\033[m')
elif player == lista[1] and pc == lista[2]:
    print(f'\033[31mVOCÊ PERDEU! {pc4} TENTE NOVAMENTE!\033[m')
elif player == lista[2] and pc == lista[0]:
    print(f'\033[31mVOCÊ PERDEU! {pc4} TENTE NOVAMENTE!\033[m')
elif player == lista[2] and pc == lista[1]:
    print(f'\033[32mVOCÊ GANHOU! {pc3}\033[m')
elif player == lista[2] and pc == lista[2]:
    print('\033[33mEMPATE!\033[m')