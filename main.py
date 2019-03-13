import pandas_datareader.data as web
import datetime
import csv
import pandas as pd


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

df = web.DataReader('^GSPC', 'yahoo', start=start, end=end)

header = ['Close']
f = df.to_csv('csvvvv.csv', columns=header)

results = []

with open("csvvvv.csv") as csvfile:
    reader = csv.reader(csvfile, quotechar=',')  # change contents to floats
    for row in reader:  # each row is a list
        results.append(row)


start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")                                                              # здесь мы генерим массив дат
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")                                                                # формат во второй переменной ГГГГ-ММ-ДД
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]


rez = []
for i in range(len(date_generated)):
    rez.append([date_generated[i], 0])

print(rez)

for i in range(1, len(results)):
    for j in range(i, len(date_generated)):                                                                             # нужно подождать секунд 15-20(слишком много жрет циклов)
        if datetime.datetime.strptime(results[i][0], "%Y-%m-%d") == date_generated[j]:
            rez[j][1] = results[i][1]
            break
print(rez)

prev_non_zero = 0
next_non_zero = 0
middle_value = 0

if rez[0][1] == 0:
    for i in range(0, len(rez)):                                                                                        #  Заполняем первые нули первым ненулевым значением
        if rez[i][1] != 0:                                                                                              #  Также проверяем, равно ли первое значение нулю
            next_non_zero = rez[i][1]
            for j in range(0, i):
                rez[j][1] = next_non_zero
            break

print(rez)

not_zero = True
j = -1
for i in range(0, len(rez)):                                                                                            #  Проходим по циклу, ищем нули, заполняем их средним
    if (rez[i][1] == 0) and not_zero:
        prev_non_zero = float(rez[i-1][1])
        j = i
        not_zero = False
    if (rez[i][1] != 0) and not not_zero:
        next_non_zero = float(rez[i][1])
        middle_value = (prev_non_zero + next_non_zero)/2
        for each in range(j, i):
            rez[each][1] = str(middle_value)
        not_zero = True

print(rez)

curr_year = start.year
curr_month = start.month
start_dt = curr_month + curr_year * 12
end_dt = rez[len(rez)-1][0].month + rez[len(rez)-1][0].year * 12

new_rez = []
void_mas = []

for i in range(start_dt, end_dt, 2):                                                                                    #TODO добавляется только 1 интервал январь-февраль 2006, надо пофиксить
    temp = []
    curr_month = i % 12
    curr_year = i // 12
    for j in range(((curr_month + curr_year * 12) - start_dt), ((curr_month + curr_year * 12) - start_dt + 62)):
        if (rez[j][0].month == curr_month or rez[j][0].month == curr_month + 1) and rez[j][0].year == curr_year:        #TODO возможно ошибка где-то в логике этого условия
            temp.append(rez[j])
        elif temp != void_mas:
            new_rez.append(temp)
        else:
            i += 2

print(new_rez)                                                                                                          #  итоговый массив формата [интервал][дата][значение]
