dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km rodou? '))
pago = (dias * 60) + (km * 0.15)
print(f'O valor que vai pagar eh? {pago} ')