from django.contrib.auth.decorators import login_required
from finder.forms import *
from django.shortcuts import render, redirect

# Create your views here.
def chat(request):
    return render(request, 'chat.html')

def home(request):
    return render(request, 'index.html')


def margarita(request):
    people = Member.objects.filter(event__category__name='I want a margarita!')
    return render(request, 'margarita.html', {'people': people})


def coffee(request):
    people = Member.objects.filter(event__category__name='I want to grab coffee!')
    return render(request, 'margarita.html', {'people': people})

def lounge(request):
    people = Member.objects.filter(event__category__name='I want to lounge somewhere!')
    return render(request, 'margarita.html', {'people': people})

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

