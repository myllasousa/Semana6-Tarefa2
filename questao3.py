def preco(maca, banana):
   return (3 * maca) + (2 * banana)

m = float(input())
b = float(input())
preco_total = preco(m, b)
print(f'{preco_total:.2f}')
