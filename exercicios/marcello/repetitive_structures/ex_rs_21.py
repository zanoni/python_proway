val_tot = 0
val_arr = []

for i in range(15):
    val = float(input('Preço do produto {}: ' .format(i + 1)))
    val_tot += val
    val_arr.append(val)

val_arr.sort()
val_arr.reverse()

med = val_tot / 15

print('O maior preço é R${:.2f} e a média é R${:.2f}' .format(val_arr[0], med))
