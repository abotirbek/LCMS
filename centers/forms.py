from django import forms
from .models import Centers, Branch, CommonLocation

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
class CenterForm(CommonLocationForm):
    class Meta(CommonLocationForm.Meta):
        model = Centers
        fields = ['logo', 'website']

class BranchForm(CommonLocationForm):
    class Meta(CommonLocationForm.Meta):
        model = Branch
        fields = ['opening_time', 'closing_time', 'center']