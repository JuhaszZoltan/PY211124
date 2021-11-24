# sorozatszamitas f1
# n = 3 => 6; n = 4 = 10; n = 6 => 21;

n = int(input('N értéke: '))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"számok összege {n}ig: {sum}")
