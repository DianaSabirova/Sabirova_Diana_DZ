#2. Дан список:
#['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
#['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#Новый список не создавать! Сформировать из обработанного списка строку:
#в "05" часов "17" минут температура воздуха была "+05" градусов

list_wrong = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_correct = []
# Задача поставить у чисел кавычки, а также дополнить числом 0

#переберём каждый элемент строки
for i in list_wrong:


     #блок для чисел
     # нужно чтобы у каждой цифры стояли кавычки. Если значение(цифры) + или -, то меняем его на пустую строку
     if i.replace("+", "").replace("-", "").isdigit():  # cюда должно попасть +5. Знак не отсекается, а временно убирается для прохождения проверки
        if i.isdigit():# в этой строке мы доработаем числа, которые не попали в условие выше, значения без знаковые. Дополним кавычки и 0 в правильный список.
            list_correct.append(f"'{int(i):02}'") # ставим  (f"'{int(i):02}'")  для того чтобы поставить дополнительный 0 перед числом(если только 1 цифра).
            # Если из 2х, то не сработает(добавятся только "")
        else: # сюда попадут элементы у которых есть знак.
            list_correct.append(f"'{i[0]} {int(i[1:]):02}'")
                     #  форматируем, склеиваим.  f"'{i[0]} #сохраняем знак", первый элемент[0] - это знак.
                     #{i[1:]} сохраняем значение, пишем :. Он первого и до конца,так как может быть длинное число.
     else:
        list_correct.append(i) # сюда попадут значения без изменений(в, часов, минут и т.д)


print(" ".join(list_correct))





