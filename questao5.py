def temperatura(celcius):
   return (celcius * (9/5)) + 32

c = float(input())
resultado = temperatura(c)
print(f'{resultado:.2f}')
