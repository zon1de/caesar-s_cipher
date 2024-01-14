from icecream import ic #from icecream import ic
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
# rus_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
len_rus = 32
# eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng = 'abcdefghijklmnopqrstuvwxyz'
len_eng = 26
result = ''

def progress(result):
    if lang == 0:
            for i in range(len(phrase)):
                if phrase[i].isalpha():
                    if ord('A') <= ord(phrase[i]) <= ord('Z'):
                        result = result + eng[step - (len_eng - eng.find(phrase[i].lower()))].upper()
                    else:
                        result = result + eng[step - (len_eng - eng.find(phrase[i].lower()))]
                else:
                    result = result + phrase[i]
            print(result)

    if lang == 1:
        for i in range(len(phrase)):
            if phrase[i].isalpha():

                if ord('А') <= ord(phrase[i]) <= ord('Я'):
                    result = result + rus[step - (len_rus - rus.find(phrase[i].lower()))].upper()
                else:
                    result = result + rus[step - (len_rus - rus.find(phrase[i].lower()))]
            else:
                result = result + phrase[i]
        print(result)


def reprogress(result):
    if lang == 0:
        for i in range(len(phrase)):
            if phrase[i].isalpha():
                if ord('A') <= ord(phrase[i]) <= ord('Z'):
                    result = result + eng[(eng.find(phrase[i].lower())) - step].upper()
                else:
                    result = result + eng[(eng.find(phrase[i].lower())) - step]
            else:
                result = result + phrase[i]
        print(result)

    if lang == 1:
        for i in range(len(phrase)):
            if phrase[i].isalpha():

                if ord('А') <= ord(phrase[i]) <= ord('Я'):
                    result = result + rus[(rus.find(phrase[i].lower())) - step].upper()
                else:
                    result = result + rus[(rus.find(phrase[i].lower())) - step]
            else:
                result = result + phrase[i]
        print(result)

if encryption_direction == 0:
    progress(result)
else:
    reprogress(result)
