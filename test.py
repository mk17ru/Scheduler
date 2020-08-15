from openpyxl import load_workbook
import re
def parsing_week():
    wb = load_workbook('./data/Приложение №1.xlsx')
    sheet = wb.get_sheet_by_name('ДПО')
    week_amount = [0, 5, 4, 4, 5, 4, 4, 5, 4, 4, 5, 4, 5]
    weeks = []
    discipline_col = 7
    year_col = 9
    for month in range(12):
        year_col = year_col + week_amount[month] * 2
        for week in range(year_col, year_col + week_amount[month + 1] * 2 + 1, 2):
            for p in range(6, 30, 2):
                if sheet.cell(row=p, column=discipline_col).value == None or sheet.cell(row=p, column=week).value == None:
                    continue
                else:
                    s = sheet.cell(row=p, column=week).value.split('\n')
                    if (len(s) > 3):
                        new_str = ""
                        ind = 0
                        for r in s:
                            if len(r) > 0 and str.isalpha(r[0]):
                                new_str += r + " "
                                ind += 1
                            else:
                                break
                        new_s = []
                        new_s.append(new_str.strip())
                        for i in range(ind, len(s)):
                            new_s.append(s[i])
                        s = new_s
                    # because of hidden cells
                    if (len(s) < 3 or s[0] == "" or s[1] == "" or s[2] == ""):
                        continue
                    auditoriums = []
                    s[2] = str.replace(s[2], '.', ' ')
                    for i in re.split(' ', s[2]):
                        if i == "ауд" or i == "ИАС" or i == "":
                            continue
                        print(i)
                        for cur in i.split(','):
                            auditoriums.append(cur)
                    temp = {"discipline": sheet.cell(row=p, column=discipline_col).value, "type": s[0], "date": s[1], "classroom": auditoriums}
                    weeks.append(temp)
    return weeks

 #Parsing application 1
#for i in parsing_week():
#    print(i)

