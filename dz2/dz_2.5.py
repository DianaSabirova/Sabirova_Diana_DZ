
#5. Создать список, содержащий цены на товары (10–20 товаров), например:
#[57.8, 46.51, 97, ...]
#* Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
#Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).





list = [57.8, 46.51, 97, 10, 96.58, 64, 893, 1, 55, 179.5, 62.03, 84, 93, 30, 12, 9.08]
rub = 0 # рубли
kop = 0 # копейки
for i in list:
    rub = int(i // 1)  # берем только целую часть для получения рублей
    cop = int(f"{i % 1:.02f}"[2:])     #  результатом остатка от деления будет число не корректное, поэтому мы добавляем :.02f
    # и с помощью :.02f округляем. Затем результатом будет целая часть и она нам не нужна, следовательно я оставляю только копейки. Это 2 индексация [2:]
    print(f"{rub} руб {kop:02d} коп,", end= " ")














