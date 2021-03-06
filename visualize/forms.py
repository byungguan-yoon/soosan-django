from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "username"})
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password"}),
    )
