conta = int(input('Número da conta: '))
saldo_in = float(input('Saldo: '))
debit = float(input('Débito: '))
credi = float(input('Crédito: '))

saldo_fn = saldo_in - debit + credi

print('Saldo atual de R${:.2f}' .format(saldo_fn))    

if saldo_fn >= 0:
    print('Saldo positivo')    
else :
    print('Saldo negativo')    


