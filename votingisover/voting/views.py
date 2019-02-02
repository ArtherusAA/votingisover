from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from voting.models import Voting
from voting.forms import VotingForm
from voting.models import Vote
import datetime


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
    if request.method == 'POST':
        newVote = Vote(date = datetime.datetime.now(), user_id = request.user)
        newVote.save()
    return render(request, 'registration/votingisover.html', context)

def make_voting(request):
    context = {}
    current_user = request.user
    context['username'] = current_user
    context['votings'] = VotingDescription.objects.all()
    return render(request, 'make_voting.html', context)


def exit(request):
    logout(request)
    return HttpResponseRedirect('/')
