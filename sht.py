import gspread
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials
# from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("JtestSheet.json", scope)
client = gspread.authorize(creds)


# sheet = client.open("Pg").sheet1

# sheet = sheet.get_worksheet(0)


def Exec():
    BookName = input('What is the name of the book?: ')
    PgNum = int(input('How many pages does the book have?: '))
    RowNum = int(input('How many days would you like to take to finish reading the book?: '))
    Fm = input('what month is it today?: ')
    Fd = input('date?: ')
    addTitles(BookName)
    fill(PgNum, RowNum, Fm, Fd)


def checkSheet(name):
    try:
        sh1 = client.open(name)
        sh1.del_worksheet(worksheet)
    except:
        pass


def addTitles(Name):
    global worksheet
    worksheet = sh.add_worksheet(title=Name, rows='100', cols='20')
    worksheet_list = sh.worksheets()
    # worksheet = sh.worksheet(str(Name))
    worksheet = sh.get_worksheet(len(worksheet_list) - 1)
    worksheet.update_cell(1, 1, "Date")
    worksheet.update_cell(1, 2, "Page Accumulation")


def format():
    global worksheet
    set_column_width(worksheet, 'A', 80)
    set_column_width(worksheet, 'B', 150)


def checkDate(month, date):
    if month == 4 or month == 6 or month == 9 or month == 11:
        if date == 31:
            month += 1
            date = 1
    elif month == 2:
        if date == 30:
            month += 1
            date = 1
    else:
        if date == 32:
            month += 1
            date = 1
    if month == 13:
        month = 1
    print(month, date)
    return month, date


def fill(Pnum, Rnum, m, d):
    global worksheet
    pacing = round(float(Pnum / Rnum))
    Day = Pnum / pacing
    x = 1
    startRow = 1
    Acc = 0
    month = int(str(m))
    date = int(str(d))
    while x <= Day:
        month = int(month)
        date = int(date)

        worksheet.update_cell(startRow + x, 1, str(month) + "/" + str(date))
        worksheet.update_cell(startRow + x, 2, Acc + pacing)
        Acc = Acc + pacing
        date += 1
        if month == 4 or month == 6 or month == 9 or month == 11:
            if date == 31:
                month += 1
                date = 1
        elif month == 2:
            if date == 30:
                month += 1
                date = 1
        else:
            if date == 32:
                month += 1
                date = 1
        if month == 13:
            month = 1
        x += 1


sh = client.open('hello')
worksheet = sh.sheet1
Exec()
