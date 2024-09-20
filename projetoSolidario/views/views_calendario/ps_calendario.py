from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render
from django.views import View
from django.utils.safestring import mark_safe
import calendar
from datetime import datetime  # Importando datetime diretamente
from projetoSolidario.models import (
    Evento,
)  # Certifique-se de que o modelo correto está sendo importado


class CalendarView(View):
    def get(self, request, *args, **kwargs):
        # Usar timezone-aware datetime
        today = timezone.now()  # Usando timezone-aware datetime
        year = int(request.GET.get("year", today.year))
        month = int(request.GET.get("month", today.month))

        # Tornar os dias do mês timezone-aware
        # Criar objetos datetime em vez de date com hora zero
        first_day = timezone.make_aware(
            datetime(year, month, 1, 0, 0, 0)
        )  # Primeiro dia do mês
        days_in_month = calendar.monthrange(year, month)[1]
        last_day = timezone.make_aware(
            datetime(year, month, days_in_month, 23, 59, 59)
        )  # Último dia do mês

        # Alterado para usar o modelo `Evento` e o campo `data_evento`
        eventos = Evento.objects.filter(
            data_evento__gte=first_day, data_evento__lte=last_day
        )

        cal = Calendar(year, month, events=eventos)
        html_cal = cal.formatmonth(withyear=True)

        context = {
            "calendar": mark_safe(html_cal),
            "prev_month": prev_month(year, month),
            "next_month": next_month(year, month),
        }

        return render(
            request, "projetoSolidario/tela_calendario/calendar.html", context
        )


def prev_month(year, month):
    prev_month = month - 1
    prev_year = year
    if prev_month == 0:
        prev_month = 12
        prev_year -= 1
    return f"year={prev_year}&month={prev_month}"


def next_month(year, month):
    next_month = month + 1
    next_year = year
    if next_month == 13:
        next_month = 1
        next_year += 1
    return f"year={next_year}&month={next_month}"


# Lógica da classe Calendar no utils.py (garantir que a classe esteja corretamente implementada)
class Calendar:
    def __init__(self, year, month, events=None):
        self.year = year
        self.month = month
        self.events = events if events else []

    def formatmonth(self, withyear=True):
        """
        Gera o HTML do mês formatado.
        """
        # Cabeçalho do mês
        month_html = (
            f"<table border='0' cellpadding='0' cellspacing='0' class='calendar'>\n"
        )
        month_html += (
            f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        )
        month_html += f"{self.formatweekheader()}\n"

        # Criar semanas e dias do mês
        for week in self.monthdays2calendar(self.year, self.month):
            month_html += f"{self.formatweek(week, self.events)}\n"

        return month_html + "</table>"

    def formatweek(self, week, events):
        """
        Formata a semana do calendário.
        """
        week_html = "<tr>"
        for d, weekday in week:
            week_html += self.formatday(d, events)
        return week_html + "</tr>"

    def formatday(self, day, events):
        """
        Formata o dia do calendário, mostrando os eventos se existirem.
        """
        # Filtra eventos com base no dia, considerando que eventos já são timezone-aware
        events_per_day = events.filter(data_evento__day=day).order_by("data_evento")
        day_html = ""
        for event in events_per_day:
            day_html += f"<li> {event.nome_evento} </li>"

        if day_html:
            return f"<td><span class='date'>{day}</span><ul> {day_html} </ul></td>"
        return f"<td><span class='date'>{day}</span></td>"

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Cabeçalho do mês.
        """
        if withyear:
            s = f"{calendar.month_name[themonth]} {theyear}"
        else:
            s = f"{calendar.month_name[themonth]}"
        return f"<tr><th colspan='7' class='month'>{s}</th></tr>"

    def formatweekheader(self):
        """
        Cabeçalho da semana.
        """
        s = ""
        for day in calendar.weekheader(2).split():
            s += f"<th class='weekday'>{day}</th>"
        return f"<tr>{s}</tr>"

    def monthdays2calendar(self, year, month):
        """
        Retorna uma lista de semanas representadas por listas de pares (dia, dia_da_semana).
        """
        return calendar.Calendar().monthdays2calendar(year, month)
