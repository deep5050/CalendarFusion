from CalendarFusion import CalendarFusion
# CalendarFusion = __import__("CalendarFusion/CalendarFusion.py")
from datetime import date

import unittest


class CalendarFusion_tests(unittest.TestCase):
    ############# normal calendar test ###############
    def test_calendar_exact_generation_fill_calendar(self):
        cf = CalendarFusion.CalendarFusion(
            year=2023, month=9, fill_calendar=True, start_from_sunday=False
        )
        result = cf.calendar()
        expected_result = "|Mon|Tue|Wed|Thu|Fri|Sat|Sun|\n\
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n\
|28|29|30|31|1|2|3|\n\
|4|5|6|7|8|9|10|\n\
|11|12|13|14|15|16|17|\n\
|18|19|20|21|22|23|24|\n\
|25|26|27|28|29|30|1|\n"
        self.assertEqual(result, expected_result, "should exact same as september 2023")

    def test_calendar_with_week_no(self):
        cf = CalendarFusion.CalendarFusion(
            year=2023,
            month=8,
            fill_calendar=True,
            start_from_sunday=False,
            week_no=True,
        )
        result = cf.calendar()
        self.assertIn("Week", result)
        self.assertEqual(result.count("|"), 9 * 7, "Check if it's a 9x7 table")

    ######################## starts with monday ###################
    def test_calendar_starts_with_monday(self):
        cf = CalendarFusion.CalendarFusion(
            year=2023,
            month=8,
            fill_calendar=False,
            start_from_sunday=False,
            lang="eng",
            week_no=True,
        )
        result = cf.calendar()
        self.assertEqual(
            result.count("|Week|Mon|Tue|"),
            1,
            "there must me exact one etry of column where monday comes first",
        )

    ########### calendar with hindi language ###
    def test_calendar_starts_with_lang_hindi(self):
        cf = CalendarFusion.CalendarFusion(
            year=2023,
            month=8,
            fill_calendar=False,
            start_from_sunday=False,
            lang="hi",
            week_no=True,
        )
        result = cf.calendar()
        self.assertEqual(
            result.count("|सप्ताह|सोम|मंगल|बुध|गुरु|शुक्र|शनि|रवि|"),
            1
        )


################### calendar with bengali language ############
    def test_calendar_starts_with_lang_bengali(self):
        cf = CalendarFusion.CalendarFusion(
            year=2023,
            month=8,
            fill_calendar=False,
            start_from_sunday=False,
            lang="bn",
            week_no=True,
        )
        result = cf.calendar()
        self.assertEqual(
            result.count("|সপ্তাহ|সোম|মঙ্গল|বুধ|বৃহঃ|শুক্র|শনি|রবি|"),
            1
        )
    ######################### calendar with selected dates ####################
    def test_calendar_with_selected_dates(self):
        cf = CalendarFusion.CalendarFusion(
            year=2023,
            month=8,
            fill_calendar=False,
            start_from_sunday=True,
            lang="eng",
            week_no=True,
        )
        selected_dates = [
            date(2023, 8, 23),
            date(2023, 8, 1),
            date(2023, 8, 27),
            date(2023, 7, 31),
            date(2023, 8, 20),
            date(2023, 8, 7),
        ]
        expeted_result = "|Week|Sun|Mon|Tue|Wed|Thu|Fri|Sat|\n\
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n\
|30|||1|||||\n\
|31||7||||||\n\
|32||||||||\n\
|33|20|||23||||\n\
|34|27|||||||\n"
        result = cf.selective(selected=selected_dates)
        self.assertEqual(result, expeted_result, "should match exactly")
        self.assertIn("||", result, "there must be atleast one blank date")

    ########## calendar with selected dates and emoji as text ###########

    def test_calendar_with_selected_dates_emoji(self):
        cf = CalendarFusion.CalendarFusion(
            year=2023,
            month=8,
            fill_calendar=True,
            start_from_sunday=True,
            lang="eng",
            week_no=False,
        )
        selected_dates = [
            date(2023, 8, 23),
            date(2023, 8, 1),
            date(2023, 8, 27),
            date(2023, 7, 31),
            date(2023, 8, 20),
            date(2023, 8, 7),
        ]
        expeted_result = """|Sun|Mon|Tue|Wed|Thu|Fri|Sat|\n\
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n\
|:red_circle:|:green_circle:|:green_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|\n\
|:red_circle:|:green_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|\n\
|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|\n\
|:green_circle:|:red_circle:|:red_circle:|:green_circle:|:red_circle:|:red_circle:|:red_circle:|\n\
|:green_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|\n"""

        result = cf.selective(
            selected=selected_dates,
            selected_date_text=":green_circle:",
            not_selected_date_text=":red_circle:",
        )
        self.assertEqual(result, expeted_result, "should match exactly")
        self.assertIn(
            "|:green_circle:|", result, "there must be atleast one selected date text"
        )

    ##################### calendar with links ###################
    def test_calendar_with_links(self):
        cf = CalendarFusion.CalendarFusion(
            year=2023,
            month=8,
            fill_calendar=True,
            start_from_sunday=True,
            lang="eng",
            week_no=False,
        )
        entity = {}
        entity[date(2023, 8, 12)] = "https://google.com"
        entity[date(2023, 8, 22)] = "https://google.com"
        entity[date(2023, 8, 2)] = "https://bing.com"

        result = cf.link(urls=entity)
        self.assertEqual(
            result.count("google.com"),
            2,
            "there must be exact two dates with link to google.com",
        )
        self.assertEqual(
            result.count("bing.com"),
            1,
            "there must be exact one date with link to bing.com ",
        )


if __name__ == "__main__":
    unittest.main()
