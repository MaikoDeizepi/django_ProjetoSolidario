from datetime import datetime
from calendar import HTMLCalendar
from .models import Event
import locale

# Define o local para português do Brasil
locale.setlocale(locale.LC_TIME, "pt_BR.utf8")


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, events=None):
        self.year = year if year is not None else datetime.today().year
        self.month = month if month is not None else datetime.today().month
        self.events = events if events is not None else []
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day).order_by("start_time")
        d = ""
        for event in events_per_day:
            # Usar o `get_absolute_url()` atualizado que agora utiliza `event_id`
            d += f"<li><a href='{event.get_absolute_url()}'>{event.title}</a></li>"

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"

    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr> {week} </tr>"

    def formatmonth(self, withyear=True):
        events = self.events  # Usando os eventos passados para a classe

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"
        return cal

    def formatmonthname(self, theyear, themonth, withyear=True):
        month_name = datetime(theyear, themonth, 1).strftime("%B")
        if withyear:
            return f'<tr><th colspan="7" class="month">{month_name} {theyear}</th></tr>'
        else:
            return f'<tr><th colspan="7" class="month">{month_name}</th></tr>'
