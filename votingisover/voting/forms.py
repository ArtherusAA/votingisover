from django import forms



class VotingForm(forms.Form):
    header = forms.CharField()
    type = forms.CharField()
    vote = forms.ChoiceField(widget = forms.RadioSelect)

class CreateVotingForm(forms.Form):
    type = forms.CharField(label="Voting Type")
    header = forms.CharField(label="Voting Header")
    variants = []
