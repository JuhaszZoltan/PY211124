# sorozatszamitas f2
# n = 3 => 6; n = 4 = 24; n = 5 => 120;

n = int(input('N értéke: '))
mult = 1
for i in range(1, n + 1):
    mult *= i
print(f'számok szorzata {n}ig: {mult}')