import re


def dateDetection(date: str):
    dateRegex = re.compile(r"(\d{2})/(\d{2})/(\d{4})")
    mo = dateRegex.search(date)
    if not mo:
        return "Invalid format.", False
    day, month, year = mo.groups()

    isLeapYear = (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0
    months = {
        "01": ("January", 31),
        "02": ("February", 28 + isLeapYear),
        "03": ("March", 31),
        "04": ("April", 30),
        "05": ("May", 31),
        "06": ("June", 30),
        "07": ("July", 31),
        "08": ("August", 31),
        "09": ("September", 30),
        "10": ("October", 31),
        "11": ("November", 30),
        "12": ("December", 31),
    }

    if not (0 < int(month) < 13):
        return "Invalid month.", False

    formattedMonth, maxDays = months[month]
    if not (0 < int(day) < maxDays + 1):
        return "Invalid day.", False

    return f"{formattedMonth} {day}, {year}.", True


dates = [
    "03/12/1992",
    "01/01/2000",
    "15/15/2015",
    "30/02/2021",
    "tuesday",
    "31/11/2000",
    "30/11/2000",
    "29/02/1960",
    "29/02/1961",
    "29/02/1900",
]
for date in dates:
    print(date, dateDetection(date))
