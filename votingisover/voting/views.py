from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from voting.models import Voting
from voting.forms import VotingForm, CreateVotingForm
from django import forms


# Create your views here.


def index(request):
    context = {}
    current_user = request.user
    context['username'] = current_user
    return render(request, "index.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def voting(request):
    context = {}
    current_user = request.user
    context['username'] = current_user
    context['votings'] = []
    all_variants = Variant.objects.all()
    for voting in Voting.objects.all():
        variants = []
        for variant in all_variants:
            if variant.voting_id == voting:
                variants.append(variant)
        context['votings'].append(VotingForm(header = voting.header,
                                type = voting.type, vote = forms.ChoiceField(
                                choices = variants, widget = forms.RadioSelect)))
##    for voting in Voting.objects.all():
##        next_voting = {}
##        next_voting['header'] = voting.header
##        next_voting['type'] = voting.type
##        next_voting['variants'] = []
##        for variant in all_variants:
##            if variant.voting_id == voting:
##                next_voting['variants'].append(variant)
##        context['votings'].append(next_voting)
    return render(request, 'registration/votingisover.html', context)

def make_voting(request):
    context = {}
    current_user = request.user
    context['username'] = current_user
    context['form'] = CreateVotingForm()
    context['form'].variants.append(forms.CharField(label="Variant 1"))
    context['form'].variants.append(forms.CharField(label="Variant 2"))
    if request.method == 'POST':
        form = CreateVotingForm(request.POST)
        if form.is_valid():
            form.save()
            voting = Voting(type = form.type, header = form.header)
            voting.save()
            variants = []
            for variant in form.variants:
                variants.append(Variant(text = variant, voting_id = voting))
                variants[-1].save()
    ##context['votings'] = VotingDescription.objects.all()
    return render(request, 'make_voting.html', context)


def exit(request):
    logout(request)
    return HttpResponseRedirect('/')

def makeVote(request):
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

    else:
        form = VotingForm()
