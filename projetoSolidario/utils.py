from datetime import datetime
from calendar import HTMLCalendar
from django.utils import timezone
from .models import Evento  # Certifique-se de que o modelo correto está importado
import locale

# Define o locale para português do Brasil
import locale
from datetime import datetime

try:
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_TIME, "")  # Fallback


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, events=None):
        self.year = year if year is not None else timezone.now().year
        self.month = month if month is not None else timezone.now().month
        self.events = (
            events if events is not None else Evento.objects.none()
        )  # Garante que seja uma queryset
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        # Filtra eventos do dia, se houver
        events_per_day = (
            events.filter(data_evento__day=day).order_by("data_evento")
            if events
            else []
        )
        d = ""
        for event in events_per_day:
            # Supondo que o `get_absolute_url()` retorna o link correto para o evento
            d += (
                f"<li><a href='{event.get_absolute_url()}'>{event.nome_evento}</a></li>"
            )

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d if d else '<li>Sem eventos</li>'} </ul></td>"
        return "<td></td>"

    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr> {week} </tr>"

    def formatmonth(self, withyear=True):
        events = self.events  # Usando os eventos passados para a classe

        # Cabeçalho do mês
        cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"

        # Adiciona cada semana ao calendário
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"

        return cal

    def formatmonthname(self, theyear, themonth, withyear=True):
        # Utiliza a localidade definida para mostrar o nome do mês
        month_name = datetime(theyear, themonth, 1).strftime("%B")
        if withyear:
            return f'<tr><th colspan="7" class="month">{month_name} {theyear}</th></tr>'
        else:
            return f'<tr><th colspan="7" class="month">{month_name}</th></tr>'
