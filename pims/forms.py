from django import forms
from pims.models import *

class CreateItemContainerForm(forms.ModelForm):
    class Meta:
        model = item_container
        fields = ['item', 'quantity', 'container']

    # item = forms.ModelMultipleChoiceField(
    #     queryset=item_container.item.get(pk=1),
    #     widget=forms.CheckboxSelectMultiple
    # )

    quantity = forms.IntegerField()

    container = forms.CheckboxInput()




        # https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
        # https://stackoverflow.com/questions/31414091/how-to-save-many-to-many-fields-in-django-create-view