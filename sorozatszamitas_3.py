# sorozatszamitas f3
# n = 3 => 14; n = 4 = 30; n = 5 => 25;

k = int(input('K értéke: '))
sum = 0
for i in range(1, k + 1):
    sum += pow(i, 2)
    # sum += i * i
print(f'{k} egymást követő szám négyzetének összege: {sum}')