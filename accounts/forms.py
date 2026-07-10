from django import forms
from .models import Profile, CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = (
            "phone_number",
            "full_name",
            "birth_date",
            "is_student",
            "password",
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            phone_number=self.cleaned_data["phone_number"],
            password=self.cleaned_data["password"],
            full_name=self.cleaned_data["full_name"],
            birth_date=self.cleaned_data["birth_date"],
            is_student=self.cleaned_data["is_student"],
        )
        return user

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=16)
    password = forms.CharField(max_length=20)

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            'bio'
        ]