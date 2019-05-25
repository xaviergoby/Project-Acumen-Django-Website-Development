
# Create your views here.
from django.http import HttpResponse
import datetime
from django.shortcuts import render
import random




def homepage(request):
    return render(request, template_name='study/homepage.html')

def grind(request):
    easter_egg_naughty_words = ["nerd", "champ", "dork", "try hard", "champ", "you smarticle-particle"]
    random_tease_idx = random.randrange(0, len(easter_egg_naughty_words))
    random_tease = easter_egg_naughty_words[random_tease_idx]
    return render(request, 'study/grind.html', {"random_tease":random_tease})

def knowledge_base(request):
    return render(request, template_name='study/knowledge_base.html')

def about(request):
    return render(request, template_name='study/about.html')

def contact(request):
    return render(request, template_name='study/contact.html')

def test_view(request):
    return render(request, template_name='study/test_view.html')


# from django.shortcuts import render


# def test_view(request):
#     firstname = request.POST.get('Firstname')
#     lastname = request.POST.get('Lastname')
#     city = request.POST.get('City')
#     state = request.POST.get('State')
#     submitbutton = request.POST.get('Submit')
#     context = {'firstname': firstname, 'lastname': lastname,
#                'city': city, 'state': state,
#                'submitbutton': submitbutton}
#     return render(request, 'study/test_view.html', context)

