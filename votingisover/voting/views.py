from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from voting.models import Voting, Variant, Vote
from voting.forms import VotingForm, CreateVotingForm
from django import forms
from static import draw_batch
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
    draw_batch()
    context = {}
    current_user = request.user
    if not request.user.is_authenticated:
        return redirect('/')
    context['username'] = current_user
    if request.method == "POST":
        for key in request.POST.keys():
            if key[:6] == "voting":
                variant_id = int(request.POST[key][7:])
                variant = Variant.objects.filter(id=variant_id)
                vote = Vote(date=datetime.datetime.now(), user_id=current_user, variant_id=variant[0])
                vote.save()
            return redirect("/voting")
    context['votings'] = []
    all_variants = Variant.objects.all()
    for voting in Voting.objects.all():
        variants = all_variants.filter(voting_id = voting)
        ##variants = Variant.objects.filter()
        ##for variant in all_variants:
            ##if variant.voting_id == voting:
                ##variants.append(variant)
        context['votings'].append({"header": voting.header, "type": voting.type,
        "id": voting.id, "variants": variants})
        ##context['votings'].append(VotingForm(header = voting.header,
                                ##type = voting.type, vote = variants))
    if request.method == 'POST':
        pass
    return render(request, 'registration/votingisover.html', context)

def make_voting(request):
    context = {}
    current_user = request.user
    if not request.user.is_authenticated:
        return redirect('/')
    context['username'] = current_user
    context['form'] = CreateVotingForm()
    context['form'].variants = []
    if request.method == 'POST':
        keys = request.POST.keys()
        checkType = checkHeader = checkVariant1 = checkVariant2 = False
        for k in keys:
            if k == 'header':
                checkHeader = True
            elif k == 'type':
                checkType = True
            elif k == 'Variant 1' and request.POST[k] != "":
                checkVariant1 = True
            elif k == 'Variant 2' and request.POST[k] != "":
                checkVariant2 = True

        if checkType and checkHeader and checkVariant1 and checkVariant2:
            voting = Voting(type = request.POST['type'], header = request.POST['header'])
            voting.save()
            variants = []
            for k in keys:
                if k != 'type' and k != 'header' and k[:7] == 'Variant':
                    variants.append(Variant(text = request.POST[k], voting_id = voting))
                    variants[-1].save()
        else:
            context['form'] = CreateVotingForm()
        return redirect("/make_voting")
    else:
        #context['form'] = CreateVotingForm()
        context['form'].variants.append(forms.CharField(label="Variant 1"))
        context['form'].variants.append(forms.CharField(label="Variant 2"))
    return render(request, 'make_voting.html', context)


def exit(request):
    logout(request)
    return HttpResponseRedirect('/')
