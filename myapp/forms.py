from django import forms
from django.utils.translation import gettext_lazy as _
from myapp.models import UrlModel


class UrlModelForm(forms.ModelForm):
    keyword = forms.CharField(required=False)

    class Meta:
        model = UrlModel
        fields = ("keyword", "original_url")
        widgets = {
            "keyword": forms.TextInput(attrs={"class": "form-control"}),
            "original_url": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "keyword": _("Optional"),
        }

