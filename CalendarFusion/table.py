#!/usr/bin/env python

import calendar


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
