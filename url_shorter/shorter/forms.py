from django import forms
from django.utils.translation import gettext_lazy as _


class UrlToShortForm(forms.Form):
    long_url = forms.URLField(label=_('Long url'), required=True, widget=forms.Textarea)
