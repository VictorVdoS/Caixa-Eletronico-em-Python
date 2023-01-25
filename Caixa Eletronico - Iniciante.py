# Caixa Eletronico logica
print('=' * 30)
print('{:^30}'. format('BANCO DINO'))
print('=' * 30)
saque = int(input('Digite o valor desejado para saque: '))

if 10 <= saque <= 2000:
    notas_duzentos = saque // 200
    saque = saque % 200

    notas_cem = saque // 100
    saque = saque % 100

    notas_cinquenta = saque // 50
    saque = saque % 50

    notas_vinte = saque // 20
    saque = saque % 20

    notas_dez = saque // 10
    saque = saque % 10

    notas_cinco = saque // 5
    saque = saque % 5

    notas_dois = saque // 2
    saque = saque % 2

    notas_um = saque // 1

    if notas_duzentos > 0:
        print(notas_duzentos, 'Notas de R$200')
    if notas_cem > 0:
        print(notas_cem, 'Notas de R$100')
    if notas_cinquenta > 0:
        print(notas_cinquenta, 'Notas de R$50')
    if notas_vinte > 0:
        print(notas_vinte, 'Notas de R$20')
    if notas_dez > 0:
        print(notas_dez, 'Notas de R$10')
    if notas_cinco > 0:
        print(notas_cinco, 'Notas de R$5')
    if notas_dois > 0:
        print(notas_dois, 'Notas de R$2')
    if notas_um > 0:
        print(notas_um, 'Notas de R$1')

else:
    print('Não é possível fazer o saque')

print('=' * 30)
print('Volte sempre ao BANCO DINO!')
