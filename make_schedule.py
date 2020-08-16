import math
from test import *

def get_disciplines():
    return parsing_week()
def get_professors():
    return parse_teachers()
def get_requirements():
    return parse_disc()
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

for i in schedule:
    print(i)
