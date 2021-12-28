from Crypto.Cipher import DES3
import random


# необхідно, щоб вхідний текст ділиться націло на 8
def examination(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


# функція шифрування
def enctypt(text, des):
    return des.encrypt(text.encode('utf-8'))


# функція дешифрування
def decrypt(text, des):
    return des.decrypt(text).decode().rstrip('')


# генерація ключа
def key_generation():
    symbols = list('qwertyuiopasdfghjklzxcvbnm1234567890+-/*.,<>/?\|_!@#$%^&()~')
    key_list = ''
    for i in range(24):
        key_list += random.choice(symbols)

    return bytes(str(key_list), encoding='utf-8')


print('Це програма шифрування і дешифрування тексту.')

counter = True
key = key_generation()

while counter:
    mode = input('Введіть 1 якщо бажаєте зашифрувати текст: ')
    if mode == '1':
        text = input('Введіть текст, який бажаєте зашифрувати: ')
        right_text = examination(text)  # данные для шифрования

        # створення екземпляру DES3
        des = DES3.new(key, DES3.MODE_ECB)

        # шифрування
        encrypted_text = enctypt(right_text, des)
        output_encrypted_text = input('Вивести зашифрований текст? (Якщо так - введіть 1): ')
        if output_encrypted_text == '1':
            print('Зашифрований текст: ', encrypted_text)

        # дешифрування
        decrypted_text = decrypt(encrypted_text, des)
        output_decrypted_text = input('Вивести результати дешифрування? (Якщо так - введіть 1): ')
        if output_decrypted_text == '1':
            print('Розшифрований текст: ', decrypted_text)

        text = input('Зберегти ключ - введіть 1, згенерувати новий ключ - введіть 2: ')
        if text == '2':
            key = key_generation()

    else:
        counter = False
