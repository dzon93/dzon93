from datetime import datetime

from dateutil import relativedelta

date1 = datetime(1993, 9, 28)
now = datetime.today()
date2 = datetime(now.year, now.month, now.day)

diff = relativedelta.relativedelta(date2, date1)

years = diff.years
months = diff.months
days = diff.days


def dailyreadme():
    if days == 1:
        if months == 1:
            return '{} years, {} month, {} day"'.format(years, months, days)
        else:
            return '{} years, {} months, {} day"'.format(years, months, days)
    elif months == 1:
        return '{} years, {} month, {} days"'.format(years, months, days)
    elif days == 0:
        if months == 0:
            return '{} years"'.format(years)
        else:
            return '{} years, {} months"'.format(years, months, days)
    elif months == 0:
        return '{} years, {} days"'.format(years, days)
    else:
        return '{} years, {} months, {} days"'.format(years, months, days)


def converttuple(tup):
    con = ''.join(tup)
    return con


def readmeoverwrite():
    with open("README.md", "r") as file:
        data = file.readlines()
        line5 = ('          `+NMMMMMMMMMMMMNNMMMMMMMMMMMMMMh:`              Uptime: "', dailyreadme(), "\n")
    tup2str = converttuple(line5)
    data[5] = tup2str

    with open('README.md', 'w') as file:
        file.writelines(data)


if __name__ == '__main__':
    readmeoverwrite()
