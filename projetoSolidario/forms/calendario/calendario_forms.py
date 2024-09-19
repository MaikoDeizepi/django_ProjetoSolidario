from django.forms import ModelForm
from projetoSolidario.models import Event
from django import forms
from django.utils import timezone
import datetime


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def format_value(self, value):
        if isinstance(value, datetime.datetime) and timezone.is_naive(value):
            value = timezone.make_aware(value)
            return value.strftime("%Y-%m-%dT%H:%M")
        return value


class EventForm(ModelForm):
    start_time = forms.DateTimeField(
        widget=DateTimeLocalInput(attrs={"class": "form-control"}),
        input_formats=["%Y-%m-%dT%H:%M"],
    )
    end_time = forms.DateTimeField(
        widget=DateTimeLocalInput(attrs={"class": "form-control"}),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    def clean_start_time(self):
        start_time = self.cleaned_data["start_time"]
        return (
            timezone.make_aware(start_time)
            if timezone.is_naive(start_time)
            else start_time
        )

    def clean_end_time(self):
        end_time = self.cleaned_data["end_time"]
        return (
            timezone.make_aware(end_time) if timezone.is_naive(end_time) else end_time
        )

    class Meta:
        model = Event
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
