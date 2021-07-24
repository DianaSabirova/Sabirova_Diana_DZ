
#2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
#>>> >>> num_translate_adv("One")
#"Один"
#>>> num_translate_adv("two")
#"два"

translation_dict = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "чертыре", "five": "пять",
               "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
# словарь снаружи,
#за пределами функции, так чтобы была возможность взаимодействия других функций с этим словарём.
# Если я напишу в теле функции, то она будет локальная. Другие функции не смогут повзаимодействовать с ними.
def num_translate(word):# word - параметр.
    if word.istitle(): # если наше слово начинается с первой большой буквы. То, наш фильтр должен реагировать на это.
        return str(translation_dict.get(word.lower())).title()#наш фильтр. Мы обращамся к словарю, затем ставим get(чтобы не было ошибки, а было просто none).
        # Преобразуем так, чтобы символы сводились к одному. Чтобы слова(word),если они в верхнем регистре, то входили сначала всеми буквами в нижнем регистре. -  .lower
        # А затем выпускались так, чтобы первая заглавная буква была в верхнем.  - .title.    Чтобы не было ошибки, мы сначала приобразуем всё к строке.
    return translation_dict.get(word)
print(num_translate(input("Введите слово на английском: ")))


