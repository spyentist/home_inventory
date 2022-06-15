from django import forms
from pims.models import *



        # Possibility for future views.
        # https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
        # https://stackoverflow.com/questions/31414091/how-to-save-many-to-many-fields-in-django-create-view


class containerForm(forms.ModelForm):
    field_order = ['location', 'row_letter', 'column_number', 'description', 'season', 'is_partial',]
    location = forms.CharField(max_length=200)
    row_letter = forms.CharField(max_length=1)
    column_number = forms.IntegerField(max_value=99)
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = container
        fields = ['location', 'row_letter', 'column_number', 'description', 'season', 'is_partial']