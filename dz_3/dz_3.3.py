#3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
#{
#    "И": ["Иван", "Илья"],
#    "М": ["Мария"], "П": ["Петр"]
#
#Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
 # нам нужно получить результат работы функции tresaurus, где:
#    {ключ - первая буква имени сотрудника ; значения -  [список, в котором имя или имена сотрудников  ] }
#}


def tresaurus(*args): # мы не знаем кол-во имен(аргументов), которые могут передать, поэтому ставим *args
    names_dict = {} # готовим пустой словарь, в него мы будем добавлять и сохранять
    for name in sorted(args): # сюда попадают уже отсортированные имена (кортеж). От меньшего к большему
        letter = name[0] # добавляем переменную, она будет равна первой буквы имени. Это условие будет работать в любом случае
        if letter in names_dict: # если эта первая буква есть в ключе словаря, то:
             names_dict[letter] += [name] # получается словарь в котором пара ключ-значение.
             #  Ключем будет 1 буква имени. Значением будет само имя, и если их несколько, то они добавяться
        else:
            names_dict[letter] = [name] # в других случаях, ключем будет первая буква имени, а значением одно имя
    return names_dict
print(tresaurus("Виктория", "Валентина", "Евгения", "Вадим", "Диана", "Данил", "Борис"))














