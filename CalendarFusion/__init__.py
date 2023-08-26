import calendar
from datetime import datetime, date
import sys

def get_lang_dict(lang="en"):
    dic = {}
    colnames = ["Week", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    colnames_ja = ["週", "月", "火", "水", "木", "金", "土", "日"]
    colnames_tw = ["週", "一", "二", "三", "四", "五", "六", "日"] # Taiwan
    colnames_hi = ["सप्ताह", "सोम", "मंगल", "बुध", "गुरु", "शुक्र", "शनि", "रवि"]  # Hindi
    colnames_bn = ["সপ্তাহ", "সোম", "মঙ্গল", "বুধ", "বৃহস্পতি", "শুক্র", "শনি", "রবি"]  # Bengali

    if lang == "en":
        for col in colnames:
            dic[col] = col
    elif lang == "tw":
        for col, colja in zip(colnames, colnames_tw):
            dic[col] = colja
    elif lang == "ja":
        for col, colja in zip(colnames, colnames_ja):
            dic[col] = colja
    elif lang =="hi":
        for col, colja in zip(colnames, colnames_hi):
            dic[col] = colja
    elif lang == "bn":
        for col, colja in zip(colnames, colnames_bn):
            dic[col] = colja
    else:
        for col in colnames:
            dic[col] = col
    return dic


def generate_matrix(year, month, first_day=0):
    cal = calendar.Calendar(firstweekday=first_day)
    table = []
    colnames = ["Week", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if cal.firstweekday == 6:  # start from sunday
        colnames = ["Week", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    header = colnames
    table.append(header)

    for days in cal.monthdatescalendar(year, month):
        row = []
        isoweek = days[0].isocalendar()[1]
        row.append(isoweek)
        for d in days:
            row.append(d)
        table.append(row)
    return table


class CalendarFusion:
    def __init__(
        self,
        _year=datetime.now().year,
        _month=datetime.now().month,
        _start_from_sunday=False,
        _week_no=False,
        _fill_calendar = False,
        _lang="eng",
    ):
        self.year = _year
        self.month = _month
        self.DEFAULT_LINK_STYLE = "%Y%m%d"
        self.firstweekday = 6 if _start_from_sunday else 0
        self.lang = _lang
        self.week_no = _week_no
        self.fill_calendar = _fill_calendar
        self.matrix = generate_matrix(
            year=self.year, month=self.month, first_day=self.firstweekday
        )
        self.no_week_matrix = [row[1:] for row in self.matrix]  # do not use this
        if not self.week_no:
            self.matrix = self.no_week_matrix

    def markdown_table(self):
        markdown_str = ""
        dic = get_lang_dict(self.lang)

        table = self.matrix
        calendar_header = [dic[day] for day in table[0]]
        calendar_header = "|" + "|".join(calendar_header) + "|" + "\n"
        markdown_str += calendar_header
        calendar_devider = "|" + "|".join([":-:" for _ in range(len(table[0]))]) + "|" + "\n"
        markdown_str += calendar_devider

        for date_row in table[1:]:
            date_row_str = "|"
            for i in range(0,len(date_row)):
                if self.week_no and i ==0 :
                    date_row_str += str(date_row[0]) + "|"
                else:
                    if not self.fill_calendar and date_row[i].month == self.month:
                        date_row_str += f"{str(date_row[i].day)}|"
                    elif self.fill_calendar:
                        date_row_str += f"{str(date_row[i].day)}|"
                    else:
                        date_row_str += f"|"

            markdown_str += date_row_str + "\n"

        return markdown_str



    def style(self, style="bold", selected=[]):
        styles = {
            "bold": "**",
            "italic": "*",
            "strikeout": "~~",
            "quote": "`"
        }
        
        style_char = styles.get(style, "")

        markdown_str = ""
        dic = get_lang_dict(self.lang)

        table = self.matrix
        calendar_header = [dic[day] for day in table[0]]

        calendar_header = "|" + "|".join(calendar_header) + "|" + "\n"
        markdown_str += calendar_header

        calendar_devider = "|" + "|".join([":-:" for _ in range(len(table[0]))]) + "|" + "\n"
        markdown_str += calendar_devider

        for date_row in table[1:]:
            date_row_str = "|"
            for i in range(0, len(date_row)):
                if self.week_no and i == 0:
                    date_row_str += str(date_row[0]) + "|"
                else:
                    should_fill = self.fill_calendar or date_row[i].month == self.month
                    day_str = f"{style_char}{str(date_row[i].day)}{style_char}" if date_row[i] in selected else str(date_row[i].day)
                    date_row_str += f"{day_str}|" if should_fill else "|"
            markdown_str += date_row_str + "\n"

        print(markdown_str)
        return markdown_str


    def link(self, urls={}):
        markdown_str = ""
        dic = get_lang_dict(self.lang)
        table = self.matrix
        calendar_header = [dic[day] for day in table[0]]
        calendar_header = "|" + "|".join(calendar_header) + "|" + "\n"
        markdown_str += calendar_header

        calendar_devider = "|" + "|".join([":-:" for _ in range(len(table[0]))]) + "|" + "\n"
        markdown_str += calendar_devider

        for date_row in table[1:]:
            date_row_str = "|"
            for i in range(0, len(date_row)):
                if self.week_no and i == 0:
                    date_row_str += str(date_row[0]) + "|"
                else:
                    should_fill = self.fill_calendar or date_row[i].month == self.month
                    url = urls.get(date_row[i])
                    day_str = f"[{str(date_row[i].day)}]({url})" if url else str(date_row[i].day)
                    date_row_str += f"{day_str}|" if should_fill else "|"
            markdown_str += date_row_str + "\n"

        print(markdown_str)
        return markdown_str


    def selective(self,selected=[], selected_date_text:str = None, not_selected_date_text:str = ""):
        markdown_str = ""
        dic = get_lang_dict(self.lang)

        table = self.matrix
        calendar_header = [dic[day] for day in table[0]]

        calendar_header = "|" + "|".join(calendar_header) + "|" + "\n"
        markdown_str += calendar_header

        calendar_devider = "|" + "|".join([":-:" for _ in range(len(table[0]))]) + "|" + "\n"
        markdown_str += calendar_devider

        for date_row in table[1:]:
            date_row_str = "|"
            for i in range(0, len(date_row)):
                if self.week_no and i == 0:
                    date_row_str += str(date_row[0]) + "|"
                else:
                    should_fill = self.fill_calendar or date_row[i].month == self.month
                    if selected_date_text is None:
                        _selected_date_text = date_row[i].day
                    else:
                        _selected_date_text = selected_date_text

                    day_str = _selected_date_text if date_row[i] in selected else not_selected_date_text
                    date_row_str += f"{day_str}|" if should_fill else "|"
            markdown_str += date_row_str + "\n"

        print(markdown_str)
        return markdown_str


    def substitue():
        # substitude selected dates with special text
        pass

    def get_table():
        # get the final markdown table
        pass