#анализ сложности алгоритмов Big O
#счётчик уникальных символов
#функция считает сколько раз в строке встречается символ
#line - строка
import time
def count_sym(line):
    #set - функция возвращающая множество
    #множество - тип данных без повтроряющихся элементов
    for sym in set(line):
        #counter - счётчик
        counter = 0
        for sub_sym in line:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

#замеряем время начала
start = time.time()
count_sym("Ghoul horse" * 100)
finish = time.time()
print('Время выполнения программы: ',finish-start)
print('Bye')
