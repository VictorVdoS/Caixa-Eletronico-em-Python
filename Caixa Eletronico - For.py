# Caixa Eletronico For
print('=' * 30)
print('{:^30}'. format('BANCO DINO'))
print('=' * 30)
valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [200, 100, 50, 20, 10, 5, 2, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')
    else:
        print('Não é possível sacar cédulas de R$0,00')
print('=' * 30)
print('Volte sempre ao BANCO DINO!')
