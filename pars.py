import bs4
from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote, quote
#"cp1251"



async def save_data(update, context):
    url = "https://ps.vnu.edu.ua/cgi-bin/timetable.cgi?n=700"
    writing = ""
    group = update.message.text
    context.user_data["group"] = group
    encoded_group = quote(group, encoding='cp1251')
    data = "faculty=0&teacher=&course=0&group=" + encoded_group + "&sdate=&edate=&n=700"
    response = requests.post(url, data= data)
    response.encoding = 'cp1251'
    soup = BeautifulSoup(response.text, "lxml")
    tables = soup.find_all("div", class_="container")
    week = tables[1]

    week_days = week.find_all("div", class_="col-md-6 col-sm-6 col-xs-12 col-print-6")
    if not week_days:
        return 1

    for weekday in week_days:
        date = weekday.find("h4")
        writing += date.text + "\n" + "\n"
        schedule = weekday.find_all("tr")
        for tr in schedule:
            row = tr.text
            if len(row) < 13:
                continue
            num = f"{row[0]}\ufe0f\u20e3"
            row = num + " " + row[1:6] + " — " + row[6:11] + " \n" + "📚" + row[11:] + " \n"
            row = row.replace('\xa0', ' ')
            markers1 = ['зав', 'ст.', 'проф.', 'доц.', 'асист']
            aud = 'ауд'
            groups = ['Збірна група', 'Потік']
            spec = "Ліквідація"
            for marker in markers1:
                if marker in row:
                    row = row.replace(marker, "\n" + "👨‍🏫 " + marker, 1)
                    break
            row = row.replace(aud, "\n" + "🏫 " + aud, 1)
            row = row.replace(spec, "\n" + spec, 1)
            for gr in groups:
                row = row.replace(gr, "\n" + "🥷 " + gr, 1)
            writing += row + "\n"
        writing += "➖" * 14 + "\n" + "\n"
        print(writing)
    with open(group + ".txt", "w", encoding="utf-8") as f:
        f.write(writing)
    return 3