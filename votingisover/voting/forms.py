from django import forms

CHOICES = [
('Yes', 'Да, конечно'),
('No', 'Нет, но я подумаю')
]

class VotingForm(forms.Form):
    header = forms.CharField()
    vote = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)
