# Caesar's Cipher

Шифр Цезаря (шифр сдвига) — один из самых простых и наиболее широко известных методов шифрования. Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите.

## Математиеская модель

Если сопоставить каждый символ алфавита с его порядковым номером (нумеруя с 0), то шифрование и дешифрование можно выразить формулами модульной арифметики:

y=(x+k) mod n,</br>
x=(y−k) mod n,</br>
где:</br>
x — символ открытого текста, </br>
y — символ шифрованного текста, </br>
n — мощность алфавита (количество символов),</br>
k — ключ.

Под операцией mod подразумевается операция нахождения остатка. В языке Python для нахождения остатка от деления двух чисел, мы используем оператор %.

**Описание проекта:** 

требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:

- направление: шифрование или дешифрование;
- язык алфавита: русский или английский;
- шаг сдвига (со сдвигом вправо).

Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

**Составляющие проекта:**

Целые числа (тип int);</br>
Модульная арифметика;</br>
Переменные;</br>
Ввод / вывод данных (функции input() и print());</br>
Условный оператор (if/elif/else);</br>
Цикл for/while;</br>
Строковые методы.</br>