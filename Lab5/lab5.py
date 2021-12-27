import math
import random


# швидке дискретне потенціювання
def discrete_potentiation(s, k, p):
    bin_k = bin(k).replace('0b', '')
    e_i = 1
    for i in range(len(bin_k)):
        e_i = ((e_i ** 2) * (s ** int(bin_k[i]))) % p
    return e_i


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
q_max = int(input('Введіть порядок числа Q_max (ціле число): '))
a = int(input('Введіть мале просте число a (ціле число): '))
if IsPrime(a) != a:
    print("\nВведене значення 'a' не є простим числом. Спробуйте ввести інше значення.")
else:
    p = generating_large_primes(p_max, a)
    q = generating_large_primes(q_max, a)
    print('\nЗгенероване просте число P = ', p)
    print('Згенероване просте число Q = ', q)

    encryption_parameter = p * q
    Euler_function = (p - 1) * (q - 1)

    public_key = random.randint(int(math.log(encryption_parameter, 2)), 1000000000)
    while math.gcd(public_key, Euler_function) != 1:
        public_key = random.randint(int(math.log(encryption_parameter, 2)), 1000000000)

    z = 1
    secret_key = z * Euler_function + 1
    while secret_key % public_key != 0:
        z += 1
        secret_key = z * Euler_function + 1
    secret_key /= public_key

    print('Ключі шифрування для RSA-системи задаються парами:\n<Кс, Р> - секретний ключ <{0}, {2}>\n'
          '<Ко, Р> - відкритий ключ <{1}, {2}>'.format(int(secret_key), public_key, encryption_parameter))

    s = int(input('Введіть повідомлення S (ціле число): '))
    e = discrete_potentiation(s, int(public_key), encryption_parameter)
    s = discrete_potentiation(e, int(secret_key), encryption_parameter)
    print('Розшифровка пройшла успішно. Шифру E = {0} відповідає вихідне повідомлення S = {1}'
          .format(e, s))
