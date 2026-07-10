from django import forms
from .models import CommonIndividuals, CommonLocation

class CommonIndividualsForm(forms.ModelForm):
    class Meta:
        model = CommonIndividuals
        fields = [
            'name',
            'last_name',
            'birth_date',
            'phone_number',
            'email'
        ]

class CommonLocationForm(forms.ModelForm):
    class Meta:
        model = CommonLocation
        fields = [
            'name',
            'phone_number',
            'email',
            'address',
            'city',
            'district',
            'country'
        ]