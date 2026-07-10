from django import forms
from .models import Center, Branch, Room
from common.forms import CommonLocationForm

class CenterForm(CommonLocationForm):
    class Meta(CommonLocationForm.Meta):
        model = Center
        fields = ['logo', 'website']

class BranchForm(CommonLocationForm):
    class Meta(CommonLocationForm.Meta):
        model = Branch
        fields = ['opening_time', 'closing_time', 'center']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
            'capacity',
            'room_type',
            'has_projector',
            'floor',
            'branch'
        ]