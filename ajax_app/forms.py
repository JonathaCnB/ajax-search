from django import forms

from .models import WebSeries


class WebSeriesForm(forms.ModelForm):
    class Meta:
        model = WebSeries
        fields = [
            "image",
            "name",
            "description",
        ]
