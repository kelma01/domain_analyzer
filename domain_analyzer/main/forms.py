from django import forms

class TextInputForm(forms.Form):
    user_input = forms.CharField(label='Enter Domain', max_length=100)