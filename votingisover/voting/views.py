from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from voting.models import Voting
from voting.forms import VotingForm


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
    context['votings'] = Voting.objects.all()
    return render(request, 'registration/votingisover.html', context)


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
