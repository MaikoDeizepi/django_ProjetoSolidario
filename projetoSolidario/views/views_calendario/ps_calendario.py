from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils.safestring import mark_safe
import calendar
from datetime import datetime  # Importando datetime diretamente
from projetoSolidario.models import (
    Evento,
)
from projetoSolidario.forms.evento.cadastro_evento import (
    EventoForm,
)  # Certifique-se de que o modelo correto está sendo importado
import locale


try:
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_TIME, "")  # Fallback para o locale padrão do sistema


@login_required(login_url="projetosolidario:index")
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)

    contexto = {"eventos": evento, "title": "Consultar Eventos"}

    return render(request, "projetoSolidario/tela_evento/editar_id.html", contexto)


class CalendarView(View):

    def get(self, request, *args, **kwargs):
        today = timezone.now()
        year = int(request.GET.get("year", today.year))
        month = int(request.GET.get("month", today.month))

        first_day = timezone.make_aware(datetime(year, month, 1, 0, 0, 0))
        days_in_month = calendar.monthrange(year, month)[1]
        last_day = timezone.make_aware(datetime(year, month, days_in_month, 23, 59, 59))

        # Aqui você deve garantir que 'eventos' seja uma queryset
        eventos = Evento.objects.filter(
            data_evento__gte=first_day, data_evento__lte=last_day
        )

        cal = Calendar(
            year, month, events=eventos
        )  # Certifique-se de que isso é uma queryset
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
        if not isinstance(events, (list, set)):  # Garantir que seja uma queryset
            events_per_day = events.filter(data_evento__day=day).order_by("data_evento")
        else:
            events_per_day = []  # Caso events seja uma lista, trate isso adequadamente

        d = ""
        for event in events_per_day:
            d += (
                f"<li><a href='{event.get_absolute_url()}'>{event.nome_evento}</a></li>"
            )

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"

    def formatmonthname(self, theyear, themonth, withyear=True):
        # Utiliza a localidade definida para mostrar o nome do mês em português
        month_name = datetime(theyear, themonth, 1).strftime("%B")
        # Capitaliza a primeira letra do nome do mês e inclui o ano, se necessário
        if withyear:
            return f'<tr><th colspan="7" class="month">{month_name.capitalize()} {theyear}</th></tr>'
        else:
            return (
                f'<tr><th colspan="7" class="month">{month_name.capitalize()}</th></tr>'
            )

    def formatweekheader(self):
        """
        Cabeçalho da semana com dias em português.
        """
        s = ""
        # Utiliza os nomes dos dias em português
        dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
        for dia in dias_semana:
            s += f"<th class='weekday'>{dia}</th>"
        return f"<tr>{s}</tr>"

    def monthdays2calendar(self, year, month):
        """
        Retorna uma lista de semanas representadas por listas de pares (dia, dia_da_semana).
        """
        return calendar.Calendar().monthdays2calendar(year, month)
