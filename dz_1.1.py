# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.


duration = int(input("Введите время в секундах"))
seconds = duration % 60
minutes = duration // 60 % 60
day = duration // 86400
hour = duration // 3600 % 24
print("day:", day,",", "hour:", hour, "," ,"minutes:", minutes,","  "seconds:", seconds)


