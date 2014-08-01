from django.contrib.auth.decorators import login_required
from finder.forms import *
from django.shortcuts import render, redirect
from finder.models import Event
# Create your views here.


def home(request):
    return render(request, 'index.html')


# Careful using a variable called 'set', this is a built in python term and could cause errors

# You could use 1 url that has 'margarita', 'coffee', 'lounge', etc in the url and only make 1 view
# that pulls the Event from the database based on that category name instead of 3 hardcoded views.
# If you added another event type, this would automatically work instead of needing to add a new view.
def margarita(request):
    set = Event.objects.filter(category__pk=1)
    return render(request, 'margarita.html', {'set': set})


def coffee(request):
    set = Event.objects.filter(category__pk=2)
    return render(request, 'coffee.html', {'set':set})


def lounge(request):
    set = Event.objects.filter(category__pk=3)
    return render(request, 'lounge.html', {'set':set})


@login_required()
def profile(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("margarita")
    else:
        form = EventForm()

    return render(request, "profile.html", {
        'form': form,
    })


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

