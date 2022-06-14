'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях:
<d> дн <h> час <m> мин <s> сек.
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
'''

duration = int(input('Введите длительность '))
print(f'duration {duration}')
seconds_in_minitue = 60
minitues_in_hour = 60
hours_in_day = 24

days = 0
hour = 0
minitues = 0
sec = 0



if duration > 0:
    sec = duration % seconds_in_minitue
    duration //= seconds_in_minitue

if duration > 0:
    minitues = duration % minitues_in_hour
    duration //= minitues_in_hour

if duration > 0:
    hour = duration % hours_in_day
    duration //= hours_in_day

days = duration
list = [days, hour, minitues, sec]
list2 = [' дн ', ' час ', ' мин ', ' сек ']

while list[0] == 0:
    list.pop(0)
    list2.pop(0)

result_string = ''
for index, el in enumerate(list):
    result_string += str(el) + list2[index]

print(result_string)
