from django import forms



class VotingForm(forms.Form):
    header = forms.CharField()
    type = forms.CharField()
    vote = forms.ChoiceField(widget = forms.RadioSelect)
