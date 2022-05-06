def check_digit(num):
    while True:
        try:
            num = int(num)
        except ValueError:
            num = input('Введите 0 или 1 - ')
            continue
        return num

def check_num(num):
    while True:
        try:
            num = int(num)
        except ValueError:
            num = input('Введите число - ')
            continue
        return num


encryption_direction = input('Вы хотите зашифровать (0) или дешифровать (1)? (0/1) - ')
encryption_direction = check_digit(encryption_direction)
lang = input('Выберите язык текста: Английский (0) или Русский (1) (0/1) - ')
lang = check_digit(lang)
step = input('Введите шаг сдвига (число) - ')
step = check_num(step)
phrase = input('Введите текст - ')
rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
len_rus = 32
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
len_eng = 26
result = ''

def progress(result):
    if lang == 0:
        for i in range(len(phrase)):
            if phrase[i].isalpha():
                if ord('A') <= ord(phrase[i]) <= ord('Z'):
                    if (ord(phrase[i]) - (step % len_eng)) > 90:
                        result = result + chr((ord(phrase[i]) + (step % len_eng)) - 26)
                    else:
                        result = result + chr((ord(phrase[i]) + (step % len_eng)))
                else:
                    if (ord(phrase[i]) - (step % len_eng)) > 122:
                        result = result + chr((ord(phrase[i]) + (step % len_eng)) - 26)
                    else:
                        result = result + chr((ord(phrase[i]) + (step % len_eng)))

            else:
                result = result + phrase[i]
        print(result)

progress(result)
