import math


# швидке дискретне потенціювання
def discrete_potentiation(s, k, p):
    bin_k = bin(k).replace('0b', '')
    e_i = 1
    for i in range(len(bin_k)):
        e_i = ((e_i ** 2) * (s ** int(bin_k[i]))) % p
    return e_i


s = int(input('Введіть повідомлення S (ціле число): '))
k = int(input('Введіть ключ шифрування K (ціле число): '))
p = int(input('Введіть параметр P (ціле число): '))

print('\nШифр E = ', discrete_potentiation(s, k, p), '\n')


# генератор великих простих чисел
def generating_large_primes(p_max, a):
    k = math.ceil(math.log(p_max / 2, a))
    p1 = 2 * (a ** k) + 1
    p2 = 2 * (a ** k) - 1
    if discrete_potentiation(2, p1 - 1, p1) == 1:
        p = p1
    if discrete_potentiation(2, p2 - 1, p2) == 1:
        p = p2
    else:
        while discrete_potentiation(2, p1 - 1, p1) != 1:
            p1 += 2
        p = p1
    return p


# перевірка числа на простоту
def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d


p_max = int(input('Введіть порядок числа P_max (ціле число): '))
a = int(input('Введіть мале просте число a (ціле число): '))
if IsPrime(a) == a:
    print('\nЗгенероване просте число P = ', generating_large_primes(p_max, a))
else:
    print("\nВведене значення 'a' не є простим числом. Спробуйте ввести інше значення.")
