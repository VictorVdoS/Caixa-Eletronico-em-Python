# Caixa Eletronico While
print('=' * 30)
print('{:^30}'. format('BANCO DINO'))
print('=' * 30)
saque = int(input('Digite o valor desejado para saque: '))
total = saque
nota = 200
totalnota = 0


while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota == 0:
            print('Não é possível sacar cédulas de R$0,00')
        if totalnota > 0:
            print(f'Total de {totalnota} cédulas de R${nota}')
        if nota == 200:
            nota = 100
        elif nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        elif nota == 2:
            nota = 1
        totalnota = 0
        if total == 0:
            break


print('=' * 30)
print('Volte sempre ao BANCO DINO!')
