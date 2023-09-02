# Table of Contents

* [CalendarFusion](#CalendarFusion)
* [CalendarFusion.CalendarFusion](#CalendarFusion.CalendarFusion)
  * [CalendarFusion](#CalendarFusion.CalendarFusion.CalendarFusion)
    * [\_\_init\_\_](#CalendarFusion.CalendarFusion.CalendarFusion.__init__)
    * [calendar](#CalendarFusion.CalendarFusion.CalendarFusion.calendar)
    * [style](#CalendarFusion.CalendarFusion.CalendarFusion.style)
    * [link](#CalendarFusion.CalendarFusion.CalendarFusion.link)
    * [selective](#CalendarFusion.CalendarFusion.CalendarFusion.selective)

<a id="CalendarFusion"></a>

# CalendarFusion

<a id="CalendarFusion.CalendarFusion"></a>

# CalendarFusion.CalendarFusion

<a id="CalendarFusion.CalendarFusion.CalendarFusion"></a>

## CalendarFusion Objects

```python
class CalendarFusion()
```

This class will be used to generate a month's custom calendar views.

<a id="CalendarFusion.CalendarFusion.CalendarFusion.__init__"></a>

#### \_\_init\_\_

```python
def __init__(year=datetime.now().year,
             month=datetime.now().month,
             start_from_sunday=False,
             week_no=False,
             fill_calendar=False,
             lang="eng")
```

Initialize a month's calendar.

**Arguments**:

- `year` __type_, optional_ - Calendar year. Defaults to datetime.now().year.
- `month` __type_, optional_ - Calendar month. Defaults to datetime.now().month.
- `start_from_sunday` _bool, optional_ - Specifies if the first day of the week is sunday or not. Defaults to False (monday).
- `week_no` _bool, optional_ - Week no of the given month. Defaults to False.
- `fill_calendar` _bool, optional_ - Specifies if the the calendar should fill with previous and next month's dates. Defaults to False.
- `lang` _str, optional_ - Calendar language. Defaults to "eng".

<a id="CalendarFusion.CalendarFusion.CalendarFusion.calendar"></a>

#### calendar

```python
def calendar() -> str
```

Generate calendar view with no customization

**Returns**:

- `str` - Returns a markdown table as output.

<a id="CalendarFusion.CalendarFusion.CalendarFusion.style"></a>

#### style

```python
def style(style="bold", selected=[]) -> str
```

Add styles to the dates.

**Arguments**:

- `style` _str, optional_ - Formatting styles of the dates. options: bold,italic,strikeout,quote. Defaults to "bold".
- `selected` _list, optional_ - Apply formatting styles to the selected dates only. expects a list of dates Defaults to [].
  

**Returns**:

- `str` - Returns a markdown table as output.

<a id="CalendarFusion.CalendarFusion.CalendarFusion.link"></a>

#### link

```python
def link(urls={}) -> str
```

Add custom links to the dates.

**Arguments**:

- `urls` _dict, optional_ - A dictionary with date:url format. Defaults to {}.
  

**Returns**:

- `str` - A formatted markdown calendar view with links attached to the selected dates.

<a id="CalendarFusion.CalendarFusion.CalendarFusion.selective"></a>

#### selective

```python
def selective(selected=[],
              selected_date_text: str = None,
              not_selected_date_text: str = "") -> str
```

Show selected dates on the calendar only.

**Arguments**:

- `selected` _list, optional_ - A list of dates to be shown on the calendar. Defaults to [].
- `selected_date_text` _str, optional_ - Text to be shown in place of dates. if None it will be normal date otherwise any custom text even emojis. Defaults to None (date).
- `not_selected_date_text` _str, optional_ - Text to be shown in place of non selected dates. defaults to blank otherwise any given text even emojis. Defaults to "" (blank).
  

**Returns**:

- `str` - Returns a markdown table view of the month.

