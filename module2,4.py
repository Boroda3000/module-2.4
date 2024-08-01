numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers) +1):
    if i == 1:
        continue
    elif i % 1 == 0 and i % 2 == 0 and i != 2:
        not_primes += [i]
    elif i % 1 == 0 and i % 3 == 0 and i != 3:
        not_primes += [i]
    else:
        primes += [i]
print('Primes:', primes)
print('Not primes:', not_primes)