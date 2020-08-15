import math

def get_disciplines():
    return [{'discipline': 'Досмотр', 'type': 'Повышение квалификации', 'date': '13.01 - 17.01', 'classroom': ['107']},
        {'discipline': 'Перронный контроль', 'type': 'Специальная профессиональная подготовка', 'date': '13.01-24.01', 'classroom': ['105']},
        {'discipline': 'Опасные грузы. 10 категория', 'type': 'Повышение квалификации', 'date': '13.01–14.01', 'classroom': ['414Б']},
        {'discipline': 'Опасные грузы. 9 категория', 'type': 'Повышение квалификации', 'date': '13.01–14.01', 'classroom': ['422']},
        {'discipline': 'Досмотр', 'type': 'Повышение квалификации', 'date': '20.01 - 24.01', 'classroom': ['107']},
        {'discipline': 'Перронный контроль', 'type': 'Специальная профессиональная подготовка', 'date': '13.01-24.01', 'classroom': ['105']},
        {'discipline': 'Охрана аэропорта ', 'type': 'Повышение квалификации', 'date': '20.01- 24.01', 'classroom': ['106', '414б']},
        {'discipline': 'Пассажирские перевозки', 'type': 'Базовый курс', 'date': '21.01–24.01', 'classroom': ['414Б-1']},
        {'discipline': 'Опасные грузы. 9 категория', 'type': 'Повышение квалификации', 'date': '20.01–21.01', 'classroom': ['422']},
        {'discipline': 'Опасные грузы. 8 категория', 'type': 'Повышение квалификации', 'date': '22.01–23.01', 'classroom': ['422']},
        {'discipline': 'Досмотр', 'type': 'Повышение квалификации', 'date': '27.01 - 31.01', 'classroom': ['107']},
        {'discipline': 'Перронный контроль', 'type': 'Повышение квалификации', 'date': '27.01 - 31.01', 'classroom': ['105']},
        {'discipline': 'Опасные грузы. 9 категория', 'type': 'Базовый курс', 'date': '27.01–28.01', 'classroom': ['422']},]

def get_professors():
    return [{'name': 'Лебедев М.В.', 'works': [{'discipline': 'Центровка и контроль загрузки ВС', 'type': 'Базовый курс'}, {'discipline': 'Центровка и контроль загрузки ВС', 'type': 'Повышение квалификации'}], 'prior': 2, 'work_time': 'пятидневный', 'scheduler': 'нет'},
        {'name': 'Красненко А.Г.', 'works': [{'discipline': 'Центровка и контроль загрузки ВС', 'type': 'Базовый курс'}, {'discipline': 'Центровка и контроль загрузки ВС', 'type': 'Повышение квалификации'}], 'prior': 1, 'work_time': 'пятидневный', 'scheduler': 'нет'},
        {'name': 'Автеньев Д.Г.', 'works': [{'discipline': 'Опасные грузы. 10 категория', 'type': 'Базовый курс'}, {'discipline': 'Опасные грузы. 10 категория', 'type': 'Повышение квалификации'}, {'discipline': 'Опасные грузы. 8 категория', 'type': 'Базовый курс'}, {'discipline': 'Опасные грузы. 8 категория', 'type': 'Повышение квалификации'}], 'prior': 2, 'work_time': 'сменный', 'scheduler': '3 смена'},
        {'name': 'Шабалин К.Н.', 'works': [{'discipline': 'Опасные грузы. 10 категория', 'type': 'Базовый курс'}, {'discipline': 'Опасные грузы. 10 категория', 'type': 'Повышение квалификации'}, {'discipline': 'Опасные грузы. 8 категория', 'type': 'Базовый курс'}, {'discipline': 'Опасные грузы. 8 категория', 'type': 'Повышение квалификации'}], 'prior': 'при распределении на программы 7 и 8 - приоритет 1', 'work_time': 'пятидневный', 'scheduler': 'нет'},
        {'name': 'Пачко Г.М.', 'works': [{'discipline': 'Опасные грузы. 8 категория', 'type': 'Базовый курс'}, {'discipline': 'Опасные грузы. 8 категория', 'type': 'Повышение квалификации'}], 'prior': 'при распределении на программы 11 и 12- приоритет 1', 'work_time': 'пятидневный', 'scheduler': 'нет'},
        {'name': 'Гладковская А.Ю.', 'works': [{'discipline': 'Опасные грузы. 8 категория', 'type': 'Базовый курс'}, {'discipline': 'Опасные грузы. 8 категория', 'type': 'Повышение квалификации'}, {'discipline': 'Опасные грузы. 9 категория', 'type': 'Базовый курс'}, {'discipline': 'Пассажирские перевозки', 'type': 'Повышение квалификации'}, {'discipline': 'Пассажирские перевозки', 'type': 'Базовый курс'}], 'prior': 'при распределении на программы 11;12 приоритет 2', 'work_time': 'пятидневный', 'scheduler': 'нет'},
        {'name': 'Попова И.О.', 'works': [{'discipline': 'Опасные грузы. 8 категория', 'type': 'Базовый курс'}, {'discipline': 'Опасные грузы. 8 категория', 'type': 'Повышение квалификации'}, {'discipline': 'Опасные грузы. 9 категория', 'type': 'Базовый курс'}, {'discipline': 'Пассажирские перевозки', 'type': 'Повышение квалификации'}, {'discipline': 'Пассажирские перевозки', 'type': 'Базовый курс'}], 'prior': 'при распределении на программы 11;12 приоритет 2', 'work_time': 'пятидневный', 'scheduler': 'нет'},]

def get_requirements():
    return [{'discipline': 'Центровка и контроль загрузки ВС', 'type': 'Базовый курс', 'hours': 80},
        {'discipline': 'Центровка и контроль загрузки ВС', 'type': 'Повышение квалификации', 'hours': 64},
        {'discipline': 'Опасные грузы. 10 категория', 'type': 'Базовый курс', 'hours': 24},
        {'discipline': 'Опасные грузы. 10 категория', 'type': 'Повышение квалификации', 'hours': 16},
        {'discipline': 'Опасные грузы. 9 категория', 'type': 'Базовый курс', 'hours': 16},
        {'discipline': 'Опасные грузы. 8 категория', 'type': 'Базовый курс', 'hours': 24},
        {'discipline': 'Опасные грузы. 8 категория', 'type': 'Повышение квалификации', 'hours': 16},
        {'discipline': 'Пассажирские перевозки', 'type': 'Повышение квалификации', 'hours': 16},
        {'discipline': 'Пассажирские перевозки', 'type': 'Базовый курс', 'hours': 32},
        {'discipline': 'Организация наземного обслуживания ВС', 'type': 'Базовый курс', 'hours': 72},
        {'discipline': 'Организация наземного обслуживания ВС', 'type': 'Повышение квалификации', 'hours': 32},]

disciplines = get_disciplines()
professors = get_professors()
requirements = get_requirements()

lectures = 4
months = 12
days = 31
schedule = [[[[] for x in range(lectures)] for y in range(days)] for z in range(months)]

def get_date(date):
    day = int(date[:2])
    month = int(date[3:])
    return [day, month]

def get_discipline(item):
    return item['discipline'] + '/' + item['type']

'''
Пара 1- 09.00-10.30
Пара 2- 10.40-12.10
Пара 3- 12.50-14.20
Пара 4- 14.30-16.00
'''

def check_classroom(lecture, day, month, classroom):
    for item in schedule[month][day][lecture]:
        if item['classroom'] == classroom:
            return False
    return True

def check_professor(lecture, day, month, professor):
    for item in schedule[month][day][lecture]:
        if item['professor'] == professor:
            return False
    return True

def check_professor_discipline(professor, discipline):
    for item in professor['works']:
        if get_discipline(item) == discipline:
            return True
    return False

need_lectures = {}
for item in requirements:
    need_lectures[get_discipline(item)] = int(math.ceil(item['hours'] / 1.5))

for item in disciplines:
    cur = get_discipline(item)
    if need_lectures.get(cur) == 0:
        continue
    dates = item['date'].split('-')
    if len(dates) == 1:
        dates = item['date'].split('–')
    dates = [dates[0].strip(), dates[1].strip()]
    date_start = get_date(dates[0])
    date_end = get_date(dates[1])
    month = date_start[1] - 1
    print(date_start)
    for day in range(date_start[0] - 1, date_end[0]):
        if need_lectures.get(cur) == 0:
            break
        for lecture in range(lectures):
            if need_lectures.get(cur) == 0:
                break
            for classroom in item['classroom']:
                if check_classroom(lecture, day, month, classroom):
                    temp = {'discipline' : item['discipline'], 'type' : item['type'], 'classroom' : classroom, 'professor' : ''}
                    schedule[month][day][lecture].append(temp)
                    if cur in need_lectures:
                        need_lectures[cur] -= 1
                    break


for month in range(months):
    for day in range(days):
        for lecture in range(lectures):
            for item in schedule[month][day][lecture]:
                cur = get_discipline(item)
                for professor in professors:
                    if check_professor(lecture, day, month, professor['name']) and check_professor_discipline(professor, cur):
                        item['professor'] = professor['name']

print(schedule)
