from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=180)
    last_name = forms.CharField(max_length=180)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=180)