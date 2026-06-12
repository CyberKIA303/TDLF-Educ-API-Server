from datetime import datetime
from .letter_casing import lower_case_words

monthval = [
    {"numval": "01", "chrval": "January"},
    {"numval": "02", "chrval": "February"},
    {"numval": "03", "chrval": "March"},
    {"numval": "04", "chrval": "April"},
    {"numval": "05", "chrval": "May"},
    {"numval": "06", "chrval": "June"},
    {"numval": "07", "chrval": "July"},
    {"numval": "08", "chrval": "August"},
    {"numval": "09", "chrval": "September"},
    {"numval": "10", "chrval": "October"},
    {"numval": "11", "chrval": "November"},
    {"numval": "12", "chrval": "December"}
]

not_allowed = "- :"

def flexer_data(data: list, target: str):
    output: str = ""
    for dim in data:
        if dim['type'] == target:
            output = dim['data']
            break
    return output

def get_modern_datetime_now(date: datetime, add_year: int = 0):
    output: str = ""
    now = date.now()
    meridian: str = str(now.strftime('%p'))
    data: str = str(now)
    containdt = [
        {"init": "0", "type": "year",   "data": ""},
        {"init": "1", "type": "month",  "data": ""},
        {"init": "2", "type": "day",    "data": ""},
        {"init": "3", "type": "hour",   "data": ""},
        {"init": "4", "type": "minute", "data": ""},
        {"init": "5", "type": "seconds","data": ""}
    ]
    target: int = 0
    content: str = ""
    for let in data:
        ok: bool = True
        if let == '.':
            break
        for check in not_allowed:
            if let == check:
                ok = False
                break
        if ok:
            content += let
        else:
            for dim in containdt:
                if str(target) == dim['init']:
                    dim['data'] = content
                    break
            content = ""
            target += 1
    letmonth: str = flexer_data(containdt, "month")
    for lm in monthval:
        if lm['numval'] == letmonth:
            letmonth = lm['chrval']
            break
    letyear: int = int(flexer_data(containdt, "year")) + add_year
    lethour: int = int(flexer_data(containdt, "hour"))
    trimhour: str = ""
    if lethour > 12:
        lethour -= 12
    if lethour < 10:
        trimhour += "0" + str(lethour)
    else:
        trimhour = str(lethour)
    output = letmonth + " " + flexer_data(containdt, "day") + ", " + str(letyear) + " - " + trimhour + ":" + flexer_data(containdt, "minute") + lower_case_words(meridian)
    return output

def simplify_datetime(date_and_time: str):
    output: str = ""
    for let in date_and_time:
        if let != '.':
            output += let
        else:
            break
    return output

def add_5years_terms(date_and_time: str):
    output: str = ""
    data: str = ""
    year_get: bool = False
    for let in date_and_time:
        if let == '-' and not year_get:
            year_get = True
            output += str(int(data) + 5)
        if not year_get:
            data += let
        else:
            output += let
    return output