from django.contrib.auth.decorators import login_required
from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from projetoSolidario.models import Event
from projetoSolidario.forms.calendario.calendario_forms import EventForm
from projetoSolidario.utils import Calendar


class CalendarView(View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        year = int(request.GET.get("year", today.year))
        month = int(request.GET.get("month", today.month))

        first_day = date(year, month, 1)
        days_in_month = calendar.monthrange(year, month)[1]
        last_day = date(year, month, days_in_month)

        events = Event.objects.filter(start_time__gte=first_day, end_time__lte=last_day)

        cal = Calendar(year, month, events=events)
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


class EventView(View):
    def get(self, request, event_id=None):
        instance = get_object_or_404(Event, pk=event_id) if event_id else None
        form = EventForm(instance=instance)
        return render(
            request,
            "projetoSolidario/tela_calendario/event.html",
            {"form": form, "instance": instance},
        )

    def post(self, request, event_id=None):
        instance = get_object_or_404(Event, pk=event_id) if event_id else None
        form = EventForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("projetosolidario:calendar"))
        return render(
            request, "projetoSolidario/tela_calendario/event.html", {"form": form}
        )
