import calendar
from datetime import datetime


def get_lang_dict(lang="en"):
    dic = {}
    colnames = ["Week", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    colnames_ja = ["週", "月", "火", "水", "木", "金", "土", "日"]
    colnames_tw = ["週", "一", "二", "三", "四", "五", "六", "日"]  # Taiwan
    colnames_hi = [
        "सप्ताह",
        "सोम",
        "मंगल",
        "बुध",
        "गुरु",
        "शुक्र",
        "शनि",
        "रवि",
    ]  # Hindi
    colnames_bn = [
        "সপ্তাহ",
        "সোম",
        "মঙ্গল",
        "বুধ",
        "বৃহঃ",
        "শুক্র",
        "শনি",
        "রবি",
    ]  # Bengali

    if lang == "en":
        for col in colnames:
            dic[col] = col
    elif lang == "tw":
        for col, colja in zip(colnames, colnames_tw):
            dic[col] = colja
    elif lang == "ja":
        for col, colja in zip(colnames, colnames_ja):
            dic[col] = colja
    elif lang == "hi":
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
    """This class will be used to generate a month's custom calendar views."""
    def __init__(
        self,
        year=datetime.now().year,
        month=datetime.now().month,
        start_from_sunday=False,
        week_no=False,
        fill_calendar=False,
        lang="eng",
    ):
        """Initialize a month's calendar.

        Args:
            year (_type_, optional): Calendar year. Defaults to datetime.now().year.
            month (_type_, optional): Calendar month. Defaults to datetime.now().month.
            start_from_sunday (bool, optional): Specifies if the first day of the week is sunday or not. Defaults to False (monday).
            week_no (bool, optional): Week no of the given month. Defaults to False.
            fill_calendar (bool, optional): Specifies if the the calendar should fill with previous and next month's dates. Defaults to False.
            lang (str, optional): Calendar language. Defaults to "eng".
        """
        self.year = year
        self.month = month
        self.DEFAULT_LINK_STYLE = "%Y%m%d"
        self.firstweekday = 6 if start_from_sunday else 0
        self.lang = lang
        self.week_no = week_no
        self.fill_calendar = fill_calendar
        self.matrix = generate_matrix(
            year=self.year, month=self.month, first_day=self.firstweekday
        )
        self.no_week_matrix = [
            row[1:] for row in self.matrix
        ]  # remove the first column containing week numbers
        if not self.week_no:
            self.matrix = self.no_week_matrix

    def calendar(self) -> str:
        """Generate calendar view with no customization
        Returns:
            str: Returns a markdown table as output.
        """
        markdown_str = ""
        dic = get_lang_dict(self.lang)

        table = self.matrix
        calendar_header = [dic[day] for day in table[0]]
        calendar_header = "|" + "|".join(calendar_header) + "|" + "\n"
        markdown_str += calendar_header
        calendar_divider = (
            "|" + "|".join([":-:" for _ in range(len(table[0]))]) + "|" + "\n"
        )
        markdown_str += calendar_divider

        for date_row in table[1:]:
            date_row_str = "|"
            for i in range(0, len(date_row)):
                if self.week_no and i == 0:
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

    def style(self, style="bold", selected=[]) -> str:
        """Add styles to the dates.

        Args:
            style (str, optional): Formatting styles of the dates. options: bold,italic,strikeout,quote. Defaults to "bold".
            selected (list, optional): Apply formatting styles to the selected dates only. expects a list of dates Defaults to [].

        Returns:
            str: Returns a markdown table as output.
        """
        styles = {"bold": "**", "italic": "*", "strikeout": "~~", "quote": "`"}
        style_char = styles.get(style, "")

        markdown_str = ""
        dic = get_lang_dict(self.lang)

        table = self.matrix
        calendar_header = [dic[day] for day in table[0]]

        calendar_header = "|" + "|".join(calendar_header) + "|" + "\n"
        markdown_str += calendar_header

        calendar_divider = (
            "|" + "|".join([":-:" for _ in range(len(table[0]))]) + "|" + "\n"
        )
        markdown_str += calendar_divider

        for date_row in table[1:]:
            date_row_str = "|"
            for i in range(0, len(date_row)):
                if self.week_no and i == 0:
                    date_row_str += str(date_row[0]) + "|"
                else:
                    should_fill = self.fill_calendar or date_row[i].month == self.month
                    day_str = (
                        f"{style_char}{str(date_row[i].day)}{style_char}"
                        if date_row[i] in selected
                        else str(date_row[i].day)
                    )
                    date_row_str += f"{day_str}|" if should_fill else "|"
            markdown_str += date_row_str + "\n"

        return markdown_str

    def link(self, urls={}) -> str:
        """Add custom links to the dates.

        Args:
            urls (dict, optional): A dictionary with date:url format. Defaults to {}.

        Returns:
            str: A formatted markdown calendar view with links attached to the selected dates.
        """
        markdown_str = ""
        dic = get_lang_dict(self.lang)
        table = self.matrix
        calendar_header = [dic[day] for day in table[0]]
        calendar_header = "|" + "|".join(calendar_header) + "|" + "\n"
        markdown_str += calendar_header

        calendar_divider = (
            "|" + "|".join([":-:" for _ in range(len(table[0]))]) + "|" + "\n"
        )
        markdown_str += calendar_divider

        for date_row in table[1:]:
            date_row_str = "|"
            for i in range(0, len(date_row)):
                if self.week_no and i == 0:
                    date_row_str += str(date_row[0]) + "|"
                else:
                    should_fill = self.fill_calendar or date_row[i].month == self.month
                    url = urls.get(date_row[i])
                    day_str = (
                        f"[{str(date_row[i].day)}]({url})"
                        if url
                        else str(date_row[i].day)
                    )
                    date_row_str += f"{day_str}|" if should_fill else "|"
            markdown_str += date_row_str + "\n"
        return markdown_str

    def selective(
        self,
        selected=[],
        selected_date_text: str = None,
        not_selected_date_text: str = "",
    ) -> str:
        """Show selected dates on the calendar only.

        Args:
            selected (list, optional): A list of dates to be shown on the calendar. Defaults to [].
            selected_date_text (str, optional): Text to be shown in place of dates. if None it will be normal date otherwise any custom text even emojis. Defaults to None (date).
            not_selected_date_text (str, optional): Text to be shown in place of non selected dates. defaults to blank otherwise any given text even emojis. Defaults to "" (blank).

        Returns:
            str: Returns a markdown table view of the month.
        """
        markdown_str = ""
        dic = get_lang_dict(self.lang)

        table = self.matrix
        calendar_header = [dic[day] for day in table[0]]

        calendar_header = "|" + "|".join(calendar_header) + "|" + "\n"
        markdown_str += calendar_header

        calendar_divider = (
            "|" + "|".join([":-:" for _ in range(len(table[0]))]) + "|" + "\n"
        )
        markdown_str += calendar_divider

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

                    day_str = (
                        _selected_date_text
                        if date_row[i] in selected
                        else not_selected_date_text
                    )
                    date_row_str += f"{day_str}|" if should_fill else "|"
            markdown_str += date_row_str + "\n"

        return markdown_str

__all__ = ['CalendarFusion']