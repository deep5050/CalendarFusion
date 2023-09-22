#!/usr/bin/env python

from datetime import datetime

from .lang import get_lang_dict
from .table import generate_matrix


class CalendarFusion:
    """This class will be used to generate a month's custom calendar views."""

    def __init__(
        self,
        year: int = datetime.now().year,
        month: int = datetime.now().month,
        start_from_sunday: bool = False,
        week_no: bool = False,
        fill_calendar: bool = False,
        lang: str = "eng",
    ):
        """Initialize a month's calendar.

        Args:
            year (int, optional): Calendar year. Defaults to datetime.now().year.
            month (int, optional): Calendar month. Defaults to datetime.now().month.
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

    def style(self, style: str = "bold", selected: list[datetime] = []) -> str:
        """Add styles to the dates.

        Args:
            style (str, optional): Formatting styles of the dates. options: bold,italic,strikeout,quote. Defaults to "bold".
            selected (list[datetime], optional): Apply formatting styles to the selected dates only. expects a list of dates Defaults to [].

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

    def link(self, urls: dict[datetime, str] = {}) -> str:
        """Add custom links to the dates.

        Args:
            urls (dict[datetime,str], optional): A dictionary with date:url format. Defaults to {}.

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
        selected: list[datetime] = [],
        selected_date_text: str = None,
        not_selected_date_text: str = "",
    ) -> str:
        """Show selected dates on the calendar only.

        Args:
            selected (list[datetime], optional): A list of dates to be shown on the calendar. Defaults to [].
            selected_date_text (str, optional): Text to be shown in place of dates. \
            if None it will be normal date otherwise any custom text even emojis. Defaults to None (date).
            not_selected_date_text (str, optional): Text to be shown in place of non selected dates. \
                defaults to blank otherwise any given text even emojis. Defaults to "" (blank).

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


__all__ = ["CalendarFusion"]
