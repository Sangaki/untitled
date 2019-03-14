import datas
import graphs
import asdasd
import datetime
import math

start = datetime.datetime.strptime("2006-1-1", "%Y-%m-%d")  # здесь мы генерим массив дат
end = datetime.datetime.strptime("2016-1-1", "%Y-%m-%d")  # формат во второй переменной ГГГГ-ММ-ДД

df = datas.get_data()

results = datas.data_to_cvs(df)
#  print(results)

rez = datas.filling_empty_days(results, start, end)
#  print(rez)

rez = datas.floating_mass(rez)

new_rez = datas.sequence(rez, start)

# out = asdasd.diff_timeline(new_rez[0], start, rez)
# TODO ПОЧЕМУ ПОСЛЕ ВЫПОЛНЕНИЯ ЭТОЙ ФУНКЦИИ В new_rez НА ПЕРВОМ ИНТЕРВАЛЕ ДИФФЕРЕНЦИРОВАННЫЕ ЗНАЧЕНИЯ???????

# graphs.plot(new_rez[0])

summ = 0
for i in range(len(rez)):
    summ += rez[i][1]
summ /= len(rez)  # среднее арифметическое ВСЕХ данных (всех отрезков)
print('summ=', summ)
summ_i = 0
square_temp = 0
z = []
qwe = 0
for each in range(len(new_rez)):
    for j in range(len(new_rez[qwe])):
        summ_i += new_rez[qwe][j][1]
    summ_i /= len(new_rez[qwe])
    square_temp += math.pow((summ_i - summ), 2)  # скобочка с квадратом в сумме хуйня ебаная блять я запутался
    z.append(summ - summ_i)
    summ_i = 0
    qwe += 1

print('huynya = ', square_temp)
print('z = ', z)
print('summ z = ', math.fsum(z))
s = math.sqrt(square_temp/len(new_rez))
print('s = ', s)
alpha = 1.5708  # по той формуле можно альфу на 0.5 поменять и тогда h=0.4011
r = max(z) - min(z)
print('R = ', r)

h = math.log(r/s)/math.log(alpha*len(new_rez))

print('H = ', h)
